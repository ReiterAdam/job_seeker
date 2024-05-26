## Description

Job seeker is a Python script which automates collecting job offers from websites and gathers them at one place. User can define preffered keywords for his searches and websites which he wants to monitor. Every time search is running, program compares already found offers and saves only new ones - offers are compared based on URL. Currently supported websites:

+ **justjoin.it**
+  **solid.jobs**
+ ~~pracuj.pl~~
+ ~~olx.pl~~
+ ~~rocketjobs.pl~~


## Features

+ **Search configuration:** The script uses user preferences saved in `config.toml` file, allowing to specify stack or level and also website which should be searched. Quality of the output relies on quality of search engine implemented on the website.
+ **Web Scraping:** On the run, the script is using `selenium` and `BeautifulSoup` to scrape job offers from websites based on criteria from `config.toml`
+ **Data Extraction:** After getting data from website, the script extracts information useful for user, as **job title**, **URL**, **salary**, **required skills** and **location**.
+ **Duplicate Handling:** To filter out already saved offers, the script ensures that every saved offer is unique.
+ **Friendly CSV output:** The script saves unique job offers into a csv file, `founded.csv`, which allows easier integration with any other application. 

## Technologies

The project uses internal libraries (tomllib, os, sys, re and csv) but also relies heavly on two external dependencies:
+ Selenium
+ BeautifulSoup4


## Installation

As most of the other python applications, this script also requires installation of required dependencies. You can install them using pip
```
pip install -r requirements.txt
```

It is also required to have Firefox web browser installed on your system, as the script uses `selenium` with Firefox webdriver.


## Configuration

The `config.toml` file contains simple structure to make searching more precise. 
Currently, script supports config saved in `.toml` filetype with following structure:

1. List of websites with following schema:
```
[websites]
[websites.'justjoin.it']
address = "https://justjoin.it/"
enabled = true

[website.name]
address = "website URL"
enabled = <true/false>
```
Each website has its `address` and boolean `enabled` value, which indicates if the website is included in search or not.

2. List of properties with following schema:
```
[properties]
level = ["<junior/regular/senior>"]
skills = ["list", "of", "skills"]
```

So for example, `[properties]` section can look something like this:

```
[properties]
level = ["junior"]
skills = ["python", "sql"]
```


## Usage 

1. Clone or download the repository and install dependencies
2. Adjust `config.toml` to suit your search preferences
3. Run the script with following command
   ```
   python job_seeker.py
   ```
4. Go to `founded.csv` and look for offers!   


## Output
The `founded.csv` contains 7 following columns:
+ **title** - which contains job title from the offer,
+ **url** - contains URL leading to page with offer,
+ **salary** - stores salary from job offer,
+ **localization** - contains information where office is located,
+ **is_remote** - boolean value which indicates if remote working is allowed or not,
+ **skills** - list of main skills required,
+ **collected_on** - contains date that indicates when offer was scraped.
