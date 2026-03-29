# vad vi bygger och varför
Vi bygger ett verktyg för retail stock pickers som är trötta på att drunkna i information.

Problemet är inte att det finns för lite information om aktier. Problemet är att det finns för mycket. Nyheter, analyser, Reddit-trådar, chart-mönster, motstridiga åsikter - allt pockar på uppmärksamhet samtidigt. Resultatet är att folk antingen fattar beslut på fel grund eller skjuter upp dem helt.

Vår lösning är enkel. En enda sida där du söker på en aktie och direkt får svar på fyra frågor - vad är viktigt nu, vad driver aktien, vad gäller kortsiktigt respektive långsiktigt, och vad är slutsatsen. Inget mer, inget mindre.

Det som gör produkten trovärdig är vad vi väljer att inte visa. Vi visar inte chart-mönster, tekniska indikatorer, sociala medier eller analytikerspekulationer. Vi visar bara det som faktiskt påverkar bolagets värde - kvartalsrapporter, ledningsbyten, förvärv, regulatoriska beslut och andra officiella bolagshändelser. Allt länkat till originalkällan så användaren alltid kan verifiera vad de ser.

Skillnaden mot andra verktyg är inte att vi har AI. Det är att vi begränsar vad användaren ser och presenterar det i en fast, tydlig struktur varje gång. Ingen terminal. Inget nyhetsflöde. Inget brus.

Målet är att en retail stock picker ska förstå en aktie bättre på 60 sekunder med vår produkt än på 30 minuter på egen hand.

Det är produkten. Det är vad vi bygger mot.


# Planering
Vecka 1 Planering och produktdefinition
Vecka  — Påbörja bygge och lära känna systemet
Alla tre sätter upp miljön, förstår sin del och skriver de första raderna kod. Inget behöver vara klart.
Vecka 3 — Bygge
Alla tre färdigställer sina delar.
Vecka 4 — Ihopsättning och test
Koppla ihop delarna, köra på en riktig aktie och testa.
Totalt: Klar vecka 4.

# Vad ska vi bygga - per person
 
**Projekt:** Stock Signal System
**Datum:** 2026-03-28
 
---
 
## Melker - Bygger två saker
 
### Del 1: Normaliseringsscript
Ett script som tar en råtext (artikel, pressmeddelande, rapport, filing) och omvandlar den till JSON enligt Format 1.
 
Du matar in texten manuellt i scriptet. Scriptet fyller i alla fält automatiskt: titel, källtyp, datum, bolag, brödtext och så vidare. Resultatet är en JSON-fil som Alfredo kan ta emot direkt.
 
**Input:** Råtext kopierad från en källa
**Output:** Format 1 JSON-fil
 
---
 
### Del 2: LLM-koppling
Ett script som tar emot Format 2 från Alfredo och skickar det till en språkmodell. Språkmodellen får tydliga instruktioner om vad den ska skriva: vad är viktigt nu, vad driver aktien, kort vs långsiktigt, slutsats.
 
Svaret från språkmodellen formateras till Format 3 och skickas vidare till Filip.
 
**Input:** Format 2 JSON från Alfredo
**Output:** Format 3 JSON till Filip
 
---
 
## Alfredo - Bygger scoring-logiken
 
Ett script som tar emot Format 1 från Melker och bedömer hur viktig varje signal är.
 
Scriptet räknar ut ett poäng för varje signal baserat på tre saker:
- Hur trovärdig är källan (primary, secondary, regulatory)
- Hur stor är affärspåverkan (high, medium, low)
- Hur ny är informationen (datum)
 
Signaler med tillräckligt högt poäng går vidare. De med lågt poäng filtreras bort. Resultatet returneras som Format 2 till Melek.
 
**Input:** Format 1 JSON från Melek
**Output:** Format 2 JSON till Melek
 
---
 
## Filip - Bygger frontend
 
En ensidig webbsida där användaren kan söka på ett bolagsnamn eller ticker, till exempel "Nvidia" eller "NVDA", och få Format 3 visat på ett tydligt sätt.
 
Sidan visar fyra sektioner i fast ordning:
1. Vad är viktigt nu
2. Vad driver aktien
3. Kort vs långsiktigt
4. Slutsats
 
Under varje sektion visas källan som en klickbar länk.
 
Du behöver inte vänta på Melek eller Alfredo. Börja med mock-data från `/shared/mock-data` och bygg sidan mot det formatet.
 
**Input:** Format 3 JSON från Melek
**Output:** Webbsida användaren ser
 
---
 
## Sammanfattning
 
| Person | Bygger | Input | Output |
|--------|--------|-------|--------|
| Melker | Normaliseringsscript | Råtext | Format 1 JSON |
| Melek | LLM-koppling | Format 2 JSON | Format 3 JSON |
| Alfredo | Scoring-logik | Format 1 JSON | Format 2 JSON |
| Filip | Frontend | Format 3 JSON | Webbsida |
 
---
 
## Ordningen det sätts ihop
 
```
1. Melek matar in råtext → Normaliseringsscript → Format 1
2. Format 1 → Alfredos scoring → Format 2
3. Format 2 → Melker LLM-koppling → Format 3
4. Format 3 → Filips frontend → Användaren ser svaret
```
