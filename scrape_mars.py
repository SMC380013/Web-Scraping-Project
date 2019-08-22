# Dependencies
from bs4 import BeautifulSoup as bs
import requests
import pymongo
import pandas as pd
from splinter import Browser
import time
def scrape_info():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)
    mars = {}

# Scrape the [NASA Mars News Site](https://mars.nasa.gov/news/) and collect the latest News Title and Paragraph Text. 

    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    time.sleep(1)
    html = browser.html
    soup = bs(html, "html.parser")


    # Assign the text to variables that you can reference later.

    mars['news_title'] = soup.find('div', class_='content_title').get_text().strip()
    mars['news_p']= soup.find("div", class_="article_teaser_body").get_text().strip()
    # mars

    # Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string 
    # to a variable called `featured_image_url`.

    url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars/assets/images/logo_nasa_trio_black@2x.png'
    browser.visit(url2)
    full_image_click= browser.find_by_id('full_image')
    full_image_click.click()
    time.sleep(3)
    browser.click_link_by_partial_text('more info')
    html = browser.html
    soup = bs(html, "html.parser")

    # Make sure to find the image url to the full size `.jpg` image.
    # Make sure to save a complete url string for this image.
    image_path = soup.find('img', class_='main_image').get('src')
    mars['featured_image_url'] = 'https://www.jpl.nasa.gov' + image_path
    # featured_image_url
    # mars
    # image_path

    # Visit the Mars Facts webpage [here](https://space-facts.com/mars/) and use Pandas to scrape the table containing facts 
    # about the planet including Diameter, Mass, etc.

    url3 = 'https://space-facts.com/mars/'
    browser.visit(url3)
    html = browser.html
    soup = bs(html, "html.parser")

    tables = pd.read_html(url3)
    # tables

    df=tables[1]
    # df.head()

    renamed_df = df.rename(columns={
        0: "Description",
        1: "Value"
    })
    # renamed_df.head()

    renamed_df.to_html('mars_facts.html')

    mars['table']= renamed_df

    browser.quit()

    return mars