import urllib.request
from urllib.parse import urlparse
from bs4 import BeautifulSoup

def get_page(url):
    """Scrapes a URL and returns the HTML source.
    
    Args:
        url (string): Fully qualified URL of a page.
    
    Returns:
        soup (string): HTML source of scraped page.
    """
    
    response = urllib.request.urlopen(url)
    soup = BeautifulSoup(response, 
                         'html.parser', 
                         from_encoding=response.info().get_param('charset'))
    
    return soup

def get_og_title(soup):
    """Return the Open Graph title

    Args:
        soup: HTML from Beautiful Soup.
    
    Returns:
        value: Parsed content. 
    """

    if soup.findAll("meta", property="og:title"):
        return soup.find("meta", property="og:title")["content"]
    else:
        return
    
    return

def get_og_description(soup):
    """Return the Open Graph description

    Args:
        soup: HTML from Beautiful Soup.
    
    Returns:
        value: Parsed content. 
    """

    if soup.findAll("meta", property="og:description"):
        return soup.find("meta", property="og:description")["content"]
    else:
        return
    
    return
