# Task CLI Tool

Jednoduchý Python projekt pro správu úkolů v příkazové řádce.

## Funkce
- Přidání úkolu (název, popis, priorita)
- Výpis úkolů
- Označení úkolu jako dokončeného
- Smazání úkolu
- Ukládání do JSON souboru

## Instalace
pip install -r requirements.txt


## Použití
python main.py add "Nakoupit" -d "Mléko a pečivo" -p high

python main.py list

python main.py done 1

python main.py delete 1

