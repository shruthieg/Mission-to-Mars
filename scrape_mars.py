# import dependicies
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
import time
import pandas as pd
import numpy as np
from splinter.exceptions import ElementDoesNotExist



    # Initiate headless driver for deployment
browser = Browser("chrome", executable_path="chromedriver", headless=True)



def get_mars_news():
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')
    content_titles = soup.find_all('div', class_ = 'content_title')
    titles = []
    paragraphs = []
    for title in content_titles:
        titles.append(title.a.text.strip())
        content_paragraphs = soup.find_all('div', class_ = 'rollover_description_inner')
        for paragraph in content_paragraphs:
            paragraphs.append(paragraph.text.strip())
            latest_title = titles[0]
            latest_paragraph = paragraphs[0]
    return latest_title, latest_paragraph

# news_title, news_paragraph = get_mars_news()
# print (f"{news_title} {news_paragraph}")

# ## JPL Mars Space Images - Featured Image

def get_featured_image_url():
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    browser.click_link_by_partial_text('FULL IMAGE')
    html = browser.html
    soup = bs(html, 'html.parser')
    featured_image_url=soup.find('div', class_='img')
    featured_image_url = featured_image_url.find('img')['src']
    featured_image_url = 'https://www.jpl.nasa.gov' + featured_image_url
    return featured_image_url

# featured_image = get_featured_image_url()
# print (f"{featured_image}")

# # # Mars Weather


def get_twitter_weather():
    url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')
    tweets=soup.find_all('p', class_='TweetTextSize')
    for tweet in tweets:
        if 'Sol' in tweet.text:
            mars_weather = tweet.text
            break
    return(mars_weather)

# weather =  get_twitter_weather()
# print (f"{weather}")

# # # Mars Facts

def get_mars_facts():
    import pandas as pd
    url = 'https://space-facts.com/mars/'
    mars_facts = pd.read_html(url)
    df = mars_facts[0]
    df.columns = ['features', 'values']
    return df.to_html()

# facts = get_mars_facts()
# print(f"{facts}")

# # # Mars Hemispheres

def get_hemispheres():
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    browser.click_link_by_partial_text('Cerberus')
    browser.click_link_by_partial_text('Open')
    html = browser.html
    soup = bs(html, 'html.parser')
    img3=soup.find('img', class_='wide-image')
    img3 = img3.get('src')
    img3 = 'https://astrogeology.usgs.gov' + img3
    browser.back()
    browser.click_link_by_partial_text('Schiaparelli')
    browser.click_link_by_partial_text('Open')
    html = browser.html
    soup = bs(html, 'html.parser')
    img4=soup.find('img', class_='wide-image')
    img4 = img4.get('src')
    img4 = 'https://astrogeology.usgs.gov' + img4
    browser.back()
    browser.click_link_by_partial_text('Syrtis')
    browser.click_link_by_partial_text('Open')
    html = browser.html
    soup = bs(html, 'html.parser')
    img5=soup.find('img', class_='wide-image')
    img5 = img5.get('src')
    img5 = 'https://astrogeology.usgs.gov' + img5
    browser.back()
    browser.click_link_by_partial_text('Valles')
    browser.click_link_by_partial_text('Open')
    html = browser.html
    soup = bs(html, 'html.parser')
    img6=soup.find('img', class_='wide-image')
    img6 = img6.get('src')
    img6 = 'https://astrogeology.usgs.gov' + img6

    title1= img3.split('/')
    title1 = title1[5].split('_')[1]
    title2 = img4.split('/')
    title2= title2[5].split('_')[1]
    title3 = img5.split('/')
    title3 = title3[5].split('_')[1]
    title4 = img6.split('/')
    title4 = title4[5].split('_')[1]
    #titles = [title1, title2, title3, title4]

    img_urls =[(title1, img3),(title2, img4),(title3, img5),(title4, img6)]

    # for i, j in zip(titles, img_urls):
    #     print('titles: ' + i +', img_urls : '+ j)
    return img_urls

# hemispheres =  get_hemispheres()
# print(f"{hemispheres}")

def scrape_all():
# Run all scraping functions and store in dictionary.
    data = {
        "news_title": get_mars_news()[0],
        "news_paragraph": get_mars_news()[1],
        "featured_image": get_featured_image_url(),
        "weather" :  get_twitter_weather(),
        "facts": get_mars_facts(),
        "hemispheres": get_hemispheres()
    }
    browser.quit()

    # Stop webdriver and return data
    return data


# data = scrape_all()
# print(f"{data}")