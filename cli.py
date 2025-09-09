import argparse
from genprototypów import generuj_klase

parser = argparse.ArgumentParser(description='Generator prototypów')
parser.add_argument('--nazwa', required=True)
parser.add_argument('--komponenty', nargs='+')
args = parser.parse_args()

print(generuj_klase(args.nazwa, args.komponenty))
