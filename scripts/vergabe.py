"""Lädt Tagesexporte (OCDS, CC0) von oeffentlichevergabe.de und erzeugt Nischen-Auswertungen.
Nutzung: python3 scripts/vergabe.py [tage] [cpv-präfix ...]"""
import json, sys, io, zipfile, urllib.request, datetime, collections, os
days = int(sys.argv[1]) if len(sys.argv) > 1 else 7
prefixes = sys.argv[2:]
C = "data/cache"; os.makedirs(C, exist_ok=True)
def day(d):
    p = f"{C}/{d}.zip"
    if not os.path.exists(p):
        u = f"https://oeffentlichevergabe.de/api/notice-exports?pubDay={d}&format=ocds.zip"
        try: open(p, "wb").write(urllib.request.urlopen(u, timeout=60).read())
        except Exception as e: print("fehlt", d, e, file=sys.stderr); return []
    z = zipfile.ZipFile(p)
    return [json.load(z.open(n))["releases"][0] for n in z.namelist()]
import re
LF = re.compile(r"\b(GmbH|AG|SE|KG|mbB|PartG|GbR|OHG|UG|eG|e\.V\.|AöR|Ltd|Inc|S\.A\.|B\.V\.|GesmbH|Gruppe|Group|Ingenieurgesellschaft|Zweckverband)\b", re.I)
def pub(n): return n if LF.search(n) else "Einzelbieter (Name aus Datenschutzgründen ausgeblendet)"  # DSGVO: keine natürlichen Personen veröffentlichen
rel = []
for i in range(1, days + 1):
    rel += day((datetime.date.today() - datetime.timedelta(days=i)).isoformat())
def cpvs(r): return [it.get("classification", {}).get("id", "") for it in r.get("tender", {}).get("items", [])]
if not prefixes:  # Übersicht: Ausschreibungen je CPV-3 und Zuschläge mit Lieferanten
    c = collections.Counter(); names = {}
    for r in rel:
        if "tender" in r.get("tag", []):
            for x in {k[:3] for k in cpvs(r) if k}: c[x] += 1
    print(len(rel), "Meldungen"); [print(k, v) for k, v in c.most_common(40)]
    sys.exit()
hit = [r for r in rel if any(k.startswith(tuple(prefixes)) for k in cpvs(r))]
reg = os.environ.get("REGION", "")  # NUTS-Präfix des Auftraggebers, z. B. DE2 = Bayern
def breg(r): return next((p.get("address", {}).get("region", "") for p in r.get("parties", []) if "buyer" in p.get("roles", [])), "")
if reg: hit = [r for r in hit if breg(r).startswith(reg)]
out = [f"# Vergabe-Report CPV {','.join(prefixes)} · letzte {days} Tage (automatisch, KI-/Skript-erzeugt, ohne Gewähr)\n",
       "Quelle: Bekanntmachungsservice oeffentlichevergabe.de (CC0).\n", "## Offene Ausschreibungen"]
today = datetime.date.today().isoformat()
for r in hit:
    t = r.get("tender", {})
    if "tender" not in r.get("tag", []): continue
    dl = (t.get("tenderPeriod", {}).get("endDate") or "")[:10]
    if dl and dl < today: continue
    buyer = next((p["name"] for p in r.get("parties", []) if "buyer" in p.get("roles", [])), "")
    out.append(f"- **{t.get('title','')[:120]}** – {buyer[:70]} · Frist {dl or 's. Unterlagen'}" + (f" · [Unterlagen]({t['documents'][0]['url']})" if t.get('documents') and t['documents'][0].get('url') else ""))
out.append("\n## Zuschläge (Gewinner, Wert falls veröffentlicht)")
for r in hit:
    if "award" not in r.get("tag", []): continue
    sup = [pub(p["name"]) for p in r.get("parties", []) if "supplier" in p.get("roles", [])]
    val = sum(a.get("value", {}).get("amount") or 0 for a in r.get("awards", []))
    buyer = next((p["name"] for p in r.get("parties", []) if "buyer" in p.get("roles", [])), "")
    out.append(f"- {r.get('tender',{}).get('title','')[:100]} – {buyer[:50]} → {', '.join(sup[:3]) or 'k. A.'}" + (f" · {val:,.0f} €" if val > 1 else ""))
win = collections.Counter(pub(p["name"]) for r in hit if "award" in r.get("tag", []) for p in r.get("parties", []) if "supplier" in p.get("roles", []))
out.append("\n## Häufigste Gewinner im Zeitraum")
out += [f"- {n} – {c} Zuschlag/Zuschläge" for n, c in win.most_common(16) if not n.startswith("Einzelbieter")][:15]
print("\n".join(out))
