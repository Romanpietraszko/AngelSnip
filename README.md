# Generator Prototypów z AI
Zobacz landing page - (https://possible-guests-785259.framer.app/)
Aplikacja stworzona jako projekt rekrutacyjny — służy do szybkiego generowania klas Python na podstawie danych wejściowych. , użytkownik może wygenerować kod bez pisania boilerplate. Idealne narzędzie dla junior developerów, PM-ów i startupowców.


## Funkcje
- Interfejs Streamlit do wpisania nazwy i atrybutów
- Fallback,
- Obsługa CLI z argparse
- Parsowanie konfiguracji z YAML (opcjonalnie)
👉 Demo online: [Kliknij tutaj, aby uruchomić aplikację](https://generatorprotypuw-awqezszjrxhyspezyqde4y.streamlit.app/)
## 🔄 Ścieżka użytkownika

1. Użytkownik wpisuje nazwę aplikacji i atrybuty
2. Kliknięcie „Generuj snippet”
5. Kod wyświetlany w UI ( fallback lokalny)


## 🚀 Następne kroki

- Dodanie opcji zapisu wygenerowanego kodu do pliku `.py`
- Integracja z GitHub (np. push wygenerowanego kodu)
- Generowanie testów jednostkowych na podstawie klasy
- Tryb demo bez potrzeby podawania klucza
- Landing page z CTA i linkiem do aplikacji
- - Dodanie fallbacku lokalnego — generowanie klasy bez AI na podstawie danych wejściowych

## ⚙️ Technologie i uzasadnienie

- **Python + Streamlit** — szybkie prototypowanie z prostym UI
- **YAML** — opcjonalna konfiguracja bez potrzeby edytowania kodu
## 🖼️ Interfejs użytkownika

Aplikacja zawiera prosty formularz:
- Pole „Nazwa aplikacji”
- Pole „Atrybuty (oddzielone przecinkami)”
- Przycisk „Generuj snippet”

Po kliknięciu, kod klasy zostaje wygenerowany i wyświetlony w oknie.
![Zrzut ekranu aplikacji](apkascreen.png)
## 📊 Walidacja i potencjał

Projekt może być szczególnie przydatny dla osób uczących się programowania lub budujących szybkie prototypy.  
Potencjalne sposoby walidacji:

- Przeprowadzenie testów z junior developerami — porównanie czasu pisania klasy ręcznie vs. z AI
- Udostępnienie demo na grupach programistycznych i zebranie feedbacku
- Analiza użycia w kontekście MVP dla startupów

W przyszłości aplikacja może zostać rozszerzona o:
- Generowanie testów jednostkowych
- Obsługę innych języków programowania
- Integrację z repozytorium GitHub
- połączenie z lokalnymi snippetami


## Uruchomienie
```bash
pip install -r requirements.txt
streamlit run genprototypów.py
