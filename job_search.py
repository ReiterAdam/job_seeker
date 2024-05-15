# import requests
import tomllib
import sys
from html.parser import HTMLParser
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


class Parser(HTMLParser):
    def handle_data(self, data: str) -> None:
        print(data)




def main():
    # load config

    # search jobs on portal within matching properties

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


def get_job_offers():
    url = "https://justjoin.it/"

    driver = webdriver.Firefox()

    driver.get(url)

    driver.implicitly_wait(2)
  
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    offers = soup.find_all('div', class_='css-2crog7')

    driver.quit()
    return offers

def scope_offers(offers_list):
    """function takes list of bs4.element.ResultSet from justjoin.it and returns list of dict with url, skills, etc"""
    refined_data = []
    for offer in offers_list:
        title = offer.findChild(class_='css-1gehlh0').get_text()
        url = "https://justjoin.it/" + offer.findChild(class_='offer_list_offer_link').get('href')
        salary = offer.findChild(class_='css-17pspck').get_text()
        loc = offer.findChild(class_='css-11qgze1').get_text()
        skills = [x.get_text() for x in offer.findAll(class_='css-d6miz5')]
        refined_data.append({'title': title,
                        'url': url,
                        'salary': salary,
                        'localization': loc,
                        'skills': skills})
    return refined_data


if __name__ == '__main__':
    main()