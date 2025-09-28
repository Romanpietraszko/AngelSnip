import streamlit as st
import yaml
import json
import os

# === Generator klasy ===
def generuj_klase(nazwa, atrybuty):
    linie = [f"class {nazwa}:"]
    linie.append("    def __init__(self, " + ", ".join(atrybuty) + "):")
    for a in atrybuty:
        linie.append(f"        self.{a} = {a}")
    return "\n".join(linie)

# === Ładowanie snippetów z folderu ===
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

# === Lista dostępnych prefixów ===
def wypisz_prefixy(folder):
    prefixy = []
    if not os.path.isdir(folder):
        return prefixy
    for plik in os.listdir(folder):
        if plik.endswith(".code-snippets"):
            sciezka = os.path.join(folder, plik)
            try:
                with open(sciezka, encoding="utf-8") as f:
                    snippety = json.load(f)
                    for dane in snippety.values():
                        if "prefix" in dane:
                            prefixy.append(dane["prefix"])
            except:
                continue
    return sorted(set(prefixy))

# === UI (Streamlit) ===
st.title("🧠 Generator Prototypów z Lokalnymi Snippetami")

# Stała ścieżka do folderu snippetów
folder_snippetow ="python.code-snippets"

# Lista prefixów
prefixy = wypisz_prefixy(folder_snippetow)
wybrany_prefix = st.selectbox("🔍 Wybierz prefix snippetu", prefixy)

if st.button("🔄 Załaduj snippet"):
    snippet = znajdz_snippet_w_folderze(folder_snippetow, wybrany_prefix)
    if snippet:
        st.subheader(f"✅ Snippet: {wybrany_prefix}")
        st.code("\n".join(snippet["body"]), language="python")
    else:
        st.warning("❌ Nie znaleziono snippetu o takim prefixie.")

# === Parsowanie YAML (jeśli potrzebne) ===
def wczytaj_konfiguracje(plik):
    with open(plik, encoding="utf-8") as f:
        return yaml.safe_load(f)
