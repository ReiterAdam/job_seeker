import tomllib
import sys
import pprint
from justjoinit import JustJoinIT
import csv


def main():
    # load config
    user_conf = load_config()

    # search jobs on portal within matching properties
    search = user_conf['properties']['level'] + user_conf['properties']['skills']

    offers = JustJoinIT.offers(search)
    save_offers(offers)
    pp = pprint.PrettyPrinter(indent=4, sort_dicts=False)
    pp.pprint(offers)
    # if matches -> save offer to json with 
    # - href
    # - salary
    # - position
    # - localization
    # - type of offer (b2b etc)
    # - remote/on site/hybrid
    # - requirements
    # - benefits

    # output job offers


def load_config():
    try:
        with open("config.toml", "rb") as f:
            data = tomllib.load(f)
            return data
    except FileNotFoundError:
        sys.exit("config.toml not found!")


def load_founded():
    try:
        visited = {}
        with open("founded.csv", newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                visited.add(row['url'])
        return visited

    except FileNotFoundError:
        return {}
    
    
def save_offers(offers_list):
    if len(offers_list) == 0: return
    visitied = load_founded()
    fieldnames = ['title', 'url', 'salary', 'localization', 'is_remote', 'skills']
    with open('founded.csv', 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        for offer in offers_list:
            if offer['url'] not in visitied:
                writer.writerow(offer)

if __name__ == '__main__':
    main()