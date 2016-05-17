import argparse
from analyzer import main

parser = argparse.ArgumentParser(description='analyze scraped references from imdb')
parser.add_argument('-p', '--print', type=int, help="prints the defined number of movies")

args = parser.parse_args()

main.printTopTen(args.print)
