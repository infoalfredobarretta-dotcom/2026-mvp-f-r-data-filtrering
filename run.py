# Kör hela systemet i rätt ordning
# 1. normalize.py  → Format 1
# 2. scoring.py    → Format 2
# 3. llm.py        → Format 3

from data_pipeline import normalize, llm
from scoring_engine import scoring

if __name__ == "__main__":
    normalize.run()
    scoring.run()
    llm.run()
