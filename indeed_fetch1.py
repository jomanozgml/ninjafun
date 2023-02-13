# Description: Scrapes a URL and returns the HTML source from dynamic page using pyppeteer
# Add the following in requirements.txt: pyppeteer==1.0.2

import asyncio
from pyppeteer import launch

async def get_details_indeed(givenUrl):
    """Scrapes a URL of dynamic page using Pyppeteer.
    
    Args:
        url (string): Fully qualified URL of a page.
    
    Returns:
        Title (string) and Description Text (list).
    """
    #Downloads the browser in next line
    browser = await launch(
        headless=True,
        handleSIGINT=False,
        handleSIGTERM=False,
        handleSIGHUP=False,
        args= ['--no-sandbox']
    )
    page = await browser.newPage()
    await page.setUserAgent('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36')
    
    if 'jk' in givenUrl:
      jkValue = givenUrl.split('jk=')[1].split('&')[0]
      baseUrl = 'https://au.indeed.com/viewjob?jk='
      url = baseUrl + jkValue
    else:
      url = givenUrl
      
    await page.goto(url)
    pageTitle = await page.title()
    try:
      positionElement = await page.querySelector('h1')
      position = await page.evaluate('(element) => element.innerText', positionElement)
      
      if 'indeed' in givenUrl:
        companyElement = await page.querySelector('[data-company-name = "true"]')
        company = await page.evaluate('(element) => element.innerText', companyElement)
        salaryElement = await page.querySelector('#salaryInfoAndJobType')
        salary = await page.evaluate('(element) => element.innerText', salaryElement)
        detailsElement = await page.querySelector('#jobDescriptionText')
        details = await page.evaluate('(element) => element.innerText', detailsElement)
        
      elif 'careerjet' in givenUrl:
        companyElement = await page.querySelector('.company')
        company = await page.evaluate('(element) => element.innerText', companyElement)
        salaryElement = await page.querySelector('.details')
        salary = await page.evaluate('(element) => element.innerText', salaryElement)
        detailsElement = await page.querySelector('.content')
        details = await page.evaluate('(element) => element.innerText', detailsElement)
      
      elif 'careerone' in givenUrl:
        companyElement = await page.querySelector('.jv-subtitle')
        company = await page.evaluate('(element) => element.innerText', companyElement)
        salaryElement = await page.querySelector('.jv-pay-summary')
        salary = await page.evaluate('(element) => element.innerText', salaryElement)
        detailsElement = await page.querySelector('#jvDescription')
        details = await page.evaluate('(element) => element.innerText', detailsElement)
      
      descriptionText = [position, company, salary, details]
    except:
      pTags = await page.querySelectorAll('p, h1, h2, h3, ul')
      descriptionText = [await page.evaluate('(element) => element.innerText', p) for p in pTags]
    await browser.close()
    print('extracted using pyppeteer')
    return pageTitle, descriptionText