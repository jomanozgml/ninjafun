# Description: Scrapes a URL and returns the HTML source from dynamic page using Scrape.do
# Free Plan comes with With 5 concurrent requests, a total of 1000 requests per month

# import requests
# from bs4 import BeautifulSoup

# def get_details_indeed(givenUrl):
#     # Formats the the given url that directs to specific page
#     jkValue = givenUrl.split('jk=')[1].split('&')[0]
#     baseUrl = 'https://au.indeed.com/viewjob?jk='
#     target_url = baseUrl + jkValue
#     api_token = "e1684eed86c04f7f8080238648018dc3b4ad58083f9"
#     url = f"http://api.scrape.do/?token={api_token}&url={target_url}"
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, "html.parser")
#     title = soup.title.string
#     tags = soup.select("p, h2, h3, h4, h5, h6, ul")
#     text = [title] + [item.text+'\n' for item in list(tags)]
#     return title, text