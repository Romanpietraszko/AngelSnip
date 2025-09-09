
import streamlit as st
import yaml
from ai import podpowiedz_snippet
# === Generator klasy ===
def generuj_klase(nazwa, atrybuty):
    linie = [f"class {nazwa}:"]
    linie.append("    def __init__(self, " + ", ".join(atrybuty) + "):")
    for a in atrybuty:
        linie.append(f"        self.{a} = {a}")
    return "\n".join(linie)

# === UI (Streamlit) ===
st.title("Generator Prototypów z AI")

nazwa_ui = st.text_input("Nazwa aplikacji")
komponenty_ui = st.text_input("Atrybuty (oddzielone przecinkami)")

if st.button("Generuj z AI"):
    if nazwa_ui and komponenty_ui:
        prompt = f"Stwórz klasę Python o nazwie {nazwa_ui} z atrybutami: {komponenty_ui}"
        try:
            kod = podpowiedz_snippet(prompt)
            st.subheader("Kod wygenerowany przez AI:")
            st.code(kod, language="python")
        except Exception as e:
            st.error("Nie udało się połączyć z AI. Pokazuję lokalny snippet.")
            st.code(generuj_klase(nazwa_ui, komponenty_ui.split(",")), language="python")
    else:
        st.warning("Podaj nazwę aplikacji i atrybuty.")

# === Parsowanie YAML ===
def wczytaj_konfiguracje(plik):
    with open(plik) as f:
        return yaml.safe_load(f)
