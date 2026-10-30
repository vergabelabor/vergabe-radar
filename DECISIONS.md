# DECISIONS

## D1 · 2026-09-30 · Laufzeit: GitHub Actions statt VPS
Evidenz: privates Repo hat 2.000 freie Linux-Minuten/Monat; ohne Zahlungsmittel bei GitHub entstehen bei Überschreitung keine Kosten. Hetzner CX23 kostet seit 06/2026 ~5,49 €/Monat.
Entscheidung: Actions (cron + issue_comment + manuell), Zustand im Git. VPS erst, wenn ein Experiment einen dauerhaften Dienst nachweislich braucht.

## D2 · 2026-09-30 · Kommunikation: GitHub Issues
Bereits vorhanden, kostenlos, E-Mail-Push an den Menschen, Antwort per Kommentar startet den Agenten. Kein Telegram/Bot nötig.

## D3 · 2026-09-30 · Modell: Claude Sonnet 5.5, Fallback Haiku 4.5, Prepaid
Prepaid verhindert Überziehung technisch. Limit pro Lauf 0,40 $ (anpassbar in config/budget.json). Tägliche Kadenz 1 Lauf + ereignisgesteuerte Läufe.

## D4 · 2026-09-30 · Guthabenhöhe 10 $
Kleinster sinnvoller Betrag (~10–12 € inkl. MwSt.) für ~25–40 Läufe. Hält ≥ 45 € Kapital für Experimente frei. Nachkauf nur mit Evidenz.

## D5 · 2026-09-30 · Rechtlicher Rahmen Akquise
Keine unaufgeforderte Werbe-E-Mail (§ 7 UWG). Akquise nur über öffentliche Inhalte, Marktplätze, Foren im Rahmen ihrer Regeln, Opt-in. KI-Einsatz wird gegenüber Kunden offen gelegt.

## D6 · 2026-09-30 · Guthaben 20 € statt 10 $
Owner kaufte 20 € (mehr als angefragt). Voll als Ausgabe gebucht (Kapital 39 €, YELLOW). USD-Gegenwert unbestätigt → api_credit_purchased_usd bleibt konservativ 10, bis Betrag bekannt. Kein Nachkauf nötig; Experimentbudget ≤ 39 € minus Laufkosten.

## D7 · 2026-09-30 · Budgetübergang abgeschlossen
D6 überholt durch Ledger #2: 20 $ Guthaben, config/budget.json = 20 $. Ab jetzt laufen alle Modellkosten aus dem Experimentbudget; Bootstrap über Pro-Abo beendet. Erste echte Läufe: 0,071 $ und 0,059 $.

## D8 · 2026-09-30 · Dauerbetrieb statt Tageslauf (Korrektur zu D3)
Rückmeldung des Menschen: Tageslauf entsprach nicht der Absicht (autonomer Dauer-Loop). Neu: Selbstverkettung der Läufe über agent/next.json (continue/sleep/wait_human), Watchdog alle 2 h ohne Modellkosten, Tageslimit 1,00 $ (config/budget.json). Laufzeit weiterhin 0 € Hosting.

## 2026-09-30 – ACTION 2 abgelehnt (Gewerbe fehlt)
Entscheidung: Kein Plattformverkauf (H3) ohne Gewerbeanmeldung; nicht erneut drängen. Gewerbeanmeldung (ca. 20–60 €, Human Action) erst anfragen, wenn kostenlos belegte Nachfrage besteht. Verbleibend 3 Actions bündeln. Bis dahin: Lauf pausieren (kein Token-Verbrauch ohne Zweck).

## 2026-09-30 (Lauf 10) – Rechtsweg ohne Gewerbe geprüft
- Analyse (ohne Recherchekosten): In DE gibt es keine Bagatellgrenze für „Gewerbe“; wiederholte Verkäufe mit Gewinnabsicht gelten als Gewerbe. Kleinunternehmerregelung ist nur steuerlich. Freiberuflichkeit (Texte/Beratung) bräuchte Finanzamt-Anmeldung durch den Menschen.
- Unentgeltliche Muster/Leistungen sind legal, liefern aber keine Zahlungsbereitschaft; Spenden/„Zahl was du willst“ gelten nicht als validierter Umsatz.
- Entscheidung: Kein legaler bezahlter Weg ohne menschliche Registrierung. Keine Action jetzt (2/5 bleiben Reserve). Kapital erhalten; Lauf pausiert bis Mensch Richtung ändert. Bündel-Action (Anmeldung + Kanal) erst bei belegter Nachfrage aus kostenlosem Muster.

## 2026-09-30 – Vorgabe des Menschen: Neustart der Ideenfindung
Der Mensch erwartet neue Ideen statt Pause. Befund aus der Bootstrap-Analyse: Nicht das Kapital ist der Engpass, sondern
(1) Reichweite/Distribution (kein Publikum, kein Ruf, keine Kaltakquise), (2) Austauschbarkeit (generische KI-Inhalte kann der Kunde selbst erzeugen),
(3) fehlende rechtliche Identität. Ein Registrierungs-Paket (Gewerbe + Merchant-of-Record-Shop + Postfach + öffentliche Seite) ist für den Menschen denkbar,
wenn eine Hypothese es mit Evidenz rechtfertigt – das ist KEIN Blocker mehr für die Ideenfindung, sondern eine spätere, gebündelte Action.
Auftrag: mindestens 10 neue Hypothesen, die gezielt (1) und (2) lösen (eigener Distributionsweg, nicht austauschbarer Vorteil, z. B. Daten/Automatisierung,
die ein Kunde nicht einfach selbst per Chat erzeugt). Bewerten nach: Zugang zu Käufern, Differenzierung, legaler Weg, Zeit bis zum ersten Signal, Kosten.
Top 2 mit dem billigsten realen Test (Signal von echten Menschen, nicht Desk-Research) in EXPERIMENTS.md planen und starten, soweit ohne Human Action möglich.
Gründlich arbeiten (mehrere Läufe sind ok, Tageslimit beachten). Keine Pause, solange es offene sinnvolle Schritte gibt.

## 2026-09-30 abends – Vorgabe des Menschen: Denkbudget 5 € (ca. 5,80 $), keine Einschränkung
- Der Mensch gibt 5 € extra zum Überlegen. Für die Ideenfindung gilt die Token-Sparregel nicht: gründlich, tief, kritisch arbeiten.
- config/budget.json vorübergehend: Modell claude-opus-5-5, bis 1,50 $/Lauf, Tageslimit 6,80 $ (1 $ regulär + 5,80 $ Denkbudget). Nach Abschluss der Ideenfindung selbst zurückstellen (Sonnet, 1 $/Tag) und in DECISIONS dokumentieren.
- Buchhaltung: kein neuer Geldfluss; das Denkbudget wird aus dem vorhandenen API-Guthaben verbraucht. Reicht das Guthaben später nicht, weiß der Mensch, dass er 5 € zugesagt hat.
- Zielbild: Die Lösung muss danach AUTONOM laufen. Benötigte APIs/Accounts/Zugänge richtet der Mensch ein – der Agent spezifiziert sie konkret und vollständig (was, wozu, welche Rechte/Scopes, Kosten, Risiko) als EINE gebündelte Action. Das ist kein Hindernis mehr für die Ideenwahl.
- Schutz des Menschen bleibt Pflicht: legal, keine Täuschung, kein Spam, kein Abmahnrisiko (eigene Inhalte, korrekte Pflichtangaben), keine Verpflichtungen ohne Zustimmung.
- Auftrag: die Top-Ideen (und ggf. neue) gründlich prüfen – echte Daten/Wettbewerber, Prototyp wo sinnvoll, Monetarisierungspfad, realistische Umsatzerwartung, benötigte Zugänge – und dann die beste Lösung mit fertiger Setup-Spezifikation vorlegen.

## 2026-09-30 (Lauf 13) – H6 präzisiert, Quelle gewechselt
TED → oeffentlichevergabe.de (CC0, national + EU, Zuschläge mit Gewinnern). Generischer Digest verworfen (gesättigt), weiter nur als Nischen-Zuschlags-Intelligenz (H6b). Keine Human Action vor der Endempfehlung. Denkbudget-Modus bleibt bis zur Endempfehlung aktiv.

## 2026-09-30 (Lauf 19) – Endempfehlung, Denkbudget-Modus beendet
- Empfehlung: H6b „Vergabe-Radar Planungsleistungen (CPV 71)“ mit H5 (öffentliche Story) als Kanal. Stufenplan und Setup-Spezifikation in docs/ENDEMPFEHLUNG.md. Stufe 1 = ACTION 3/5 (Repo öffentlich + Pages, 0 €). Stufe 2 (Gewerbe + MoR + Newsletter = ACTION 4/5) nur bei Erfolg von E7.
- Anfrage erst am 2026-10-01 ab 08:00 Berlin (Regel 9). Jetzt ist es 20:06 Berlin.
- Datenschutz: Einzelbieter ohne Rechtsform werden in veröffentlichten Reports ausgeblendet.
- config/budget.json zurück auf Normalbetrieb: claude-sonnet-5-5, 0,50 $/Lauf, 1,00 $/Tag (Vorgabe des Menschen). Denkbudget verbraucht: ~2,0 $ von 5,80 $, Rest wird nicht beansprucht.

## 2026-10-30 – Vorgabe des Menschen: Anonymität, pseudonyme Veröffentlichung
- Der Mensch gibt nichts unter seinem Namen frei: kein öffentliches Schalten DIESES Repos (Kontoname und ein Commit in der Historie identifizieren ihn), kein Post im eigenen Profil. Die bisherige ACTION 3/5 (Entwurf) ist damit hinfällig.
- Neuer Weg: eine pseudonyme GitHub-Organisation mit einem öffentlichen Repo. Befüllt wird es nur über `scripts/export_public.sh --push`: Whitelist der Dateien, frische Historie mit einem Commit, Abbruch bei verbotenen Zeichenketten (config/public.json). Dieses Repo bleibt privat. Regel 15 im LOOP_PROMPT.
- Infrastruktur dafür ist vorbereitet (Export-Skript, config/public.json, config/public_README.md, Secret `PUBLIC_REPO_TOKEN` wird im Workflow durchgereicht). Testlauf ohne Push: 13 Dateien, Prüfung ok.
- Krypto-Wallet als Budget: vorerst nicht. Geld ist nicht der Engpass, ein privater Schlüssel im Agenten wäre ein Diebstahlrisiko, und Einnahmen bleiben ohne Gewerbe/Impressum unzulässig, egal in welcher Währung. Wieder prüfen, wenn eine konkrete Ausgabe nur per Krypto anonym möglich ist.
- AUFTRAG an den Agenten (nächster Lauf):
  1. Einen Namen für Organisation und Repo vorschlagen: neutral, ohne Bezug zum Menschen, passend zu „Vergabe-Radar Planungsleistungen“ + offenes KI-Experiment, kurz, merkbar. 3 Kandidaten, Verfügbarkeit per `gh api users/<name>` prüfen (404 = frei), Favorit begründen. In config/public.json `repo` als `<org>/<repo>` eintragen.
  2. docs/index.md und docs/ENDEMPFEHLUNG.md an den neuen Weg anpassen (kein „Repo öffentlich schalten“, kein Post im Namen des Menschen; Kanal nur über die pseudonyme Seite). Danach `scripts/export_public.sh` ohne Push laufen lassen, muss „Prüfung ok“ melden.
  3. ACTION 3/5 neu schreiben und als Issue anlegen (Regel 9 beachten). Inhalt, ca. 10 Min: (a) Organisation <org> anlegen (Free; Mitgliedschaft bleibt privat, kurz unter People prüfen), (b) leeres öffentliches Repo <org>/<repo> anlegen, (c) Fine-grained Token: Resource owner <org>, nur dieses Repo, Rechte Contents RW + Pages RW, Ablauf 1 Jahr → im privaten Repo als Actions-Secret `PUBLIC_REPO_TOKEN`, (d) nach dem ersten Push durch den Agenten: Settings → Pages → Branch `main`, Ordner `/docs`. Die anderen Kandidaten im Issue nennen, damit der Mensch ausweichen kann, falls der Favorit vergeben ist.
  4. Nach ERLEDIGT: `scripts/export_public.sh --push`, Pages-URL prüfen, E7 starten. Ab dann nach jedem relevanten Lauf exportieren.

## 2026-10-30 (Lauf 2) – Name gewählt
Favorit `vergabelabor/vergabe-radar` (Ausweich `zuschlagsradar`, `vergabewerk`; alle frei). config/public.json gesetzt, Docs angepasst, Export-Prüfung ok. ACTION 3/5 als Issue angelegt.

## 2026-10-30 – Vorgabe des Menschen: Distribution für E7 lösen
- Korrektur: Pages ist live (https://vergabelabor.github.io/vergabe-radar/, vom Menschen aktiviert). Die 403 der Pages-API ist kein Fehler der Seite.
- Befund: E7 hat keinen Kanal. Ohne Besucher endet E7 mit 0 Rückmeldungen, das wäre ein Messfehler, kein Marktsignal. Warten bis 27.11. ohne Kanal ist daher nicht zulässig.
- AUFTRAG an den Agenten (nächster Lauf, Denkbudget wie Normalbetrieb):
  1. Kanäle bewerten, über die Planungsbüros (Architektur/Ingenieure, CPV 71) die Seite ANONYM und LEGAL finden: (a) pseudonymes Konto für Fachforen/Reddit/Communities (welche konkret, deren Regeln zu Eigenwerbung), (b) SEO/Auffindbarkeit (Titel, Beschreibungen, sprechende Seiten je Bundesland/Leistung, Sitemap; kostenlos, sofort machbar), (c) Hinweis an öffentliche Stellen/Verbände/Kammern (nur über deren veröffentlichte Kanäle, kein Spam nach § 7 UWG), (d) weitere. Je Kanal: erwartete Besucher in 4 Wochen, Aufwand, Risiko, nötige Human Action.
  2. Alles, was ohne Human Action geht (v. a. SEO), sofort umsetzen und exportieren.
  3. Falls ein Kanal ein Konto braucht: EINE gebündelte ACTION 4/5 mit exakter Klickanleitung (Konto, Pseudonym, keine Verbindung zum Menschen, Zugangsdaten nur als Secret). Regel 9 beachten. Der Mensch postet nicht unter eigenem Namen.
  4. E7-Zeitraum ggf. ab Start des ersten echten Kanals neu zählen und in EXPERIMENTS.md dokumentieren.

## 2026-10-30 (Lauf 4) – Kanalplan Distribution E7
Bewertung (Besucher in 4 Wochen, Aufwand, Risiko):
- (b) SEO: 16 Bundesland-Seiten + Gesamtseite, Titel/Beschreibung, Sitemap, robots.txt (docs/_config.yml, scripts/seiten.sh) – JETZT umgesetzt und exportiert. Ohne Backlinks/Search Console realistisch 0–20 Besucher. Kein Risiko.
- (a) Pseudonymes Reddit/Foren (r/Architekten, Fachforen): 20–100 Besucher bei einem gut angenommenen Beitrag; Risiko: Eigenwerbungsregeln → als Frage formulieren, KI offenlegen. Braucht Konto = Human Action. Kein automatisiertes Posten (Bot-/Spam-Risiko).
- (c) Kammern/Verbände: nur über deren veröffentlichte Kontaktformulare, unaufgefordert an Organisationen = Werbung, § 7 UWG grenzwertig; zurückgestellt bis Rückmeldung aus (a).
- (d) Search Console/Bing: bringt Indexierung in Tagen statt Wochen; braucht Konto = Human Action.
Entscheidung: (a)+(d) gebündelt als ACTION 4/5. E7 wird ab Erledigung neu gezählt (28 Tage). Die Zahl bleibt vorsichtig: ich erwarte 0–5 Rückmeldungen, Stufe bleibt 0.
