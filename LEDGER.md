# LEDGER – Finanzielle Wahrheit

Regeln: Nur bestätigte Zahlungsflüsse. Einträge werden nie geändert oder gelöscht, nur durch Korrekturbuchungen ergänzt.
Kapital = Startkapital + bestätigte Einnahmen − tatsächlich bezahlte Ausgaben. Niemals < 0.

| # | Datum | Art | Beschreibung | Betrag € | Beleg | Kapital danach € |
|---|---|---|---|---|---|---|
| 0 | 2026-09-30 | START | Startkapital | +59,00 | Startinstruktion | 59,00 |

## Hinweis zu Prepaid-Guthaben
Kauf von API-Guthaben = tatsächliche Ausgabe (nicht erstattbar) und wird bei Kauf voll gebucht.
Der Verbrauch des Guthabens wird in COSTS.md bzw. logs/runs.csv verfolgt (Restguthaben = gekauft − verbraucht).

## Buchungen
| # | Datum | Art | Beschreibung | Betrag € | Beleg | Kapital danach € |
|---|---|---|---|---|---|---|
| 1 | 2026-09-30 | AUSGABE | API-Guthaben gekauft (ACTION 1/5), Betrag laut Owner-Kommentar Issue #1 „20 Euro“; USD-Gegenwert unbestätigt | −20,00 | Issue #1 Kommentar | 39,00 |
| 2 | 2026-09-30 | KORREKTUR | Korrektur zu #1 (Owner-Kommentar Issue #1): 20 $ Guthaben, bezahlt 23,80 $ (inkl. Steuer). Konservativ als 23,80 € angesetzt (Obergrenze, da 1 $ < 1 €); bei Vorliegen des Kurses/Belegs per weiterer Buchung feinjustieren | −3,80 | Issue #1 Kommentar | 35,20 |
