# Generator Prototypów z AI

Aplikacja stworzona jako projekt rekrutacyjny — służy do szybkiego generowania klas Python na podstawie danych wejściowych. Dzięki wsparciu AI (Gemini via OpenRouter), użytkownik może wygenerować kod bez pisania boilerplate. Idealne narzędzie dla junior developerów, PM-ów i startupowców.


## Funkcje
- Interfejs Streamlit do wpisania nazwy i atrybutów
- Generowanie kodu lokalnie lub przez AI
- Fallback, jeśli AI nie odpowiada
- Obsługa CLI z argparse
- Parsowanie konfiguracji z YAML (opcjonalnie)
## 🔑 Konfiguracja API

Aby aplikacja działała z AI, potrzebujesz własnego klucza API z [OpenRouter](https://openrouter.ai).

1. Zarejestruj się i wygeneruj klucz
2. Utwórz plik `.env` na podstawie `.env.example`
3. Wklej swój klucz:
👉 Demo online: [Kliknij tutaj, aby uruchomić aplikację](https://generatorprotypuw-awqezszjrxhyspezyqde4y.streamlit.app/)

## ⚙️ Technologie i uzasadnienie

- **Python + Streamlit** — szybkie prototypowanie z prostym UI
- **OpenRouter (Gemini)** — dostęp do modeli AI bez konieczności własnego hostingu
- **Dotenv** — bezpieczne zarządzanie kluczem API
- **YAML** — opcjonalna konfiguracja bez potrzeby edytowania kodu
## 🖼️ Interfejs użytkownika

Aplikacja zawiera prosty formularz:
- Pole „Nazwa aplikacji”
- Pole „Atrybuty (oddzielone przecinkami)”
- Przycisk „Generuj z AI”

Po kliknięciu, kod klasy zostaje wygenerowany i wyświetlony w oknie.
![Zrzut ekranu aplikacji](apkascreen.png)

## Uruchomienie
```bash
pip install -r requirements.txt
streamlit run genprototypów.py
