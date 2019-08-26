#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
from bs4 import BeautifulSoup as bs
import requests
import pymongo
import pandas as pd
from splinter import Browser
import time


# In[20]:
#master function
def scrape_info():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    mars_data= {
        "mars_titles": mars_title_p(browser),
        "mars_image": mars_image(browser),
    }
    return mars_data

# In[3]:


# Scrape the [NASA Mars News Site](https://mars.nasa.gov/news/) and collect the latest News Title and Paragraph Text. 
def mars_title_p(browser):
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    time.sleep(1)
    html = browser.html
    soup = bs(html, "html.parser")
    mars = {}
    mars['news_title'] = soup.find('div', class_='content_title').get_text().strip()
    mars['news_p']= soup.find("div", class_="article_teaser_body").get_text().strip()
    return mars



# Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string 
# to a variable called `featured_image_url`.
def mars_image(browser):
    url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars/assets/images/logo_nasa_trio_black@2x.png'
    browser.visit(url2)
    full_image_click= browser.find_by_id('full_image')
    full_image_click.click()
    time.sleep(3)
    browser.click_link_by_partial_text('more info')
    html = browser.html
    soup = bs(html, "html.parser")


# In[22]:


# Make sure to find the image url to the full size `.jpg` image.
# Make sure to save a complete url string for this image.
    image_path = soup.find('img', class_='main_image').get('src')
    
    # featured_image_url
    return 'https://www.jpl.nasa.gov' + image_path
# image_path


# In[7]:


# Visit the Mars Facts webpage [here](https://space-facts.com/mars/) and use Pandas to scrape the table containing facts 
# about the planet including Diameter, Mass, etc.

# def mars_table(browser):
# url3 = 'https://space-facts.com/mars/'
# browser.visit(url3)
# html = browser.html
# soup = bs(html, "html.parser")

# tables = pd.read_html(url3)
# tables


# In[9]:


# df=tables[1]
# df.head()


# In[10]:


# renamed_df = df.rename(columns={
#     0: "Description",
#     1: "Value"
# })
# renamed_df.head()


# In[11]:


# Use Pandas to convert the data to a HTML table string.
# renamed_df.to_html('mars_facts.html')


# In[28]:


# Visit the USGS Astrogeology site to obtain high resolution images for each of Mar's hemispheres.
# You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
# Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the 
# hemisphere name. Use a Python dictionary to store the data using the keys `img_url` and `title`.
# In[41]:


# url4='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars' 
# browser.visit(url4)

# hemisphere_image_urls =[]

# for i in range(4):
#     mars_title_and_images={}  

#     html = browser.html
#     soup = bs(html, "html.parser")

#     titles = soup.find_all('h3')
#     mars_title_and_images['title']= titles[i].get_text().strip()

#     image= browser.find_by_tag('h3')[i]
#     image.click()

#     html = browser.html
#     soup = bs(html, "html.parser")

#     mars_title_and_images['image_url']= soup.find('li').find('a')['href']


#     hemisphere_image_urls.append(mars_title_and_images)
#     browser.back()
    
# hemisphere_image_urls 





# browser.quit()


# # In[ ]:


# get_ipython().system('jupyter nbconvert --to script scrape_mars.ipynb')

