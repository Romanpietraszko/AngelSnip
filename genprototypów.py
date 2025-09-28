import streamlit as st
import yaml
import json

# === Generator klasy ===
def generuj_klase(nazwa, atrybuty):
    linie = [f"class {nazwa}:"]
    linie.append("    def __init__(self, " + ", ".join(atrybuty) + "):")
    for a in atrybuty:
        linie.append(f"        self.{a} = {a}")
    return "\n".join(linie)

# === Ładowanie snippetów z jednego pliku ===
def znajdz_snippet_w_pliku(plik, prefix):
    try:
        with open(plik, encoding="utf-8") as f:
            snippety = json.load(f)
            for dane in snippety.values():
                if dane.get("prefix") == prefix:
                    return dane
    except Exception as e:
        st.error(f"Błąd w pliku '{plik}': {e}")
    return None

# === Lista dostępnych prefixów z jednego pliku ===
def wypisz_prefixy_z_pliku(plik):
    prefixy = []
    try:
        with open(plik, encoding="utf-8") as f:
            snippety = json.load(f)
            for dane in snippety.values():
                if "prefix" in dane:
                    prefixy.append(dane["prefix"])
    except Exception as e:
        st.error(f"Nie można wczytać prefixów: {e}")
    return sorted(set(prefixy))

# === UI (Streamlit) ===
st.title("🧠 Generator Prototypów z Lokalnymi Snippetami")

plik_snippetu = "python.code-snippets"

prefixy = wypisz_prefixy_z_pliku(plik_snippetu)
wybrany_prefix = st.selectbox("🔍 Wybierz prefix snippetu", prefixy)

if st.button("🔄 Załaduj snippet"):
    snippet = znajdz_snippet_w_pliku(plik_snippetu, wybrany_prefix)
    if snippet:
        st.subheader(f"✅ Snippet: {wybrany_prefix}")
        st.code("\n".join(snippet["body"]), language="python")
    else:
        st.warning("❌ Nie znaleziono snippetu o takim prefixie.")

# === Parsowanie YAML (jeśli potrzebne) ===
def wczytaj_konfiguracje(plik):
    with open(plik, encoding="utf-8") as f:
        return yaml.safe_load(f)
