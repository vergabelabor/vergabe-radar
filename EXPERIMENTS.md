# EXPERIMENTS

## E0 · Laufzeit-Bootstrap
- HYPOTHESE: Ein 0-€-Setup (GitHub Actions + Issues + Prepaid-API) reicht für autonomen Betrieb.
- TEST: Workflow-Lauf ohne Key (Plumbing), danach mit Key (echter Agentenlauf), Kosten/Lauf messen.
- KOSTEN: 0 € Hosting; erster Agentenlauf ≤ 0,40 $.
- ERWARTUNG: Lauf < 10 min, < 0,40 $, Zustand wird committet, Issue-Kommunikation funktioniert.
- ERFOLGSKRITERIUM: 3 aufeinanderfolgende erfolgreiche Läufe mit gemessenen Kosten.
- ABBRUCHKRITERIUM: Kosten/Lauf > 1 $ oder Läufe nicht stabil → Architektur überdenken.
- ERGEBNIS: Plumbing ohne Key: ERFOLGREICH (Run 36672646295, alle Schritte grün, 12 s, 0 $) · mit Key: 2 Läufe erfolgreich (0,071 $ / 0,059 $, je < 1 min); 3. Lauf (Zeitplan) steht aus
- INTERPRETATION / ENTSCHEIDUNG: Infrastruktur trägt; ACTION 1/5 angefordert (Issue #1).

## E1 · Desk-Research Nachfrage H1/H2
- HYPOTHESE: H1 und H2 haben genug Nachfrage/Lücke für zahlende Kunden.
- TEST: 2 Websuchen (BFSG-Kleinshops, E-Rechnung-Tools/Preise).
- KOSTEN: ~0,08 $ · ERWARTUNG: beide plausibel · ERFOLGSKRITERIUM: Pflicht trifft Zielgruppe + keine kostenlose Sättigung
- ABBRUCHKRITERIUM: Zielgruppe ausgenommen oder Markt gesättigt
- ERGEBNIS: H1: Kleinstunternehmen ausgenommen, kostenlose Beratung vorhanden. H2: Pflicht erst 2028, kostenlose Tools überall.
- INTERPRETATION: Annahme „kleine Shops sind pflichtig“ war falsch (ich hatte die Ausnahme zwar notiert, aber unterschätzt). H2 gesättigt.
- ENTSCHEIDUNG: H2 verworfen, H1 herabgestuft. Nächster Test: H3 (Marktplatz-Nachfrage/Preise) und H4 (Nische mit Zahlungsbereitschaft) per Desk-Research.

## E2 · Desk-Research H3/H4 (2026-09-30)
- HYPOTHESE: H4 (Fördermittel-Liste als Abo) hat Zahlungsbereitschaft; H3 hat Nachfrage.
- TEST: 1 Websuche zu bezahlten Fördermittel-Listen/Abos.
- KOSTEN: ~0,05 $ API.
- ERWARTUNG: einige bezahlte Nischenangebote sichtbar.
- ERFOLGSKRITERIUM: konkretes bezahltes Angebot/Preis gefunden, Lücke erkennbar.
- ABBRUCHKRITERIUM: nur kostenlose amtliche Quellen.
- ERGEBNIS: Nur kostenlose/amtliche Quellen (foerderdatenbank.de, >3.500 Programme, Länder-/IHK-Übersichten, Blogs). Kein bezahltes Abo-Angebot gefunden. Marktplatz-Preise für H3 nicht geprüft (Suchtool liefert keine Plattformdaten).
- INTERPRETATION: Breite Fördermittelliste = gesättigt/kostenlos → H4 in dieser Form verworfen. Nische müsste eng und aktuell sein (z. B. eine Branche/Region), Zahlungsbereitschaft unbelegt.
- ENTSCHEIDUNG: H4 herabgestuft. H3 bleibt Kandidat, aber Test erfordert echten Kontakt/Angebot. Nächster Test: kostenloses Muster-Recherche-Angebot als öffentliche Landingpage (GitHub Pages) erstellen, um Interesse zu messen; Zahlungsannahme erst bei Interesse (Human Action).
- SELBSTKORREKTUR: Annahme "Desk-Research zeigt Zahlungsbereitschaft" ist schwach; Nachfrage lässt sich nur über reale Angebote testen.

## E3 · Muster-Angebot H3 (2026-09-30)
- HYPOTHESE: Solo-Selbstständige zahlen ~39 € für einen 48-h-Wettbewerbs-Check.
- TEST: Angebot als docs/angebot.md erstellt (KI offengelegt). Interesse-Messung erst nach Veröffentlichung + Kanal.
- KOSTEN: ~0,04 $ · ERWARTUNG: Artefakt nutzbar für Marktplatz/Seite
- ERFOLGSKRITERIUM (Gesamttest): ≥1 echte Anfrage/Zahlung in 14 Tagen · ABBRUCHKRITERIUM: 0 Anfragen nach 20 Kontakten/Listings
- ERGEBNIS: Artefakt fertig; noch keine Reichweite. Blocker: es gibt keinen zulässigen Kanal ohne Human Action (Account/Pages/Marktplatz, kein Spam).
- INTERPRETATION: Zahlungsbereitschaft weiter unbelegt (Stufe 0).
- ENTSCHEIDUNG: Eine gebündelte Human Action (Marktplatz-Account/Zahlungsempfang) vorbereiten, aber erst mit konkreten Plattformdaten; nächster Lauf: Plattformoptionen/Gebühren prüfen (1 Suche).

## E4 · Neustart-Ideenfindung H5–H14 (2026-09-30, Lauf 11)
- HYPOTHESE: Es gibt Ideen mit eigenem Distributionsweg und nicht-austauschbarem Vorteil, die ohne Gewerbe testbar sind.
- TEST: Desk-Bewertung von 10 Ideen (HYPOTHESES.md). KOSTEN: ~0,05 $. ERWARTUNG: 2 testbare Kandidaten.
- ERFOLGSKRITERIUM: Top 2 mit realem Test ohne Kosten. ABBRUCHKRITERIUM: –
- ERGEBNIS: H5 (Story/Publikum) und H6 (Vergabe-Digest) gewählt.
- INTERPRETATION: Reichweite ist der Engpass; Geld erst nach Publikum. Desk-Bewertung bleibt Schätzung (Stufe 0).
- ENTSCHEIDUNG: E5 starten: Landingpage/Story-Seite in docs/ (kostenlos, lokal erstellbar). Veröffentlichung (Pages aktivieren + 1 Post) = gebündelte Human Action, sobald Seite fertig und H6-Muster-Feed vorliegt.

## E5 · H5+H6 Veröffentlichungspaket (geplant)
- HYPOTHESE: Fremde reagieren auf die öffentliche Story und abonnieren einen kostenlosen Digest.
- TEST: docs/index.md (Story + Digest-Muster aus TED-API, KI offengelegt), 1 Post/Repo-Sichtbarkeit durch Mensch.
- KOSTEN: ~0,1 $ API, 0 € · ERFOLGSKRITERIUM: ≥20 Reaktionen oder ≥5 Opt-ins in 14 Tagen · ABBRUCH: 0 nach 14 Tagen
- ERGEBNIS (Lauf 12): TED-API v3 ohne Key erreichbar; scripts/digest.py + docs/index.md gebaut (~0,05 $). Noch nicht veröffentlicht (Pages/Post = Human Action, Berlin-Zeit 20:00 -> Anfrage morgen).
- INTERPRETATION: Artefakt technisch machbar, Nachfrage weiter Stufe 0. Digest zeigt teils abgelaufene Fristen -> Filter nötig.
- ENTSCHEIDUNG (Lauf 12): Veröffentlichung erst nach vertiefter Prüfung (Denkbudget, Lauf 13).

## E6 · Tiefenprüfung H6 Vergabe-Daten: Wettbewerb, Datenquelle, Prototyp (2026-09-30, Lauf 13)
- HYPOTHESE: Ein Vergabe-Digest ist (a) datentechnisch autonom und zu 0 $ lieferbar und (b) gegenüber dem Markt differenzierbar.
- TEST: 2 Websuchen + 1 Abruf (Wettbewerb/Preise, Datenquelle), Download von 7 Tagesexporten oeffentlichevergabe.de, Prototyp scripts/vergabe.py.
- KOSTEN: ~0,35 $ API · ERWARTUNG: Daten ok, Markt teils besetzt
- ERFOLGSKRITERIUM: Datenquelle frei/legal + Lieferung ohne Modellkosten + erkennbare Lücke · ABBRUCH: Daten kostenpflichtig oder Markt vollständig kostenlos bedient
- ERGEBNIS:
  - Datenquelle: Bekanntmachungsservice oeffentlichevergabe.de, Tagesexport OCDS/eForms ohne Key, Lizenz CC0. ~800 Meldungen pro Werktag (7 Tage: 5.515), auch nationale Vergaben unterhalb der EU-Schwelle („Public announcement“ ~30 %), Ausschreibungen ~58 %, Zuschläge ~38 %. Bei Zuschlägen nennen ~65 % den Gewinner, ~15 % den Wert. Die Frist fehlt im OCDS-Export (steht in eForms/Unterlagen).
  - Prototyp: scripts/vergabe.py (Nischenfilter nach CPV, offene Ausschreibungen + Zuschläge mit Gewinnern, Link zu Unterlagen). Muster IT/Software (CPV 72+48): 173 Einträge in 7 Tagen → docs/muster-it-vergabe.md. Lieferkosten 0 $ (kein Modell), läuft in GitHub Actions.
  - Wettbewerb: Vergabe24 18–86 €/Monat (Bundesland-Tarif ab ~20 €), DTAD individuell (~200 €/Monat geschätzt), zahlreiche KI-Start-ups (patterno, bidfix, usetendit, aufträge.io), dazu kostenlose Keyless-APIs (infranode.dev) auf derselben CC0-Quelle.
- INTERPRETATION: Zahlungsbereitschaft für Vergabe-Infos ist im Markt belegt (18–200 €/Monat), aber nicht für UNS (Stufe bleibt 0). Ein generischer Digest ist nicht differenziert: dieselben Daten gibt es gratis, und KI-Matching bieten mehrere Start-ups. Denkbare Lücke: **Zuschlags-/Wettbewerber-Intelligenz für eine enge Nische** (wer gewinnt bei wem, zu welchem Preis, wer ist neu im Markt), günstig (9–19 €/Monat). Die Daten sind im Export vorhanden, einfache Tools zeigen sie kaum. Distribution bleibt der Engpass: B2B-Nischenkäufer sind über HN/Reddit kaum erreichbar.
- NEUER BEFUND: Das Repo ist PRIVAT. H5 (öffentliche Story) ist damit bisher unsichtbar, und GitHub Pages ist im Free-Plan nur für öffentliche Repos kostenlos. Das Repo öffentlich zu machen wäre eine Veröffentlichung im Namen des Menschen, also eine Human Action.
- ENTSCHEIDUNG: H6 präzisiert zu H6b „Zuschlags-Intelligenz Nische“ (Stufe 0, KANDIDAT). Nächster Lauf: Nischenwahl nach Erreichbarkeit der Käufer + Suche nach günstigen Wettbewerbern für Zuschlagsdaten; danach Endempfehlung mit gebündelter Setup-Spezifikation (Repo öffentlich/Pages, Gewerbe, Zahlungsdienst/MoR, Opt-in-Mail).
- SELBSTKORREKTUR: Die Annahme „TED-Digest ist differenziert“ (E4) war zu optimistisch. Richtig war die Annahme „offene Daten ermöglichen 0-$-Lieferung“. Übersehen hatte ich die Sichtbarkeit des Repos: Das hätte vor der H5-Wahl geprüft werden müssen.

## E6b · Nischenwahl H6b nach Datenlage (2026-09-30, Lauf 19)
- HYPOTHESE: Es gibt eine Nische mit genug Volumen, hoher Gewinner-Transparenz und einer Käufergruppe, die DTAD nicht bezahlt.
- TEST: Auswertung von 14 Tagesexporten (10.929 Meldungen) je CPV-2: Ausschreibungen, Zuschläge, Anteil mit Gewinner bzw. Wert. KOSTEN: ~0,5 $ (Lauf inkl. Doku).
- ERWARTUNG: Bau (45) ist am größten, aber gesättigt. ERFOLGSKRITERIUM: Nische mit ≥20 Zuschlägen/Woche und ≥70 % Gewinner-Angabe. ABBRUCH: keine.
- ERGEBNIS: CPV 71 (Architektur/Ingenieur): 632 Ausschreibungen, 375 Zuschläge, 80 % mit Gewinner, 14 % mit Wert. CPV 45: 3.110/1.310, 56 % Gewinner. CPV 72: 161/98, 70 %. Die Werte sind überall selten (≤15 %). Unter den Gewinnern sind auch natürliche Personen → Datenschutzfilter eingebaut. Report docs/muster-planung-71.md.
- INTERPRETATION: Gewinner-Intelligenz ist machbar, Preis-Intelligenz nicht. Die Nische CPV 71 ist gewählt. Die Zahlungsbereitschaft bleibt Stufe 0.
- ENTSCHEIDUNG: Endempfehlung docs/ENDEMPFEHLUNG.md, ACTION 3/5 (Repo öffentlich + Pages) als Entwurf.
- SELBSTKORREKTUR: Die Annahme „Zuschlagswerte = Preis-Intelligenz“ (E6) ist widerlegt, weil nur ~14 % der Zuschläge einen Wert nennen. Neu erkannt: DSGVO-Risiko durch Personennamen in offenen Daten.

## E7 · Öffentlicher Vergabe-Radar CPV 71 (Seite live seit 2026-10-30; Zählung der 28 Tage startet mit Erledigung ACTION 4/5, da vorher kein Kanal)
- HYPOTHESE: Planer reagieren auf einen kostenlosen Gewinner-/Ausschreibungsreport.
- TEST: Repo öffentlich + Pages, Report bei jedem Agentenlauf (≥1×/Woche) neu erzeugen, optional 1 Post durch den Menschen.
- KOSTEN: 0 € (Pages), ~0,05 $/Aktualisierungslauf · ERWARTUNG: 0–10 Rückmeldungen
- ERFOLGSKRITERIUM: ≥5 qualifizierte Rückmeldungen/Opt-ins in 28 Tagen → Stufe 2 (ACTION 4/5: Gewerbe + MoR + Newsletter). ABBRUCH: 0 in 28 Tagen → H6b herabstufen.
- ERGEBNIS/INTERPRETATION/ENTSCHEIDUNG: offen
