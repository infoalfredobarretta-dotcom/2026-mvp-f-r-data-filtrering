
# Data filtrering - MVP
**Period:** 2026-03-29 till 2026-04-14

---

## Vår vision 

Stock pickers ska aldrig behöva drunkna i information för att fatta ett välgrundat beslut.

**Kom ihåg:** Om något inte stödjer visionen så gör vi det inte 






## Vad vi bygger och varför

Vi bygger ett verktyg för retail stock pickers som är trötta på att drunkna i information.

Problemet är inte att det finns för lite information om aktier. Problemet är att det finns för mycket. Nyheter, analyser, Reddit-trådar, chart-mönster, motstridiga åsikter — allt pockar på uppmärksamhet samtidigt. Resultatet är att folk antingen fattar beslut på fel grund eller skjuter upp dem helt.

Vår lösning är enkel. En enda sida där du söker på en aktie och direkt får svar på fyra frågor: vad är viktigt nu, vad driver aktien, vad gäller kortsiktigt respektive långsiktigt, och vad är slutsatsen. Inget mer, inget mindre.

Det som gör produkten trovärdig är vad vi väljer att inte visa. Vi visar inte chart-mönster, tekniska indikatorer, sociala medier eller analytikerspekulationer. Vi visar bara det som faktiskt påverkar bolagets värde — kvartalsrapporter, ledningsbyten, förvärv, regulatoriska beslut och andra officiella bolagshändelser. Allt länkat till originalkällan så användaren alltid kan verifiera vad de ser.

Skillnaden mot andra verktyg är inte att vi har AI. Det är att vi begränsar vad användaren ser och presenterar det i en fast, tydlig struktur varje gång. Ingen terminal. Inget nyhetsflöde. Inget brus.

Målet är att en retail stock picker ska förstå en aktie bättre på 60 sekunder med vår produkt än på 30 minuter på egen hand.

---

## Mål

När en retail stock picker söker på en aktie ska systemet inom 60 sekunder leverera en tydlig och källhänvisad bild av vad som faktiskt påverkar bolaget just nu, baserat enbart på seriösa och verifierbara källor.

---

## Ansvar

| Person | Ansvar |
|--------|--------|
| Melker | Backend - hela systemet från datainsamling till output |
| Filip | Frontend - aktievyn som användaren ser |

I slutet ska båda delar fungera sömlöst tillsammans.

---

## Nyckelord

- Extrem enkelhet och tydlighet
- Trovärdighet

---

## Leverans

Fullständig MVP som fungerar på tre utvalda aktier:

- Investor B (INVE-B)
- Nvidia (NVDA)
- Novo Nordisk B (NOVO-B)
  
**CIO**-Levererar ett fullständigt dokument på hur systemet funkar från rådata till output 



## Det som aldrig visas

- Sociala medier
- Analytikerspekulationer
- Chart-mönster och tekniska indikatorer
- Rykten och obekräftad information
- Makrohändelser utan direkt bolagskoppling
