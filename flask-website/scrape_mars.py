#import dependencies
import pymongo
from bs4 import BeautifulSoup
from splinter import Browser
import requests
import os
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


def scrape():
    #Connect to Mars websites
    #Chromedriver Setup
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://redplanetscience.com/'
    browser.visit(url)
    #Scrape the latest new title
    news_title = browser.find_by_css('div.content_title').text
    print(news_title)

    #Scrape the latest news paragraph
    news_p = browser.find_by_css('div.article_teaser_body').text
    print(news_p)

    #Visit Website
    browser.visit('https://spaceimages-mars.com/image/featured/mars2.jpg')
    #Scrape image source
    browser.find_by_css('img')['src']

    #Scraping Mars facts
    pd.read_html('https://galaxyfacts-mars.com/',
                index_col=0,header=0)[0].reset_index().to_html()

    #Scrape images titles and url's
    browser.visit('https://marshemispheres.com/')

    hemispheres = [];
    for i in range(3):
        hemisphere = {}
        browser.find_by_css('a h3')[i].click()
        hemisphere['title'] = browser.find_by_tag('h2').text
        hemisphere['url'] = browser.find_by_text('Sample')['href']
        hemispheres.append(hemisphere)
        browser.back()

    print(hemispheres )  

    #Quit browser
    browser.quit()
    return hemispheres


  