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

    # search website with provided keywords
    offers = JustJoinIT.offers(search)

    # Save offers and output a list of new elements
    saved = save_offers(offers)
    print("Offers saved: ")
    pp = pprint.PrettyPrinter(indent=4, sort_dicts=False)
    pp.pprint(saved)


def load_config():
    """functions returns config file as dictionary"""
    try:
        with open("config.toml", "rb") as f:
            data = tomllib.load(f)
            return data
    except FileNotFoundError:
        sys.exit("config.toml not found!")


def load_founded():
    """function returns set of urls leading to already founded offers"""
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
    """function saves new offers in provided list and returns list of saved offers"""
    if len(offers_list) == 0: return
    visitied = load_founded()
    saved = []
    fieldnames = ['title', 'url', 'salary', 'localization', 'is_remote', 'skills']
    with open('founded.csv', 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        for offer in offers_list:
            if offer['url'] not in visitied:
                writer.writerow(offer)
                saved.append(offer)
    return saved


if __name__ == '__main__':
    main()