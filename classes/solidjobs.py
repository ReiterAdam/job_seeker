from selenium import webdriver
from bs4 import BeautifulSoup

class SolidJobs:

    @classmethod
    def get_job_offers(cls, keywords=""):
        url = 'https://solid.jobs/offers/it;' + keywords
        options = webdriver.FirefoxOptions() 
        options.add_argument("--headless") 
        driver = webdriver.Firefox(options=options)
        driver.get(url)
        # driver.implicitly_wait(10)

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        offers = soup.find_all('offer-list-item')
        # driver.implicitly_wait(10)
        driver.quit()

        return offers

    @classmethod
    def scope_offers(cls, offers_list):
        """function takes list of bs4.element.ResultSet from rocketjobs.pl and returns list of dict with url, skills, etc"""
        refined_data = []
        for offer in offers_list:
            title = offer.findChild('h2', class_='font-weight-500 h5').get_text().strip()
            url = "https://solid.jobs/" + offer.findChild('a', class_='color-dark-grey color-blue-onhover').get('href')
            salary = offer.findChild(class_='mat-tooltip-trigger badge badge-salary hoverable mr-1 ng-star-inserted').get_text()
            loc = offer.findChild('span', class_='mat-tooltip-trigger ng-star-inserted').get_text()[1:]
            is_remote = "100% zdalnie" in loc
            skills = [x.get_text() for x in offer.findAll(class_='skill-display ng-star-inserted')]
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
            exp = properties['level'][0].strip()
            if exp in ['junior', 'regular', 'senior']:
                exp = 'experiences=' + exp
            else:
                exp = ''
            keywords = "searchTerm=" + ','.join(properties['skills']) + ';' + exp
            data = cls.get_job_offers(keywords)
        else:
            data = cls.get_job_offers()

        return cls.scope_offers(data)
