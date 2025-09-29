import streamlit as st
import yaml
import json

# === Generator klasy ===
def generuj_klase(nazwa, atrybuty):
    linie = [f"class {nazwa}:"]
    linie.append("    def __init__(self, " + ", ".join(atrybuty) + "):")
    for a in atryputy:
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
        st.error(f"❌ Błąd przy ładowaniu snippetu: {e}")
    return None

# === Lista dostępnych prefixów z jednego pliku ===
def wypisz_prefixy_z_pliku(plik):
    prefixy = []
    try:
        with open(plik, encoding="utf-8") as f:
            zawartosc = f.read()
            if not zawartosc.strip():
                st.error("❌ Plik snippetów jest pusty.")
                return []
            snippety = json.loads(zawartosc)
            for dane in snippety.values():
                if "prefix" in dane:
                    prefixy.append(dane["prefix"])
    except Exception as e:
        st.error(f"❌ Nie można wczytać prefixów: {e}")
    return sorted(set(prefixy))
# === Menu snippetów z kategoriami ===#
def menu_snippetów_z_kategoriami(plik):
    try:
        with open(plik, encoding="utf-8") as f:
            snippety = json.load(f)
    except Exception as e:
        st.error(f"❌ Nie udało się wczytać pliku: {e}")
        return

    if not isinstance(snippety, dict):
        st.error("❌ Format pliku jest nieprawidłowy — oczekiwano obiektu z kategoriami.")
        return

    kategorie = list(snippety.keys())
    wybrana_kategoria = st.selectbox("📂 Wybierz kategorię snippetów", kategorie)

    if wybrana_kategoria:
        snippety_kategorii = snippety.get(wybrana_kategoria, {})
        if not isinstance(snippety_kategorii, dict):
            st.warning("⚠️ Wybrana kategoria nie zawiera poprawnych snippetów.")
            return

        nazwy_snippetów = list(snippety_kategorii.keys())
        wybrany_snippet = st.selectbox("🧩 Wybierz snippet", nazwy_snippetów)

        if wybrany_snippet:
            snippet = snippety_kategorii[wybrany_snippet]
            st.markdown(f"### ✨ Snippet: `{snippet.get('prefix', wybrany_snippet)}`")
            st.markdown(f"**Opis:** {snippet.get('description', 'Brak opisu')}")
            st.code("\n".join(snippet.get("body", [])), language="python")


# === UI (Streamlit) ===
st.title("🧠 Generator Prototypów z Lokalnymi Snippetami")

plik_snippetu = "python.code-snippets"

# Debug: pokaż zawartość pliku
try:
    with open(plik_snippetu, encoding="utf-8") as f:
        zawartosc = f.read()
        st.text_area("📄 Zawartość pliku snippetów", zawartosc, height=200)
except Exception as e:
    st.error(f"❌ Nie można odczytać pliku: {e}")

# Lista prefixów
prefixy = wypisz_prefixy_z_pliku(plik_snippetu)

if prefixy:
    wybrany_prefix = st.selectbox("🔍 Wybierz prefix snippetu", prefixy)

    if st.button("🔄 Załaduj snippet"):
        snippet = znajdz_snippet_w_pliku(plik_snippetu, wybrany_prefix)
        if snippet:
            st.subheader(f"✅ Snippet: {wybrany_prefix}")
            st.code("\n".join(snippet["body"]), language="python")
        else:
            st.warning("❌ Nie znaleziono snippetu o takim prefixie.")
else:
    st.warning("⚠️ Brak dostępnych prefixów. Sprawdź poprawność pliku.")

# === Parsowanie YAML (jeśli potrzebne) ===
def wczytaj_konfiguracje(plik):
    try:
        with open(plik, encoding="utf-8") as f:
            return yaml.safe_load(f)
    except Exception as e:
        st.error(f"❌ Błąd przy ładowaniu YAML: {e}")
        return {}
