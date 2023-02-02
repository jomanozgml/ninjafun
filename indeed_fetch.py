# Description: Scrapes a URL and returns the HTML source from dynamic page
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def get_details_indeed(givenUrl):
    # Options to run Chrome in headless mode
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36")

    driver = webdriver.Chrome('./chromedriver', options = options)
    jkValue = givenUrl.split('jk=')[1].split('&')[0]
    baseUrl = 'https://au.indeed.com/viewjob?jk='
    url = baseUrl + jkValue
    driver.get(url)

    html = driver.page_source

    # bs4 to parse the html
    soup = BeautifulSoup(html, "html.parser")
    title = soup.title.string
    tags = soup.select("p, h2, h3, h4, h5, h6, ul")
    text = [title] + [item.text+'\n' for item in list(tags)]
    driver.close() 
    return title, text