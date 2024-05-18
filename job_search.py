import tomllib
import sys
import pprint
from justjoinit import JustJoinIT


def main():
    # load config
    user_conf = load_config()

    # search jobs on portal within matching properties
    search = user_conf['properties']['level'] + user_conf['properties']['skills']

    offers = JustJoinIT.offers(search)
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


if __name__ == '__main__':
    main()