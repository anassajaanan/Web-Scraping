from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from csv import writer
import requests
import pprint
import time

# =========================================Config================================================
op = Options()
op.add_extension('config/pay.crx')
op.add_extension('config/uorigin.crx')
op.add_extension('config/cockies.crx')
PATH = 'config/chromedriver.exe'
cc = DesiredCapabilities.CHROME
cc["pageLoadStrategy"] = "none"

headers = {
    "Accept-Language": "en-US,en;q=0.5",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}


# =======================================Cryptofinance========================================

def export_cryptofinance():
    ft_url = "https://www.ft.com/cryptofinance"
    response = requests.get(url=ft_url, headers=headers)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')

    articles = soup.find_all('a', {'class': 'js-teaser-heading-link'})
    articles = articles[-25:]
    images = soup.find_all('img', {'class': 'o-teaser__image o-lazy-load'})
    descriptions = soup.find_all('a', {'class': 'js-teaser-standfirst-link'})
    descriptions = descriptions[-25:]

    articles_links = ["https://www.ft.com" + article.get('href') for article in articles]
    articles_images = [image.get('data-src') for image in images]
    titles = [article.text for article in articles]
    articles_descriptions = [description.text for description in descriptions]
    time.sleep(1)

    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    FT_URL = "https://www.ft.com/cryptofinance"
    driver.get(FT_URL)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'js-teaser-heading-link')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(3)

    for i in range(len(articles_links)):
        driver.get(articles_links[i])
        w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
        time.sleep(2)

        try:
            author = driver.find_element(By.CLASS_NAME, 'n-content-tag--author').text
        except:
            author = "NOT FOUND"

        try:
            date = driver.find_element(By.TAG_NAME, 'time').get_attribute('datetime').split("T")[0]
        except:
            date = "NOT FOUND"

        try:
            body = driver.find_element(By.CLASS_NAME, 'article__content-body').find_elements(By.TAG_NAME, 'p')
        except:
            continue
        content = [str(item.text) + "\n" for item in body]
        content = "".join(content)

        with open('Cryptofinance.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [articles_links[i], titles[i], articles_images[i], author, date,
                           articles_descriptions[i], content]

            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_cryptofinance():
    ft_url = "https://www.ft.com/cryptofinance"
    response = requests.get(url=ft_url, headers=headers)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')

    articles = soup.find_all('a', {'class': 'js-teaser-heading-link'})
    articles = articles[-25:]
    images = soup.find_all('img', {'class': 'o-teaser__image o-lazy-load'})
    descriptions = soup.find_all('a', {'class': 'js-teaser-standfirst-link'})
    descriptions = descriptions[-25:]

    articles_links = ["https://www.ft.com" + article.get('href') for article in articles][0]
    articles_images = [image.get('data-src') for image in images][0]
    titles = [article.text for article in articles][0]
    articles_descriptions = [description.text for description in descriptions][0]
    time.sleep(1)

    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    FT_URL = "https://www.ft.com/cryptofinance"
    driver.get(FT_URL)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'js-teaser-heading-link')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(3)

    driver.get(articles_links)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
    time.sleep(2)

    try:
        author = driver.find_element(By.CLASS_NAME, 'n-content-tag--author').text
    except:
        author = "NOT FOUND"

    try:
        date = driver.find_element(By.TAG_NAME, 'time').get_attribute('datetime').split("T")[0]
    except:
        date = "NOT FOUND"

    body = driver.find_element(By.CLASS_NAME, 'article__content-body').find_elements(By.TAG_NAME, 'p')
    content = [str(item.text) + "\n" for item in body]
    content = "".join(content)

    article = {
        "post_category": "Cryptofinance",
        "news_url": articles_links,
        "title": titles,
        "author": author,
        "date": date,
        "image_url": articles_images,
        "description": articles_descriptions,
        "original_text": content,
    }
    pprint.pprint(article)


# =======================================Capital markets========================================

def export_capital_markets():
    capital_markets_url = "https://www.ft.com/capital-markets"
    response = requests.get(url=capital_markets_url, headers=headers)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')

    articles = soup.find_all('a', {'class': 'js-teaser-heading-link'})
    images = soup.find_all('img', {'class': 'o-teaser__image o-lazy-load'})
    descriptions = soup.find_all('a', {'class': 'js-teaser-standfirst-link'})

    articles_links = ["https://www.ft.com" + article.get('href') for article in articles]
    articles_images = [image.get('data-src') for image in images]
    titles = [article.text for article in articles]
    articles_descriptions = [description.text for description in descriptions]
    time.sleep(1)

    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    capital_markets_URL = "https://www.ft.com/capital-markets"
    driver.get(capital_markets_URL)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'js-teaser-heading-link')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(3)

    for i in range(len(articles_links)):
        driver.get(articles_links[i])
        w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
        time.sleep(2)

        try:
            author = driver.find_element(By.CLASS_NAME, 'n-content-tag--author').text
        except:
            author = "NOT FOUND"

        try:
            date = driver.find_element(By.TAG_NAME, 'time').get_attribute('datetime').split("T")[0]
        except:
            date = "NOT FOUND"

        try:
            body = driver.find_element(By.CLASS_NAME, 'article__content-body').find_elements(By.TAG_NAME, 'p')
        except:
            continue
        content = [str(item.text) + "\n" for item in body]
        content = "".join(content)

        with open('Capital markets.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [articles_links[i], titles[i], articles_images[i], author, date,
                           articles_descriptions[i], content]

            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_capital_markets():
    capital_markets_url = "https://www.ft.com/capital-markets"
    response = requests.get(url=capital_markets_url, headers=headers)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')

    articles = soup.find_all('a', {'class': 'js-teaser-heading-link'})
    # articles = articles[-25:]
    images = soup.find_all('img', {'class': 'o-teaser__image o-lazy-load'})
    descriptions = soup.find_all('a', {'class': 'js-teaser-standfirst-link'})
    # descriptions = descriptions[-25:]

    articles_links = ["https://www.ft.com" + article.get('href') for article in articles][0]
    articles_images = [image.get('data-src') for image in images][0]
    titles = [article.text for article in articles][0]
    articles_descriptions = [description.text for description in descriptions][0]
    time.sleep(1)

    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    capital_markets_URL = "https://www.ft.com/capital-markets"
    driver.get(capital_markets_URL)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'js-teaser-heading-link')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(3)

    driver.get(articles_links)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
    time.sleep(2)

    try:
        author = driver.find_element(By.CLASS_NAME, 'n-content-tag--author').text
    except:
        author = "NOT FOUND"

    try:
        date = driver.find_element(By.TAG_NAME, 'time').get_attribute('datetime').split("T")[0]
    except:
        date = "NOT FOUND"

    body = driver.find_element(By.CLASS_NAME, 'article__content-body').find_elements(By.TAG_NAME, 'p')
    content = [str(item.text) + "\n" for item in body]
    content = "".join(content)

    article = {
        "post_category": "Capital markets",
        "news_url": articles_links,
        "title": titles,
        "author": author,
        "date": date,
        "image_url": articles_images,
        "description": articles_descriptions,
        "original_text": content,
    }
    pprint.pprint(article)


# =======================================Commodities========================================

def export_commodities():
    commodities_url = "https://www.ft.com/commodities"
    response = requests.get(url=commodities_url, headers=headers)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')

    articles = soup.find_all('a', {'class': 'js-teaser-heading-link'})
    images = soup.find_all('img', {'class': 'o-teaser__image o-lazy-load'})
    descriptions = soup.find_all('a', {'class': 'js-teaser-standfirst-link'})

    articles_links = ["https://www.ft.com" + article.get('href') for article in articles]
    articles_images = [image.get('data-src') for image in images]
    titles = [article.text for article in articles]
    articles_descriptions = [description.text for description in descriptions]
    time.sleep(1)

    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    commodities_url = "https://www.ft.com/commodities"
    driver.get(commodities_url)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'js-teaser-heading-link')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(3)

    for i in range(len(articles_links)):
        driver.get(articles_links[i])
        w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
        time.sleep(2)

        try:
            author = driver.find_element(By.CLASS_NAME, 'n-content-tag--author').text
        except:
            author = "NOT FOUND"

        try:
            date = driver.find_element(By.TAG_NAME, 'time').get_attribute('datetime').split("T")[0]
        except:
            date = "NOT FOUND"
        try:
            body = driver.find_element(By.CLASS_NAME, 'article__content-body').find_elements(By.TAG_NAME, 'p')
        except:
            continue
        content = [str(item.text) + "\n" for item in body]
        content = "".join(content)

        with open('Commodities.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [articles_links[i], titles[i], articles_images[i], author, date,
                           articles_descriptions[i], content]

            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_commodities():
    commodities_url = "https://www.ft.com/commodities"
    response = requests.get(url=commodities_url, headers=headers)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')

    articles = soup.find_all('a', {'class': 'js-teaser-heading-link'})
    images = soup.find_all('img', {'class': 'o-teaser__image o-lazy-load'})
    descriptions = soup.find_all('a', {'class': 'js-teaser-standfirst-link'})

    articles_links = ["https://www.ft.com" + article.get('href') for article in articles][0]
    articles_images = [image.get('data-src') for image in images][0]
    titles = [article.text for article in articles][0]
    articles_descriptions = [description.text for description in descriptions][0]
    time.sleep(1)

    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    commodities_url = "https://www.ft.com/commodities"
    driver.get(commodities_url)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'js-teaser-heading-link')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(3)

    driver.get(articles_links)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
    time.sleep(2)

    try:
        author = driver.find_element(By.CLASS_NAME, 'n-content-tag--author').text
    except:
        author = "NOT FOUND"

    try:
        date = driver.find_element(By.TAG_NAME, 'time').get_attribute('datetime').split("T")[0]
    except:
        date = "NOT FOUND"

    body = driver.find_element(By.CLASS_NAME, 'article__content-body').find_elements(By.TAG_NAME, 'p')
    content = [str(item.text) + "\n" for item in body]
    content = "".join(content)

    article = {
        "post_category": "Commodities",
        "news_url": articles_links,
        "title": titles,
        "author": author,
        "date": date,
        "image_url": articles_images,
        "description": articles_descriptions,
        "original_text": content,
    }
    pprint.pprint(article)


# =======================================Currencies========================================

def export_currencies():
    currencies_url = "https://www.ft.com/currencies"
    response = requests.get(url=currencies_url, headers=headers)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')

    articles = soup.find_all('a', {'class': 'js-teaser-heading-link'})
    images = soup.find_all('img', {'class': 'o-teaser__image o-lazy-load'})
    descriptions = soup.find_all('a', {'class': 'js-teaser-standfirst-link'})

    articles_links = ["https://www.ft.com" + article.get('href') for article in articles]
    articles_images = [image.get('data-src') for image in images]
    titles = [article.text for article in articles]
    articles_descriptions = [description.text for description in descriptions]
    time.sleep(1)

    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    currencies_url = "https://www.ft.com/currencies"
    driver.get(currencies_url)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'js-teaser-heading-link')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(3)

    for i in range(len(articles_links)):
        driver.get(articles_links[i])
        w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
        time.sleep(2)

        try:
            author = driver.find_element(By.CLASS_NAME, 'n-content-tag--author').text
        except:
            author = "NOT FOUND"

        try:
            date = driver.find_element(By.TAG_NAME, 'time').get_attribute('datetime').split("T")[0]
        except:
            date = "NOT FOUND"
        try:
            body = driver.find_element(By.CLASS_NAME, 'article__content-body').find_elements(By.TAG_NAME, 'p')
        except:
            continue

        def get_text(item):
            try:
                return str(item.text) + "\n"
            except:
                pass

        content = [get_text(item) for item in body]
        content = "".join(content)

        with open('Currencies.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [articles_links[i], titles[i], articles_images[i], author, date,
                           articles_descriptions[i], content]

            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_currencies():
    currencies_url = "https://www.ft.com/currencies"
    response = requests.get(url=currencies_url, headers=headers)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')

    articles = soup.find_all('a', {'class': 'js-teaser-heading-link'})
    images = soup.find_all('img', {'class': 'o-teaser__image o-lazy-load'})
    descriptions = soup.find_all('a', {'class': 'js-teaser-standfirst-link'})

    articles_links = ["https://www.ft.com" + article.get('href') for article in articles][0]
    articles_images = [image.get('data-src') for image in images][0]
    titles = [article.text for article in articles][0]
    articles_descriptions = [description.text for description in descriptions][0]
    time.sleep(1)

    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    currencies_url = "https://www.ft.com/currencies"
    driver.get(currencies_url)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'js-teaser-heading-link')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(3)

    driver.get(articles_links)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
    time.sleep(2)

    try:
        author = driver.find_element(By.CLASS_NAME, 'n-content-tag--author').text
    except:
        author = "NOT FOUND"

    try:
        date = driver.find_element(By.TAG_NAME, 'time').get_attribute('datetime').split("T")[0]
    except:
        date = "NOT FOUND"

    body = driver.find_element(By.CLASS_NAME, 'article__content-body').find_elements(By.TAG_NAME, 'p')
    content = [str(item.text) + "\n" for item in body]
    content = "".join(content)

    article = {
        "post_category": "Currencies",
        "news_url": articles_links,
        "title": titles,
        "author": author,
        "date": date,
        "image_url": articles_images,
        "description": articles_descriptions,
        "original_text": content,
    }
    pprint.pprint(article)


# =======================================Equities========================================


def export_equities():
    equities_url = "https://www.ft.com/equities"
    response = requests.get(url=equities_url, headers=headers)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')

    articles = soup.find_all('a', {'class': 'js-teaser-heading-link'})
    images = soup.find_all('img', {'class': 'o-teaser__image o-lazy-load'})
    descriptions = soup.find_all('a', {'class': 'js-teaser-standfirst-link'})

    articles_links = ["https://www.ft.com" + article.get('href') for article in articles]
    articles_images = [image.get('data-src') for image in images]
    titles = [article.text for article in articles]
    articles_descriptions = [description.text for description in descriptions]
    time.sleep(1)

    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    equities_url = "https://www.ft.com/equities"
    driver.get(equities_url)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'js-teaser-heading-link')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(3)

    for i in range(len(articles_links)):
        driver.get(articles_links[i])
        w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
        time.sleep(2)

        try:
            author = driver.find_element(By.CLASS_NAME, 'n-content-tag--author').text
        except:
            author = "NOT FOUND"

        try:
            date = driver.find_element(By.TAG_NAME, 'time').get_attribute('datetime').split("T")[0]
        except:
            date = "NOT FOUND"
        try:
            body = driver.find_element(By.CLASS_NAME, 'article__content-body').find_elements(By.TAG_NAME, 'p')
        except:
            continue

        def get_text(item):
            try:
                return str(item.text) + "\n"
            except:
                pass

        content = [get_text(item) for item in body]
        content = "".join(content)

        with open('Equities.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [articles_links[i], titles[i], articles_images[i], author, date,
                           articles_descriptions[i], content]

            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_equities():
    equities_url = "https://www.ft.com/equities"
    response = requests.get(url=equities_url, headers=headers)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')

    articles = soup.find_all('a', {'class': 'js-teaser-heading-link'})
    images = soup.find_all('img', {'class': 'o-teaser__image o-lazy-load'})
    descriptions = soup.find_all('a', {'class': 'js-teaser-standfirst-link'})

    articles_links = ["https://www.ft.com" + article.get('href') for article in articles][0]
    articles_images = [image.get('data-src') for image in images][0]
    titles = [article.text for article in articles][0]
    articles_descriptions = [description.text for description in descriptions][0]
    time.sleep(1)

    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    equities_url = "https://www.ft.com/equities"
    driver.get(equities_url)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'js-teaser-heading-link')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(3)

    driver.get(articles_links)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
    time.sleep(2)

    try:
        author = driver.find_element(By.CLASS_NAME, 'n-content-tag--author').text
    except:
        author = "NOT FOUND"

    try:
        date = driver.find_element(By.TAG_NAME, 'time').get_attribute('datetime').split("T")[0]
    except:
        date = "NOT FOUND"

    body = driver.find_element(By.CLASS_NAME, 'article__content-body').find_elements(By.TAG_NAME, 'p')
    content = [str(item.text) + "\n" for item in body]
    content = "".join(content)

    article = {
        "post_category": "Equities",
        "news_url": articles_links,
        "title": titles,
        "author": author,
        "date": date,
        "image_url": articles_images,
        "description": articles_descriptions,
        "original_text": content,
    }
    pprint.pprint(article)


# =======================================Fund management========================================


def export_fund_management():
    fund_management_url = "https://www.ft.com/fund-management"
    response = requests.get(url=fund_management_url, headers=headers)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')

    articles = soup.find_all('a', {'class': 'js-teaser-heading-link'})
    articles = articles[-25:]
    images = soup.find_all('img', {'class': 'o-teaser__image o-lazy-load'})
    descriptions = soup.find_all('a', {'class': 'js-teaser-standfirst-link'})
    descriptions = descriptions[-25:]

    articles_links = ["https://www.ft.com" + article.get('href') for article in articles]
    articles_images = [image.get('data-src') for image in images]
    titles = [article.text for article in articles]
    articles_descriptions = [description.text for description in descriptions]
    time.sleep(1)

    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    fund_management_url = "https://www.ft.com/fund-management"
    driver.get(fund_management_url)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'js-teaser-heading-link')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(3)

    for i in range(len(articles_links)):
        driver.get(articles_links[i])
        w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
        time.sleep(2)

        try:
            author = driver.find_element(By.CLASS_NAME, 'n-content-tag--author').text
        except:
            author = "NOT FOUND"

        try:
            date = driver.find_element(By.TAG_NAME, 'time').get_attribute('datetime').split("T")[0]
        except:
            date = "NOT FOUND"
        try:
            body = driver.find_element(By.CLASS_NAME, 'article__content-body').find_elements(By.TAG_NAME, 'p')
        except:
            continue

        def get_text(item):
            try:
                return str(item.text) + "\n"
            except:
                pass

        content = [get_text(item) for item in body]
        content = "".join(content)

        with open('Fund management.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [articles_links[i], titles[i], articles_images[i], author, date,
                           articles_descriptions[i], content]

            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_fund_management():
    fund_management_url = "https://www.ft.com/fund-management"
    response = requests.get(url=fund_management_url, headers=headers)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')

    articles = soup.find_all('a', {'class': 'js-teaser-heading-link'})
    articles = articles[-25:]
    images = soup.find_all('img', {'class': 'o-teaser__image o-lazy-load'})
    descriptions = soup.find_all('a', {'class': 'js-teaser-standfirst-link'})
    descriptions = descriptions[-25:]

    articles_links = ["https://www.ft.com" + article.get('href') for article in articles][0]
    articles_images = [image.get('data-src') for image in images][0]
    titles = [article.text for article in articles][0]
    articles_descriptions = [description.text for description in descriptions][0]
    time.sleep(1)

    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    fund_management_url = "https://www.ft.com/fund-management"
    driver.get(fund_management_url)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'js-teaser-heading-link')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(3)

    driver.get(articles_links)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
    time.sleep(2)

    try:
        author = driver.find_element(By.CLASS_NAME, 'n-content-tag--author').text
    except:
        author = "NOT FOUND"

    try:
        date = driver.find_element(By.TAG_NAME, 'time').get_attribute('datetime').split("T")[0]
    except:
        date = "NOT FOUND"

    body = driver.find_element(By.CLASS_NAME, 'article__content-body').find_elements(By.TAG_NAME, 'p')
    content = [str(item.text) + "\n" for item in body]
    content = "".join(content)

    article = {
        "post_category": "Fund management",
        "news_url": articles_links,
        "title": titles,
        "author": author,
        "date": date,
        "image_url": articles_images,
        "description": articles_descriptions,
        "original_text": content,
    }
    pprint.pprint(article)


# =======================================Trading========================================


def export_trading():
    trading_url = "https://www.ft.com/ft-trading-room"
    response = requests.get(url=trading_url, headers=headers)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')

    articles = soup.find_all('a', {'class': 'js-teaser-heading-link'})
    articles = articles[-25:]
    images = soup.find_all('img', {'class': 'o-teaser__image o-lazy-load'})
    descriptions = soup.find_all('a', {'class': 'js-teaser-standfirst-link'})
    descriptions = descriptions[-25:]

    articles_links = ["https://www.ft.com" + article.get('href') for article in articles]
    articles_images = [image.get('data-src') for image in images]
    titles = [article.text for article in articles]
    articles_descriptions = [description.text for description in descriptions]
    time.sleep(1)

    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    trading_url = "https://www.ft.com/ft-trading-room"
    driver.get(trading_url)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'js-teaser-heading-link')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(3)

    for i in range(len(articles_links)):
        driver.get(articles_links[i])
        w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
        time.sleep(2)

        try:
            author = driver.find_element(By.CLASS_NAME, 'n-content-tag--author').text
        except:
            author = "NOT FOUND"

        try:
            date = driver.find_element(By.TAG_NAME, 'time').get_attribute('datetime').split("T")[0]
        except:
            date = "NOT FOUND"
        try:
            body = driver.find_element(By.CLASS_NAME, 'article__content-body').find_elements(By.TAG_NAME, 'p')
        except:
            continue

        def get_text(item):
            try:
                return str(item.text) + "\n"
            except:
                pass

        content = [get_text(item) for item in body]
        content = "".join(content)

        with open('Trading.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [articles_links[i], titles[i], articles_images[i], author, date,
                           articles_descriptions[i], content]

            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_trading():
    trading_url = "https://www.ft.com/ft-trading-room"
    response = requests.get(url=trading_url, headers=headers)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')

    articles = soup.find_all('a', {'class': 'js-teaser-heading-link'})
    articles = articles[-25:]
    images = soup.find_all('img', {'class': 'o-teaser__image o-lazy-load'})
    descriptions = soup.find_all('a', {'class': 'js-teaser-standfirst-link'})
    descriptions = descriptions[-25:]

    articles_links = ["https://www.ft.com" + article.get('href') for article in articles][0]
    articles_images = [image.get('data-src') for image in images][0]
    titles = [article.text for article in articles][0]
    articles_descriptions = [description.text for description in descriptions][0]
    time.sleep(1)

    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    trading_url = "https://www.ft.com/ft-trading-room"
    driver.get(trading_url)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'js-teaser-heading-link')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(3)

    driver.get(articles_links)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
    time.sleep(2)

    try:
        author = driver.find_element(By.CLASS_NAME, 'n-content-tag--author').text
    except:
        author = "NOT FOUND"

    try:
        date = driver.find_element(By.TAG_NAME, 'time').get_attribute('datetime').split("T")[0]
    except:
        date = "NOT FOUND"

    body = driver.find_element(By.CLASS_NAME, 'article__content-body').find_elements(By.TAG_NAME, 'p')
    content = [str(item.text) + "\n" for item in body]
    content = "".join(content)

    article = {
        "post_category": "Trading",
        "news_url": articles_links,
        "title": titles,
        "author": author,
        "date": date,
        "image_url": articles_images,
        "description": articles_descriptions,
        "original_text": content,
    }
    pprint.pprint(article)


# ============================================Run Functions=====================================
