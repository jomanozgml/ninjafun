import asyncio
from pyppeteer import launch

async def get_title(page):
    title = await page.title()
    # print('\nPage Title: ', title)
    return title

# async def get_header(page):
#     header = await page.querySelector('div.jobsearch-JobInfoHeader-title-container')
#     headerText = await page.evaluate('(element) => element.innerText', header)
#     print('Position: ', headerText)
#     return headerText

async def get_description(page):
    description = await page.querySelector('div.jobsearch-JobComponent-description')
    descriptionText = await page.evaluate('(element) => element.innerText', description)
    # print(descriptionText)
    return descriptionText

async def get_page_indeed(givenUrl):
    browser = await launch({'headless': False})
    page = await browser.newPage()
    # givenUrl = 'https://au.indeed.com/jobs?q=job&l=&from=searchOnHP&vjk=ad88182b4518224e'
    # givenUrl = 'https://au.indeed.com/viewjob?jk=be96118bcf5dd22e&tk=1gngp7r1h2dco001&from=hp&advn=2595845290210001&adid=404828828&ad=-6NYlbfkN0AWliH01-JgzK6KcFHWZAKWGb0FjFFUlAzISIC1Rp0MmJ476PWKXVQv0uyDp7wXdjAtunlJCKVlQ-H3EW9lEElYCuOtEYyEU-clLaqfpdyqEVZJZcb2eUet393sqhL2oZd1HMEmU0S04SIuObX87o8yiS8JYZKhslDVjgWnumZJ5nVrKZxZ0hqETitIsOe2F5QUmHB2KGcksshUh9KiUUh-GDhUKNJ9b6Uqx8BYgeKqrfUxwadV7nZDgMaxw9VN6kgGoDSy-lO6KiVtXEj14n4DWfdLk63ITRQv_POE2DjPy4yP9rvVJznRm1VzHDcyDS4po53Tvd8kV7Ytebk-Y1dAhOvmEJJq6t2UHtSPZgdT83_t2QRdEjQsejqeWUdC18F-FfbIEa4isp_wBg2cSCMqYe6-oiZl9AOoZOYsCuQvB_vJKk0ROElLAPjv2Rqx8GgegIGDXO9vBf8eSI_u8OGUqAFFoQFLbK_KxjIW8qcnXRwMZnF6pX877Lg5Kd_QYaM%3D&pub=4a1b367933fd867b19b072952f68dceb&xkcb=SoBK-_M3Uw6vR0ACtz0LbzkdCdPP&vjs=3'
    # givenUrl = 'https://au.indeed.com/?from=gnav-viewjob&advn=4130294693969652&vjk=8e637c1653643683'
    jkValue = givenUrl.split('jk=')[1].split('&')[0]
    baseUrl = 'https://au.indeed.com/viewjob?jk='
    url = baseUrl + jkValue
    await page.goto(url)
    # await page.screenshot({'path': 'example.png'})
    # await get_title(page)
    # await get_header(page)
    # await get_description(page)
    return page
    await browser.close()

# asyncio.get_event_loop().run_until_complete(get_page_indeed(givenUrl))