import streamlit as st
import json
import os

# === Generator klasy ===
def generuj_klase(nazwa, atrybuty):
    linie = [f"class {nazwa}:"]
    linie.append("    def __init__(self, " + ", ".join(atrybuty) + "):")
    for a in atrybuty:
        linie.append(f"        self.{a} = {a}")
    return "\n".join(linie)

# === Ładowanie wszystkich snippetów z folderu ===
def wczytaj_snippety_z_folderu(folder):
    snippety = {}
    for plik in os.listdir(folder):
        if plik.endswith(".code-snippets"):
            kategoria = plik.replace(".code-snippets", "")
            try:
                with open(os.path.join(folder, plik), encoding="utf-8") as f:
                    snippety[kategoria] = json.load(f)
            except Exception as e:
                st.error(f"❌ Błąd w pliku `{plik}`: {e}")
    return snippety

# === UI ===
st.title("🧠 Generator Prototypów z Lokalnymi Snippetami")

folder_snippetów = "snippety"
wszystkie_snippety = wczytaj_snippety_z_folderu(folder_snippetów)

if wszystkie_snippety:
    kategorie = list(wszystkie_snippety.keys())
    wybrana_kategoria = st.selectbox("📂 Wybierz kategorię", kategorie)

    if wybrana_kategoria:
        snippety_kategorii = wszystkie_snippety[wybrana_kategoria]
        nazwy = list(snippety_kategorii.keys())
        wybrany = st.selectbox("🧩 Wybierz snippet", nazwy)

        if wybrany:
            dane = snippety_kategorii[wybrany]
            st.markdown(f"### ✨ Snippet: `{dane.get('prefix', wybrany)}`")
            st.markdown(f"**Opis:** {dane.get('description', 'Brak opisu')}")
            st.code("\n".join(dane.get("body", [])), language="python")
else:
    st.warning("⚠️ Nie znaleziono żadnych snippetów w folderze.")
