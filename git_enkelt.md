# Git-guide — Gör exakt detta, inget annat

---

## Första gången — Kopiera projektet till din dator

Kör dessa tre rader i terminalen:

```
git clone https://github.com/infoalfredobarretta-dotcom/2026-mvp-f-r-data-filtrering.git
cd 2026-mvp-f-r-data-filtrering
code .
```

Byt sedan till din branch. Kör bara den rad som gäller dig:

```
git checkout melek/data-pipeline
```
```
git checkout alfredo/scoring-engine
```
```
git checkout filip/frontend
```

---

## Varje dag innan du börjar — Gör alltid detta först

```
cd 2026-mvp-f-r-data-filtrering
git pull
```

---

## När du är klar för dagen — Skicka upp din kod

Kör dessa tre rader i ordning:

```
git add .
git commit -m "vad du gjort idag"
git push
```

---

## Tre regler

1. Jobba alltid på din egen branch, aldrig main
2. Kör alltid `git pull` innan du börjar
3. Kör alltid `git add .` + `git commit` + `git push` när du är klar

---

## Osäker på var du är?

```
git branch
git status
```

Det första visar vilken branch du är på. Det andra visar vad som inte är uppskickat.
