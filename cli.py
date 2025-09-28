import argparse
import json
import os
from genprototypow import generuj_klase, znajdz_snippet_w_folderze

parser = argparse.ArgumentParser(description='Generator prototypów (CLI)')
parser.add_argument('--nazwa', required=False)
parser.add_argument('--komponenty', nargs='+', default=[])
parser.add_argument('--prefix', required=False)
parser.add_argument('--folder_snippetow', required=False, default="snipety")
args = parser.parse_args()

if args.prefix:
    snippet = znajdz_snippet_w_folderze(args.folder_snippetow, args.prefix)
    if snippet:
        print("\n".join(snippet["body"]))
    else:
        print("❌ Nie znaleziono snippetu.")
elif args.nazwa:
    print(generuj_klase(args.nazwa, args.komponenty))
else:
    print("⚠️ Podaj --prefix lub --nazwa.")

