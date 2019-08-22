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


# In[76]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


# Scrape the [NASA Mars News Site](https://mars.nasa.gov/news/) and collect the latest News Title and Paragraph Text. 

url = 'https://mars.nasa.gov/news/'
browser.visit(url)
time.sleep(1)
html = browser.html
soup = bs(html, "html.parser")
mars = {}


# In[4]:


# Assign the text to variables that you can reference later.

mars['news_title'] = soup.find('div', class_='content_title').get_text().strip()
mars['news_p']= soup.find("div", class_="article_teaser_body").get_text().strip()
mars


# In[78]:


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


# In[84]:


# Make sure to find the image url to the full size `.jpg` image.
# Make sure to save a complete url string for this image.
image_path = soup.find('img', class_='main_image').get('src')
mars['featured_image_url'] = 'https://www.jpl.nasa.gov' + image_path
# featured_image_url
mars
# image_path


# In[7]:


# Visit the Mars Facts webpage [here](https://space-facts.com/mars/) and use Pandas to scrape the table containing facts 
# about the planet including Diameter, Mass, etc.

url3 = 'https://space-facts.com/mars/'
browser.visit(url3)
html = browser.html
soup = bs(html, "html.parser")


# In[8]:


tables = pd.read_html(url3)
tables


# In[11]:


df=tables[1]
df.head()


# In[85]:


renamed_df = df.rename(columns={
    0: "Description",
    1: "Value"
})
renamed_df.head()


# In[86]:


# Use Pandas to convert the data to a HTML table string.
renamed_df.to_html('mars_facts.html')


# In[31]:


# Visit the USGS Astrogeology site to obtain high resolution images for each of Mar's hemispheres.
# You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
# Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the 
# hemisphere name. Use a Python dictionary to store the data using the keys `img_url` and `title`.


# url4='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars' 
# url4='https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
# browser.visit(url4)
# html = browser.html
# soup = bs(html, "html.parser")
# mars_title_and_images={}


# In[96]:


# html


# In[93]:


# mars_title_and_images['cerberus_title'] = soup.find('h2', class_="title").get_text().strip()
# # soup.select('h2.title')
# mars_title_and_images


# In[92]:


# cerberus_image= soup.find_all('img')[0]["src"]
# mars_title_and_images['cerberus_image']= url4 + cerberus_image
# mars_title_and_images


# In[44]:


# url5='https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
# browser.visit(url5)
# html = browser.html
# soup = bs(html, "html.parser")

# mars_title_and_images['valles_marineris_title'] = soup.find('h2', class_="title").get_text().strip()


# In[45]:


# valles_marineris_image= soup.find_all('img')[0]["src"]
# mars_title_and_images['valles_marineris_image']= url5 + valles_marineris_image


# In[46]:


# url6='https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
# browser.visit(url6)
# html = browser.html
# soup = bs(html, "html.parser")

# mars_title_and_images['schiaparelli_title'] = soup.find('h2', class_="title").get_text().strip()


# In[47]:


# schiaparelli_image= soup.find_all('img')[0]["src"]
# mars_title_and_images['schiaparelli_image']= url6 + schiaparelli_image


# In[88]:


# url7='https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
# browser.visit(url5)
# html = browser.html
# soup = bs(html, "html.parser")

# mars_title_and_images['syrtis_major_title'] = soup.find('h2', class_="title").get_text().strip()


# In[89]:


# syrtis_major_image= soup.find_all('img')[0]["src"]
# mars_title_and_images['syrtis_major_image']= url7 + syrtis_major_image


# In[90]:


# Append the dictionary with the image url string and the hemisphere title to a list. 
# This list will contain one dictionary for each hemisphere.

# hemisphere_image_urls =[]
# hemisphere_image_urls.append(mars_title_and_images)
# hemisphere_image_urls 


# In[91]:


browser.quit()


# In[95]:


get_ipython().system('jupyter nbconvert --to script scrape_mars.ipynb')


# In[ ]:





# In[ ]:




