from selenium import webdriver
from bs4 import BeautifulSoup

class PracujPL:

    @classmethod
    def get_job_offers(cls, keywords=""):
        # TODO
        ...

    @classmethod
    def scope_offers(cls, offers_list):
        """function takes list of bs4.element.ResultSet from pracuj.pl and returns list of dict with url, skills, etc"""
        # TODO
        ...

    @classmethod
    def offers(cls, properties=[]):
        if len(properties) > 0:
            properties = [f'keyword={p}' for p in properties]
            keywords = "?" + '&'.join(properties)
            data = cls.get_job_offers(keywords)
        else:
            data = cls.get_job_offers()

        return cls.scope_offers(data)


    @classmethod
    def say_hello(cls):
        print(f"{cls.__name__} says hello!")