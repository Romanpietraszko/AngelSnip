import argparse
from genprototypów import generuj_klase

# === CLI ===
parser = argparse.ArgumentParser(description='Generator prototypów')
parser.add_argument('--nazwa', required=False)
parser.add_argument('--komponenty', nargs='+', default=[])
parser.add_argument('--prefix', required=False)
parser.add_argument('--folder_snippetow', required=False, default="snipety")
args = parser.parse_args()
print(generuj_klase(args.nazwa, args.komponenty))
