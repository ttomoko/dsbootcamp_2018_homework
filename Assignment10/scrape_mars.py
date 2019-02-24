#dependencies
from bs4 import BeautifulSoup as bs
from splinter import Browser
from selenium import webdriver
import requests
import pymongo
import pandas as pd
import time

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver"} 
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
    mars_results = {}

    #visit the news site
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    time.sleep(1)

    #using bs to write it into html
    html = browser.html
    soup = bs(html, 'html.parser')

    #mars latest news scrape
    news_title = soup.find("div", class_="content_title").text
    news_p = soup.find("div", class_="article_teaser_body").text

    mars_results["news_title"] = news_title
    mars_results["news_p"] = news_p

    #JPL Mars Space Images - Featured Image
    url_spaceimage = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url_spaceimage)
    time.sleep(1)
    html = browser.html
    soup = bs(html,'html.parser')
    featured_image_list = []

    for image in soup.find_all('div',class_="img"):
        featured_image_list.append(image.find('img').get('src'))

    #feature image
    feature_Image = featured_image_list[0]

    #feature image url 
    feature_Image_url = "https://www.jpl.nasa.gov/" + feature_Image

    feature_Image_dict = {"image": feature_Image_url}

    mars_results["featured_image"] = feature_Image_url 


    #Mars Weather
    #Visit the Mars Weather twitter account here and scrape the latest Mars weather tweet from the page.
    url_weathertwitter = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url_weathertwitter)

    html = browser.html
    soup = bs(html, 'html.parser')
    #print(soup.prettify)

    tweets = soup.find("div", class_="stream").find("ol").find_all("li", class_="js-stream-item")
    for tweet in tweets:
        tweet_text = tweet.find("div", class_="js-tweet-text-container").text
    if "Sol " in tweet_text:
        mars_weather = tweet_text.strip() 
    mars_results["mars_weather"] = mars_weather

    #Mars Facts
    url_facts = "https://space-facts.com/mars/"
    time.sleep(2)
    table = pd.read_html(url_facts)
    table[0]

    df_mars_facts = table[0]
    df_mars_facts.columns = ["Index", "Values"]
    clean_table = df_mars_facts.set_index(["Index"])
    mars_html_table = clean_table.to_html()
    mars_html_table = mars_html_table.replace("\n", "")
    mars_results["mars_facts_table"] = mars_html_table

    #Mars hemispheres photo scraping
    base_hemisphere_url = "https://astrogeology.usgs.gov"
    url_hemisphere = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url_hemisphere)

    html = browser.html
    soup = bs(html, 'html.parser')
    
    hemisphere_image_urls = []

    links = soup.find_all("div", class_="item")

    for link in links:
        img_dict = {}
        title = link.find("h3").text
        next_link = link.find("div", class_="description").a["href"]
        full_next_link = base_hemisphere_url + next_link
        
        browser.visit(full_next_link)
        
    pic_html = browser.html
    pic_soup = bs(pic_html, 'html.parser')
        
    url = pic_soup.find("img", class_="wide-image")["src"]

    img_dict["title"] = title
    img_dict["img_url"] = base_hemisphere_url + url
        
    hemisphere_image_urls.append(img_dict)

    mars_results["hemisphere_image_urls"] = hemisphere_image_urls

    browser.quit()

    return mars_results


