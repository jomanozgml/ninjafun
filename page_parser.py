# Description: Scrapes a URL and returns the HTML source from static page
import urllib.request
from urllib.parse import urlparse
from bs4 import BeautifulSoup

def get_page(url):
    response = urllib.request.urlopen(url)
    soup = BeautifulSoup(response, 
                         'html.parser', 
                         from_encoding=response.info().get_param('charset'))
    
    title = soup.title.string
    # desc is snippet of the page
    desc = soup.find("meta", property="og:description")['content']
    tags = soup.select("p, h2, h3, h4, h5, h6, ul")
    # text is the list of all the text in the page
    text = [title+'\n'] + [item.text+'\n' for item in list(tags)]
    
    return title, text