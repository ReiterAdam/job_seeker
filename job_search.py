import tomllib
import sys
import os
import pprint
import csv
from classes.justjoinit import JustJoinIT
from classes.olx import OLX
from classes.rocketjobs import RocketJobs
from classes.pracujpl import PracujPL
from classes.solidjobs import SolidJobs


def main():
    # load config
    user_conf = load_config()

    # search jobs on portal within matching properties
    search = user_conf['properties']['level'] + user_conf['properties']['skills']

    # search website with provided keywords
    offers_list = JustJoinIT.offers(search)

    # Save offers and output a list of new elements
    saved = save_offers(offers_list)
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
        visited = set()
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
    write_header = False
    if not os.path.isfile('founded.csv'):
        write_header = True
    with open('founded.csv', 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if write_header: writer.writeheader()
        for offer in offers_list:
            if offer['url'] not in visitied:
                writer.writerow(offer)
                saved.append(offer)
    return saved


def search_for_offers(user_config):
    search = {'pracuj.pl': PracujPL,
            'justjoin.it': JustJoinIT,
            'OLX': OLX,
            'RocketJobs': RocketJobs,
            'Solid.Jobs': SolidJobs}
    
    sites = user_config['websites']

    for site in sites:
        if sites[site]['enabled']:
            search[site].say_hello()


if __name__ == '__main__':
    main()