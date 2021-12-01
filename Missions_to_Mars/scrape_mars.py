#Import libraries
from bs4 import BeautifulSoup
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://redplanetscience.com/'
    browser.visit(url)
    time.sleep(1)

    # Create beautiful Soup object
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    news = soup.find_all('div', class_='list_text')
    news_date = news[0].find("div", class_ = "list_date").get_text()
    news_title = news[0].find("div", class_="content_title").get_text()
    news_p = news[0].find("div", class_="article_teaser_body").get_text()
    print("-"*75)
    print(news_date)
    print(news_title)
    print(news_p)
    print("-"*75)

    browser.quit()

    #JPL Mars Space Images - Featured Image
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    main_url= 'https://spaceimages-mars.com/'
    browser.visit(main_url)
    time.sleep(1)

    # Create a Beautiful Soup object
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    images = soup.find('img', class_='headerimage fade-in')
    image_url = images['src']
    featured_image_url = main_url + image_url
    print(featured_image_url)
    browser.quit()

    # Mars Facts
    fact_url = 'https://galaxyfacts-mars.com/'
    tables = pd.read_html(fact_url)
    df = tables[0]
    df = df.rename(columns= {0:"", 1:"Mars", 2:"Earth"})
    df.iloc[-1] = ["Description","",""]
    html_table= df.to_html()
    html_table = html_table.replace('\n', '')
    df.to_html('table.html')

    # Mars Hemispheres
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    hmsp_url= 'https://marshemispheres.com/'
    browser.visit(hmsp_url)
    time.sleep(1)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup.prettify())

    products = soup.find_all("div", class_ = "item")
    hmsp_img_url = []    

    for product in products:
        title = product.find('h3').text
        item_link = product.find('a')['href']
        final_link = hmsp_url + item_link

        #Click on each link
        browser.visit(final_link)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')

        #Find full image url
        img_link = soup.find_all('img', class_ = 'wide-image')[0]['src']
        img_url = hmsp_url + img_link
    
        hmsp_dict = {'title':title, 'img_url':img_url}
      
        hmsp_img_url.append(hmsp_dict)

    #Find full image url
    img_link = soup.find_all('img', class_ = 'wide-image')[0]['src']
    img_url = hmsp_url + img_link
    
    hmsp_dict = {'title':title, 'img_url':img_url}
      
    hmsp_img_url.append(hmsp_dict)


    mars_news = {
        "news_date": news_date,
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "html_table":html_table,
        "hmsp_img_url":hmsp_img_url
    }

    return mars_news









    














