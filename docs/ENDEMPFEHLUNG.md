# Endempfehlung der Ideenfindung (Lauf 19, 2026-09-30)

## Empfehlung: H6b „Vergabe-Radar Planungsleistungen“ (CPV 71) + öffentliche Experiment-Story (H5)
Die Story ist der Kanal, der Radar ist das Produkt.

**Produkt:** Ein wöchentlicher Report für Architektur- und Ingenieurbüros. Er enthält die offenen Ausschreibungen für Planungsleistungen (national und EU, auch unterhalb der EU-Schwelle) und die **Zuschläge mit Gewinnern**: wer gewinnt bei welchem Auftraggeber, wer taucht neu im Markt auf, alles nach Bundesland filterbar. Erzeugt wird er per Skript (scripts/vergabe.py) aus CC0-Daten von oeffentlichevergabe.de. Die Lieferung kostet 0 $ Modellkosten und läuft in GitHub Actions.

**Warum diese Nische (Daten aus 14 Tagen, 10.929 Meldungen):**
- CPV 71 ist die zweitgrößte Kategorie: 632 Ausschreibungen und 375 Zuschläge in 14 Tagen. Bei **80 %** der Zuschläge steht der Gewinner dabei (Bau/45: 56 %, IT/72: 70 %).
- Viele kleine Büros (Zehntausende in Deutschland) haben kein Budget für DTAD (~200 €/Monat) und verlieren Zeit mit Portal-Suche. Die Zuschlagsdaten dienen der Wettbewerbsbeobachtung, und die bieten generische Alert-Dienste kaum an.
- Bau (45) ist größer, aber gesättigt (Vergabe24, DTAD, viele Start-ups). IT (72/48) ist zu klein.

**Grenzen (ehrlich):**
- Auftragswerte werden nur bei ~14 % der Zuschläge veröffentlicht. Preis-Intelligenz ist deshalb schwach, Gewinner-Intelligenz dagegen stark.
- Die Zahlungsbereitschaft ist für UNS nicht belegt (Stufe 0). Der Markt zahlt 18–200 €/Monat für Vergabe-Infos.
- Distribution ist weiterhin der Engpass. Ohne öffentliche Sichtbarkeit gibt es keinen Test.
- Realistische Erwartung: in 4 Wochen 0–10 Rückmeldungen. Der erste Umsatz kommt frühestens nach Stufe 2, also in 1–3 Monaten. Plausibler Preis: 9–19 €/Monat. Zum Vergleich: die Laufkosten liegen bei ~0,1–0,3 $/Tag Modellkosten, solange der Agent aktiv ist. Die Lieferung selbst kostet 0 $.
- Datenschutz: Namen natürlicher Personen (Einzelbieter) werden automatisch ausgeblendet. Veröffentlicht werden nur Firmen mit Rechtsform.

## Stufenplan
**Stufe 1 (jetzt, kostenlos, reversibel) – ACTION 3/5:** Ein pseudonymes öffentliches Repo (`vergabelabor/vergabe-radar`) wird per Export befüllt und GitHub Pages wird aktiviert. Die Seite ist rein informativ und nicht kommerziell: kein Angebot, kein Preis, keine Bestellung. Feedback läuft über GitHub-Issues, ein Opt-in ist das „Watch“ auf das Repo.
- Test E7: Report wöchentlich automatisch aktualisieren. Erfolg: ≥5 qualifizierte Rückmeldungen oder Opt-ins von Planern (Issue, Stern mit Profil, Anfrage) in 28 Tagen. Abbruch: 0 in 28 Tagen ⇒ H6b herabstufen.
- Der Agent misst per `gh api` Sterne, Issues und Forks. Seitenaufrufe sind für den Agenten nicht sichtbar; Maßstab sind Sterne, Issues, Forks.

**Stufe 2 (nur bei Erfolg von E7) – ACTION 4/5, gebündelt:** Gewerbeanmeldung, Merchant-of-Record-Shop (z. B. Lemon Squeezy/Paddle, übernimmt USt und Rechnung), Newsletter-Dienst mit Double-Opt-in (z. B. Buttondown, Free-Tier), Impressum und Datenschutzerklärung. Das Bezahl-Abo liefert personalisierte Filter (Region, Leistungsphase, Auftraggeber). Kosten: Gewerbe ~20–60 € (Mensch). Der Rest ist provisionsbasiert, es gibt keine Fixkosten.

## Setup-Spezifikation Stufe 1 (für ACTION 3/5)
1. Organisation `vergabelabor` anlegen (Free, Mitgliedschaft privat) und darin ein leeres öffentliches Repo `vergabe-radar`.
2. Fine-grained Token (nur dieses Repo, Contents RW + Pages RW) als Actions-Secret `PUBLIC_REPO_TOKEN` im privaten Repo.
3. Nach dem ersten Export des Agenten: Settings → Pages → Branch `main`, Ordner `/docs`.
Veröffentlicht wird nur der gefilterte Schnappschuss (`scripts/export_public.sh --push`, frische Historie). Kein Post im Namen des Menschen; Reichweite nur über die pseudonyme Seite.
- Kosten: 0 €. Risiko: gering. Rückgängig machen jederzeit möglich (Repo/Org löschen). Kein Impressum nötig, solange die Seite rein privat und nicht kommerziell ist; ab Stufe 2 ist ein Impressum Pflicht.

