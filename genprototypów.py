import argparse
import streamlit as st
import yaml
import json
import os

# === CLI ===
parser = argparse.ArgumentParser(description='Generator prototypów')
parser.add_argument('--nazwa', required=False)
parser.add_argument('--komponenty', nargs='+', default=[])
parser.add_argument('--prefix', required=False)
parser.add_argument('--folder_snippetow', required=False, default="snipety")
args = parser.parse_args()

# === Generator klasy ===
def generuj_klase(nazwa, atrybuty):
    linie = [f"class {nazwa}:"]
    linie.append("    def __init__(self, " + ", ".join(atrybuty) + "):")
    for a in atrybuty:
        linie.append(f"        self.{a} = {a}")
    return "\n".join(linie)

# === Ładowanie snippetów z folderu ===
def znajdz_snippet_w_folderze(folder, prefix):
    for plik in os.listdir(folder):
        if plik.endswith(".code-snippets"):
            sciezka = os.path.join(folder, plik)
            try:
                with open(sciezka, encoding="utf-8") as f:
                    snippety = json.load(f)
                    for nazwa, dane in snippety.items():
                        if dane.get("prefix") == prefix:
                            return dane
            except Exception as e:
                print(f"Błąd w pliku {plik}: {e}")
    return None

# === UI (Streamlit) ===
st.title("🧠 Generator Prototypów z Lokalnymi Snippetami")

folder_ui = st.text_input("📁 Folder z snippetami", value=args.folder_snippetow)
prefix_ui = st.text_input("🔍 Prefix snippetu (np. 'todo', 'pętlafor')")

if st.button("🔄 Załaduj snippet"):
    snippet = znajdz_snippet_w_folderze(folder_ui, prefix_ui)
    if snippet:
        st.subheader(f"✅ Snippet: {prefix_ui}")
        st.code("\n".join(snippet["body"]), language="python")
    else:
        st.warning("❌ Nie znaleziono snippetu o takim prefixie.")

# === Parsowanie YAML (jeśli potrzebne) ===
def wczytaj_konfiguracje(plik):
    with open(plik, encoding="utf-8") as f:
        return yaml.safe_load(f)

# === CLI fallback ===
if __name__ == "__main__":
    if args.prefix:
        snippet = znajdz_snippet_w_folderze(args.folder_snippetow, args.prefix)
        if snippet:
            print("\n".join(snippet["body"]))
        else:
            print("Nie znaleziono snippetu.")
    elif args.nazwa:
        print(generuj_klase(args.nazwa, args.komponenty))
