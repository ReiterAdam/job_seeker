# import requests
import tomllib
import sys
import pprint
from selenium import webdriver
from bs4 import BeautifulSoup


class JustJoinIT:

    @classmethod
    def get_job_offers(cls, keywords=""):
        url = "https://justjoin.it/" + keywords
        driver = webdriver.Firefox()
        driver.get(url)
        driver.implicitly_wait(10)
        
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        offers = soup.find_all('div', class_='css-2crog7')
        driver.quit()
        
        return offers

    @classmethod
    def scope_offers(cls, offers_list):
        """function takes list of bs4.element.ResultSet from justjoin.it and returns list of dict with url, skills, etc"""
        refined_data = []
        for offer in offers_list:
            title = offer.findChild(class_='css-1gehlh0').get_text()
            url = "https://justjoin.it/" + offer.findChild(class_='offer_list_offer_link').get('href')
            salary = offer.findChild(class_='css-17pspck').get_text()
            loc = offer.findChild(class_='css-11qgze1').get_text()
            is_remote = offer.findChild(class_='css-1am4i4o').get_text() == 'Fully remote'
            skills = [x.get_text() for x in offer.findAll(class_='css-d6miz5')]
            refined_data.append({'title': title,
                            'url': url,
                            'salary': salary,
                            'localization': loc,
                            'is_remote': is_remote,
                            'skills': skills})
        return refined_data

    @classmethod
    def offers(cls, properties=[]):
        if len(properties) > 0:
            properties = [f'keyword={p}' for p in properties]
            keywords = "?" + '&'.join(properties)
            data = cls.get_job_offers(keywords)
        else:
            data = cls.get_job_offers()

        return cls.scope_offers(data)

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
    ...



def load_config():
    try:
        with open("config.toml", "rb") as f:
            data = tomllib.load(f)
            return data
    except FileNotFoundError:
        sys.exit("config.toml not found!")




if __name__ == '__main__':
    main()