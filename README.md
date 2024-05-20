## Description

Job seeker is a Python script which automates collecting job offers from websites and gathers them at one place. User can define preffered keywords for his searches and websites which he wants to monitor. Every time search is running, program compares already found offers and saves only new ones - offers are compared based on urls. Currently supported websites:

+ **justjoin.it**
+ ~~pracuj.pl~~
+ ~~olx.pl~~
+ ~~rocketjobs.pl~~
+ **solid.jobs**


## Features

+ **Search configuration:** The script uses user preferences saved in `config.toml` file, allowing to specify stack or level and also website which should be searched. Quality of the output relies on quality of search engine implemented on the website.
+ **Web Scraping:** On the run, the script is using `selenium` and `BeautifulSoup` to scrape job offers from websites which matches criteria from `config.toml`
+ **Data Extraction:** After getting data from website, the script extracts information useful for user, as **job title**, **URL**, **salary**, **required skills** and **location**.
+ **Duplicate Handling:** To filter out already saved offers, the script ensures that every saved offer is unique.
+ **Friendly CSV output:** The script saves unique job offers into a csv file, `founded.csv`, which allows easier integration with any other application. 

## Technologies

Project uses internal libraries like tomllib, os, sys and csv, but heavly relies on two external dependencies:
+ Selenium
+ BeautifulSoup4


## Installation

As most of other python applications, this script also requires installation of required dependencies. You can install them using pip
```
pip install -r requirements.txt
```

It is also required to have  Firefox web browser installed on your system, as the script uses `selenium` with Firefox webdriver.


## Configuration

The `config.toml` file contains simple structure to make searching more precise. 


## Usage 
1. Clone or download the repository and install dependencies
2. Adjust `config.toml` to suit your search preferences
3. Run the script with following command
   ```
   python job_seeker.py
   ```
4. Go to `founded.csv` and look for offers!   

