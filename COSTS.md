# COSTS

## Kostenmodell (Betriebskosten = Modell + Hosting + API + Domain + Tools + Sonstiges)

| Posten | Anbieter | Art | Kosten |
|---|---|---|---|
| Hosting/Scheduler | GitHub Actions (privat, 2.000 min/Monat frei) | fix | 0,00 € |
| Kommunikation | GitHub Issues + E-Mail-Benachrichtigung | fix | 0,00 € |
| Speicher/Gedächtnis | Git-Repo | fix | 0,00 € |
| Modell | Anthropic API, Prepaid | variabel | pro Lauf, Limit via `config/budget.json` |
| Domain/Tools | – | – | 0,00 € (keine) |

## Prepaid-API-Guthaben

| Gekauft (USD) | Gebucht (EUR, laut Beleg) | Verbraucht (USD, Summe logs/runs.csv) | Rest (USD) |
|---|---|---|---|
| 20,00 | 23,80 (konservativ, Ledger #1+#2) | ~2,0 (Stand Lauf 19, 30.09.) | ~18,0 |

## Verbrauch
Maschinenlesbar: `logs/runs.csv` (wird automatisch pro Lauf ergänzt). Umrechnung USD→EUR für Kennzahlen: Kurs aus dem Kaufbeleg des Guthabens.

Korrektur 2026-09-30: API-Guthaben = 20 $, bezahlt 23,80 $ (Ledger #2, konservativ 23,80 €).
