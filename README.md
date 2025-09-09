
# Generator Prototypów z AI

Projekt rekrutacyjny — aplikacja do generowania klas Python na podstawie danych wejściowych, z opcjonalnym wsparciem AI (Gemini via OpenRouter).

## Funkcje
- Interfejs Streamlit do wpisania nazwy i atrybutów
- Generowanie kodu lokalnie lub przez AI
- Fallback, jeśli AI nie odpowiada
- Obsługa CLI z argparse
- Parsowanie konfiguracji z YAML (opcjonalnie)

## Uruchomienie
```bash
pip install -r requirements.txt
streamlit run genprototypów.py
