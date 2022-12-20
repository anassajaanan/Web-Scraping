from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from csv import writer
import pprint
import time

# ================config====================
op = Options()
op.add_extension('config/pay.crx')
op.add_extension('config/uorigin.crx')
op.add_extension('config/cockies.crx')
PATH = 'config/chromedriver.exe'
cc = DesiredCapabilities.CHROME
cc["pageLoadStrategy"] = "none"


# ===================================CRYPTOCURRENCY=============================================
def export_cryptocurrency():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    CRYPTOCURRENCY_URL = "https://www.wsj.com/news/types/crypto?mod=breadcrumb"
    driver.get(CRYPTOCURRENCY_URL)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'WSJTheme--headline--unZqjb45')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(5)

    images = driver.find_elements(By.CLASS_NAME, 'WSJTheme--image--At42misj')
    links = driver.find_elements(By.CLASS_NAME, 'WSJTheme--headline--unZqjb45')

    articles_imgs = [image.get_attribute('src') for image in images]
    articles_links = [link.find_element(By.TAG_NAME, 'a').get_attribute('href') for link in links]

    # print(articles_imgs)
    # print(articles_links)

    time.sleep(2)

    for i in range(len(articles_links)):
        driver.get(articles_links[i])
        w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
        time.sleep(2)
        try:
            title = driver.find_element(By.CLASS_NAME, 'css-1lvqw7f-StyledHeadline').text
        except:
            title = driver.find_element(By.TAG_NAME, 'h1').text
        try:
            author = driver.find_element(By.CLASS_NAME, 'css-nyr2iw-AuthorContainer').find_element(By.TAG_NAME,
                                                                                                   'a').text
        except:
            author = "Not Found"
        date = driver.find_element(By.TAG_NAME, 'time').text
        try:
            type = driver.find_element(By.CLASS_NAME, 'css-e8qa5r-Link').text
        except:
            type = "Not Found"

        content = driver.find_elements(By.CLASS_NAME, 'css-xbvutc-Paragraph')
        content = [str(item.text) + "\n" for item in content]
        content = "".join(content)
        try:
            article_description = driver.find_element(By.CLASS_NAME, 'css-mosdo-Dek-Dek').text
        except:
            article_description = driver.find_element(By.TAG_NAME, 'h2')

        with open('cryptocurrency.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [articles_links[i], title, articles_imgs[i], author, date, type, article_description, content]
            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_cryptocurrency():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    CRYPTOCURRENCY_URL = "https://www.wsj.com/news/types/crypto?mod=breadcrumb"
    driver.get(CRYPTOCURRENCY_URL)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'WSJTheme--headline--unZqjb45')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(5)

    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'WSJTheme--image--At42misj')))
    articles_imgs = driver.find_element(By.CLASS_NAME, 'WSJTheme--image--At42misj').get_attribute('src')
    articles_links = driver.find_element(By.CLASS_NAME, 'WSJTheme--headline--unZqjb45').find_element(By.TAG_NAME,
                                                                                                     'a').get_attribute(
        'href')
    time.sleep(2)

    driver.get(articles_links)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
    time.sleep(2)
    try:
        title = driver.find_element(By.CLASS_NAME, 'css-1lvqw7f-StyledHeadline').text
    except:
        title = driver.find_element(By.TAG_NAME, 'h1').text
    try:
        author = driver.find_element(By.CLASS_NAME, 'css-nyr2iw-AuthorContainer').find_element(By.TAG_NAME,
                                                                                               'a').text
    except:
        author = "Not Found"
    date = driver.find_element(By.TAG_NAME, 'time').text
    try:
        type = driver.find_element(By.CLASS_NAME, 'css-e8qa5r-Link').text
    except:
        type = "Not Found"

    content = driver.find_elements(By.CLASS_NAME, 'css-xbvutc-Paragraph')
    content = [str(item.text) + "\n" for item in content]
    content = "".join(content)
    try:
        article_description = driver.find_element(By.CLASS_NAME, 'css-mosdo-Dek-Dek').text
    except:
        article_description = driver.find_element(By.TAG_NAME, 'h2')

    article = {
        "post_category": type,
        "news_url": articles_links,
        "title": title,
        "author": author,
        "date": date,
        "image_url": articles_imgs,
        "description": article_description,
        "original_text": content,
    }
    pprint.pprint(article)


# ===================================FOREIGN EXCHANGE=============================================
def export_foreign_exchange():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    FOREIGN_EXCHANGE_URL = "https://www.wsj.com/news/types/foreign-exchange"
    driver.get(FOREIGN_EXCHANGE_URL)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'WSJTheme--headline--unZqjb45')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(5)

    images = driver.find_elements(By.CLASS_NAME, 'WSJTheme--image--At42misj')
    links = driver.find_elements(By.CLASS_NAME, 'WSJTheme--headline--unZqjb45')

    articles_imgs = [image.get_attribute('src') for image in images]
    articles_links = [link.find_element(By.TAG_NAME, 'a').get_attribute('href') for link in links]

    # print(articles_imgs)
    # print(articles_links)

    time.sleep(2)

    for i in range(len(articles_links)):
        driver.get(articles_links[i])
        w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
        time.sleep(2)
        try:
            title = driver.find_element(By.CLASS_NAME, 'css-1lvqw7f-StyledHeadline').text
        except:
            title = driver.find_element(By.TAG_NAME, 'h1').text
        try:
            author = driver.find_element(By.CLASS_NAME, 'css-nyr2iw-AuthorContainer').find_element(By.TAG_NAME,
                                                                                                   'a').text
        except:
            author = "Not Found"
        date = driver.find_element(By.TAG_NAME, 'time').text
        try:
            type = driver.find_element(By.CLASS_NAME, 'css-e8qa5r-Link').text
        except:
            type = "Not Found"

        content = driver.find_elements(By.CLASS_NAME, 'css-xbvutc-Paragraph')
        content = [str(item.text) + "\n" for item in content]
        content = "".join(content)
        try:
            article_description = driver.find_element(By.CLASS_NAME, 'css-mosdo-Dek-Dek').text
        except:
            article_description = driver.find_element(By.TAG_NAME, 'h2')

        with open('foreign_exchange.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [articles_links[i], title, articles_imgs[i], author, date, type, article_description, content]
            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_foreign_exchange():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    FOREIGN_EXCHANGE_URL = "https://www.wsj.com/news/types/foreign-exchange"
    driver.get(FOREIGN_EXCHANGE_URL)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'WSJTheme--headline--unZqjb45')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(5)

    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'WSJTheme--image--At42misj')))
    articles_imgs = driver.find_element(By.CLASS_NAME, 'WSJTheme--image--At42misj').get_attribute('src')
    articles_links = driver.find_element(By.CLASS_NAME, 'WSJTheme--headline--unZqjb45').find_element(By.TAG_NAME,
                                                                                                     'a').get_attribute(
        'href')
    time.sleep(2)

    driver.get(articles_links)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
    time.sleep(2)
    try:
        title = driver.find_element(By.CLASS_NAME, 'css-1lvqw7f-StyledHeadline').text
    except:
        title = driver.find_element(By.TAG_NAME, 'h1').text
    try:
        author = driver.find_element(By.CLASS_NAME, 'css-nyr2iw-AuthorContainer').find_element(By.TAG_NAME,
                                                                                               'a').text
    except:
        author = "Not Found"
    date = driver.find_element(By.TAG_NAME, 'time').text
    try:
        type = driver.find_element(By.CLASS_NAME, 'css-e8qa5r-Link').text
    except:
        type = "Not Found"

    content = driver.find_elements(By.CLASS_NAME, 'css-xbvutc-Paragraph')
    content = [str(item.text) + "\n" for item in content]
    content = "".join(content)
    try:
        article_description = driver.find_element(By.CLASS_NAME, 'css-mosdo-Dek-Dek').text
    except:
        article_description = driver.find_element(By.TAG_NAME, 'h2')

    article = {
        "post_category": type,
        "news_url": articles_links,
        "title": title,
        "author": author,
        "date": date,
        "image_url": articles_imgs,
        "description": article_description,
        "original_text": content,
    }
    pprint.pprint(article)


# ===================================Bonds=============================================

def export_bonds():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    BONDS_URL = "https://www.wsj.com/news/markets/bonds?mod=nav_top_subsection"
    driver.get(BONDS_URL)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'WSJTheme--headline--unZqjb45')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(5)

    images = driver.find_elements(By.CLASS_NAME, 'WSJTheme--image--At42misj')
    links = driver.find_elements(By.CLASS_NAME, 'WSJTheme--headline--unZqjb45')

    articles_imgs = [image.get_attribute('src') for image in images]
    articles_links = [link.find_element(By.TAG_NAME, 'a').get_attribute('href') for link in links]

    # print(articles_imgs)
    # print(articles_links)

    time.sleep(2)

    for i in range(len(articles_links)):
        driver.get(articles_links[i])
        w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
        time.sleep(2)
        try:
            title = driver.find_element(By.CLASS_NAME, 'css-1lvqw7f-StyledHeadline').text
        except:
            title = driver.find_element(By.TAG_NAME, 'h1').text
        try:
            author = driver.find_element(By.CLASS_NAME, 'css-nyr2iw-AuthorContainer').find_element(By.TAG_NAME,
                                                                                                   'a').text
        except:
            author = "Not Found"
        date = driver.find_element(By.TAG_NAME, 'time').text
        try:
            type = driver.find_element(By.CLASS_NAME, 'css-e8qa5r-Link').text
        except:
            type = "Not Found"

        content = driver.find_elements(By.CLASS_NAME, 'css-xbvutc-Paragraph')
        content = [str(item.text) + "\n" for item in content]
        content = "".join(content)
        try:
            article_description = driver.find_element(By.CLASS_NAME, 'css-mosdo-Dek-Dek').text
        except:
            article_description = driver.find_element(By.TAG_NAME, 'h2')

        with open('bonds.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [articles_links[i], title, articles_imgs[i], author, date, type, article_description, content]
            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_bonds():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    BONDS_URL = "https://www.wsj.com/news/markets/bonds?mod=nav_top_subsection"
    driver.get(BONDS_URL)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'WSJTheme--headline--unZqjb45')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(5)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'WSJTheme--image--At42misj')))
    articles_imgs = driver.find_element(By.CLASS_NAME, 'WSJTheme--image--At42misj').get_attribute('src')
    articles_links = driver.find_element(By.CLASS_NAME, 'WSJTheme--headline--unZqjb45').find_element(By.TAG_NAME,
                                                                                                     'a').get_attribute(
        'href')
    time.sleep(2)

    driver.get(articles_links)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
    time.sleep(2)
    try:
        title = driver.find_element(By.CLASS_NAME, 'css-1lvqw7f-StyledHeadline').text
    except:
        title = driver.find_element(By.TAG_NAME, 'h1').text
    try:
        author = driver.find_element(By.CLASS_NAME, 'css-nyr2iw-AuthorContainer').find_element(By.TAG_NAME,
                                                                                               'a').text
    except:
        author = "Not Found"
    date = driver.find_element(By.TAG_NAME, 'time').text
    try:
        type = driver.find_element(By.CLASS_NAME, 'css-e8qa5r-Link').text
    except:
        type = "Not Found"

    content = driver.find_elements(By.CLASS_NAME, 'css-xbvutc-Paragraph')
    content = [str(item.text) + "\n" for item in content]
    content = "".join(content)
    try:
        article_description = driver.find_element(By.CLASS_NAME, 'css-mosdo-Dek-Dek').text
    except:
        article_description = driver.find_element(By.TAG_NAME, 'h2')

    article = {
        "post_category": type,
        "news_url": articles_links,
        "title": title,
        "author": author,
        "date": date,
        "image_url": articles_imgs,
        "description": article_description,
        "original_text": content,
    }
    pprint.pprint(article)


# ===================================Commercial Real Estate=============================================
def export_commercial_real_estate():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    Commercial_Real_Estate_URL = "https://www.wsj.com/news/markets/real-estate-commercial?mod=nav_top_subsection"
    driver.get(Commercial_Real_Estate_URL)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'WSJTheme--headline--unZqjb45')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(5)

    images = driver.find_elements(By.CLASS_NAME, 'WSJTheme--image--At42misj')
    links = driver.find_elements(By.CLASS_NAME, 'WSJTheme--headline--unZqjb45')

    articles_imgs = [image.get_attribute('src') for image in images]
    articles_links = [link.find_element(By.TAG_NAME, 'a').get_attribute('href') for link in links]

    # print(articles_imgs)
    # print(articles_links)

    time.sleep(2)

    for i in range(len(articles_links)):
        driver.get(articles_links[i])
        w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
        time.sleep(2)
        try:
            title = driver.find_element(By.CLASS_NAME, 'css-1lvqw7f-StyledHeadline').text
        except:
            title = driver.find_element(By.TAG_NAME, 'h1').text
        try:
            author = driver.find_element(By.CLASS_NAME, 'css-nyr2iw-AuthorContainer').find_element(By.TAG_NAME,
                                                                                                   'a').text
        except:
            author = "Not Found"
        date = driver.find_element(By.TAG_NAME, 'time').text
        try:
            type = driver.find_element(By.CLASS_NAME, 'css-e8qa5r-Link').text
        except:
            type = "Not Found"

        content = driver.find_elements(By.CLASS_NAME, 'css-xbvutc-Paragraph')
        content = [str(item.text) + "\n" for item in content]
        content = "".join(content)
        try:
            article_description = driver.find_element(By.CLASS_NAME, 'css-mosdo-Dek-Dek').text
        except:
            article_description = driver.find_element(By.TAG_NAME, 'h2')

        with open('commercial_real_estate.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [articles_links[i], title, articles_imgs[i], author, date, type, article_description, content]
            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_commercial_real_estate():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    Commercial_Real_Estate_URL = "https://www.wsj.com/news/markets/real-estate-commercial?mod=nav_top_subsection"
    driver.get(Commercial_Real_Estate_URL)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'WSJTheme--headline--unZqjb45')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(5)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'WSJTheme--image--At42misj')))
    articles_imgs = driver.find_element(By.CLASS_NAME, 'WSJTheme--image--At42misj').get_attribute('src')
    articles_links = driver.find_element(By.CLASS_NAME, 'WSJTheme--headline--unZqjb45').find_element(By.TAG_NAME,
                                                                                                     'a').get_attribute(
        'href')
    time.sleep(2)

    driver.get(articles_links)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
    time.sleep(2)
    try:
        title = driver.find_element(By.CLASS_NAME, 'css-1lvqw7f-StyledHeadline').text
    except:
        title = driver.find_element(By.TAG_NAME, 'h1').text
    try:
        author = driver.find_element(By.CLASS_NAME, 'css-nyr2iw-AuthorContainer').find_element(By.TAG_NAME,
                                                                                               'a').text
    except:
        author = "Not Found"
    date = driver.find_element(By.TAG_NAME, 'time').text
    try:
        type = driver.find_element(By.CLASS_NAME, 'css-e8qa5r-Link').text
    except:
        type = "Not Found"

    content = driver.find_elements(By.CLASS_NAME, 'css-xbvutc-Paragraph')
    content = [str(item.text) + "\n" for item in content]
    content = "".join(content)
    try:
        article_description = driver.find_element(By.CLASS_NAME, 'css-mosdo-Dek-Dek').text
    except:
        article_description = driver.find_element(By.TAG_NAME, 'h2')

    article = {
        "post_category": type,
        "news_url": articles_links,
        "title": title,
        "author": author,
        "date": date,
        "image_url": articles_imgs,
        "description": article_description,
        "original_text": content,
    }
    pprint.pprint(article)


# ===================================Commodities & Futures=============================================
def export_commodities_futures():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    Commodities_Futures_URL = "https://www.wsj.com/news/markets/oil-gold-commodities-futures?mod=nav_top_subsection"
    driver.get(Commodities_Futures_URL)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'WSJTheme--headline--unZqjb45')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(5)

    images = driver.find_elements(By.CLASS_NAME, 'WSJTheme--image--At42misj')
    links = driver.find_elements(By.CLASS_NAME, 'WSJTheme--headline--unZqjb45')

    articles_imgs = [image.get_attribute('src') for image in images]
    articles_links = [link.find_element(By.TAG_NAME, 'a').get_attribute('href') for link in links]

    # print(articles_imgs)
    # print(articles_links)

    time.sleep(2)

    for i in range(len(articles_links)):
        driver.get(articles_links[i])
        w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
        time.sleep(2)
        try:
            title = driver.find_element(By.CLASS_NAME, 'css-1lvqw7f-StyledHeadline').text
        except:
            title = driver.find_element(By.TAG_NAME, 'h1').text
        try:
            author = driver.find_element(By.CLASS_NAME, 'css-nyr2iw-AuthorContainer').find_element(By.TAG_NAME,
                                                                                                   'a').text
        except:
            author = "Not Found"
        date = driver.find_element(By.TAG_NAME, 'time').text
        try:
            type = driver.find_element(By.CLASS_NAME, 'css-e8qa5r-Link').text
        except:
            type = "Not Found"

        content = driver.find_elements(By.CLASS_NAME, 'css-xbvutc-Paragraph')
        content = [str(item.text) + "\n" for item in content]
        content = "".join(content)
        try:
            article_description = driver.find_element(By.CLASS_NAME, 'css-mosdo-Dek-Dek').text
        except:
            article_description = driver.find_element(By.TAG_NAME, 'h2')

        with open('commodities_futures.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [articles_links[i], title, articles_imgs[i], author, date, type, article_description, content]
            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_commodities_futures():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    Commodities_Futures_URL = "https://www.wsj.com/news/markets/oil-gold-commodities-futures?mod=nav_top_subsection"
    driver.get(Commodities_Futures_URL)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'WSJTheme--headline--unZqjb45')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(5)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'WSJTheme--image--At42misj')))
    articles_imgs = driver.find_element(By.CLASS_NAME, 'WSJTheme--image--At42misj').get_attribute('src')
    articles_links = driver.find_element(By.CLASS_NAME, 'WSJTheme--headline--unZqjb45').find_element(By.TAG_NAME,
                                                                                                     'a').get_attribute(
        'href')
    time.sleep(2)

    driver.get(articles_links)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
    time.sleep(2)
    try:
        title = driver.find_element(By.CLASS_NAME, 'css-1lvqw7f-StyledHeadline').text
    except:
        title = driver.find_element(By.TAG_NAME, 'h1').text
    try:
        author = driver.find_element(By.CLASS_NAME, 'css-nyr2iw-AuthorContainer').find_element(By.TAG_NAME,
                                                                                               'a').text
    except:
        author = "Not Found"
    date = driver.find_element(By.TAG_NAME, 'time').text
    try:
        type = driver.find_element(By.CLASS_NAME, 'css-e8qa5r-Link').text
    except:
        type = "Not Found"

    content = driver.find_elements(By.CLASS_NAME, 'css-xbvutc-Paragraph')
    content = [str(item.text) + "\n" for item in content]
    content = "".join(content)
    try:
        article_description = driver.find_element(By.CLASS_NAME, 'css-mosdo-Dek-Dek').text
    except:
        article_description = driver.find_element(By.TAG_NAME, 'h2')

    article = {
        "post_category": type,
        "news_url": articles_links,
        "title": title,
        "author": author,
        "date": date,
        "image_url": articles_imgs,
        "description": article_description,
        "original_text": content,
    }
    pprint.pprint(article)


# ===================================Stocks=============================================
def export_stocks():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    Stocks_URL = "https://www.wsj.com/news/markets/stocks?mod=nav_top_subsection"
    driver.get(Stocks_URL)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'WSJTheme--headline--unZqjb45')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(5)

    images = driver.find_elements(By.CLASS_NAME, 'WSJTheme--image--At42misj')
    links = driver.find_elements(By.CLASS_NAME, 'WSJTheme--headline--unZqjb45')

    articles_imgs = [image.get_attribute('src') for image in images]
    articles_links = [link.find_element(By.TAG_NAME, 'a').get_attribute('href') for link in links]

    # print(articles_imgs)
    # print(articles_links)

    time.sleep(2)

    for i in range(len(articles_links)):
        driver.get(articles_links[i])
        w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
        time.sleep(2)
        try:
            title = driver.find_element(By.CLASS_NAME, 'css-1lvqw7f-StyledHeadline').text
        except:
            title = driver.find_element(By.TAG_NAME, 'h1').text
        try:
            author = driver.find_element(By.CLASS_NAME, 'css-nyr2iw-AuthorContainer').find_element(By.TAG_NAME,
                                                                                                   'a').text
        except:
            author = "Not Found"
        date = driver.find_element(By.TAG_NAME, 'time').text
        try:
            type = driver.find_element(By.CLASS_NAME, 'css-e8qa5r-Link').text
        except:
            type = "Not Found"

        content = driver.find_elements(By.CLASS_NAME, 'css-xbvutc-Paragraph')
        content = [str(item.text) + "\n" for item in content]
        content = "".join(content)
        try:
            article_description = driver.find_element(By.CLASS_NAME, 'css-mosdo-Dek-Dek').text
        except:
            article_description = driver.find_element(By.TAG_NAME, 'h2')

        with open('stocks.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [articles_links[i], title, articles_imgs[i], author, date, type, article_description, content]
            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_stocks():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    Stocks_URL = "https://www.wsj.com/news/markets/stocks?mod=nav_top_subsection"
    driver.get(Stocks_URL)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'WSJTheme--headline--unZqjb45')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(5)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'WSJTheme--image--At42misj')))
    articles_imgs = driver.find_element(By.CLASS_NAME, 'WSJTheme--image--At42misj').get_attribute('src')
    articles_links = driver.find_element(By.CLASS_NAME, 'WSJTheme--headline--unZqjb45').find_element(By.TAG_NAME,
                                                                                                     'a').get_attribute(
        'href')
    time.sleep(2)

    driver.get(articles_links)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
    time.sleep(2)
    try:
        title = driver.find_element(By.CLASS_NAME, 'css-1lvqw7f-StyledHeadline').text
    except:
        title = driver.find_element(By.TAG_NAME, 'h1').text
    try:
        author = driver.find_element(By.CLASS_NAME, 'css-nyr2iw-AuthorContainer').find_element(By.TAG_NAME,
                                                                                               'a').text
    except:
        author = "Not Found"
    date = driver.find_element(By.TAG_NAME, 'time').text
    try:
        type = driver.find_element(By.CLASS_NAME, 'css-e8qa5r-Link').text
    except:
        type = "Not Found"

    content = driver.find_elements(By.CLASS_NAME, 'css-xbvutc-Paragraph')
    content = [str(item.text) + "\n" for item in content]
    content = "".join(content)
    try:
        article_description = driver.find_element(By.CLASS_NAME, 'css-mosdo-Dek-Dek').text
    except:
        article_description = driver.find_element(By.TAG_NAME, 'h2')

    article = {
        "post_category": type,
        "news_url": articles_links,
        "title": title,
        "author": author,
        "date": date,
        "image_url": articles_imgs,
        "description": article_description,
        "original_text": content,
    }
    pprint.pprint(article)


# ===================================Personal Finance=============================================
def export_personal_finance():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    Personal_Finance_URL = "https://www.wsj.com/news/types/personal-finance?mod=nav_top_subsection"
    driver.get(Personal_Finance_URL)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'WSJTheme--headline--unZqjb45')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(5)

    images = driver.find_elements(By.CLASS_NAME, 'WSJTheme--image--At42misj')
    links = driver.find_elements(By.CLASS_NAME, 'WSJTheme--headline--unZqjb45')

    articles_imgs = [image.get_attribute('src') for image in images]
    articles_links = [link.find_element(By.TAG_NAME, 'a').get_attribute('href') for link in links]

    # print(articles_imgs)
    # print(articles_links)

    time.sleep(2)

    for i in range(len(articles_links)):
        driver.get(articles_links[i])
        w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
        time.sleep(2)
        try:
            title = driver.find_element(By.CLASS_NAME, 'css-1lvqw7f-StyledHeadline').text
        except:
            title = driver.find_element(By.TAG_NAME, 'h1').text
        try:
            author = driver.find_element(By.CLASS_NAME, 'css-nyr2iw-AuthorContainer').find_element(By.TAG_NAME,
                                                                                                   'a').text
        except:
            author = "Not Found"
        date = driver.find_element(By.TAG_NAME, 'time').text
        try:
            type = driver.find_element(By.CLASS_NAME, 'css-e8qa5r-Link').text
        except:
            type = "Not Found"

        content = driver.find_elements(By.CLASS_NAME, 'css-xbvutc-Paragraph')
        content = [str(item.text) + "\n" for item in content]
        content = "".join(content)
        try:
            article_description = driver.find_element(By.CLASS_NAME, 'css-mosdo-Dek-Dek').text
        except:
            article_description = driver.find_element(By.TAG_NAME, 'h2')

        with open('personal_finance.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [articles_links[i], title, articles_imgs[i], author, date, type, article_description, content]
            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_personal_finance():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    Personal_Finance_URL = "https://www.wsj.com/news/types/personal-finance?mod=nav_top_subsection"
    driver.get(Personal_Finance_URL)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'WSJTheme--headline--unZqjb45')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(5)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'WSJTheme--image--At42misj')))
    articles_imgs = driver.find_element(By.CLASS_NAME, 'WSJTheme--image--At42misj').get_attribute('src')
    articles_links = driver.find_element(By.CLASS_NAME, 'WSJTheme--headline--unZqjb45').find_element(By.TAG_NAME,
                                                                                                     'a').get_attribute(
        'href')
    time.sleep(2)

    driver.get(articles_links)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
    time.sleep(2)
    try:
        title = driver.find_element(By.CLASS_NAME, 'css-1lvqw7f-StyledHeadline').text
    except:
        title = driver.find_element(By.TAG_NAME, 'h1').text
    try:
        author = driver.find_element(By.CLASS_NAME, 'css-nyr2iw-AuthorContainer').find_element(By.TAG_NAME,
                                                                                               'a').text
    except:
        author = "Not Found"
    date = driver.find_element(By.TAG_NAME, 'time').text
    try:
        type = driver.find_element(By.CLASS_NAME, 'css-e8qa5r-Link').text
    except:
        type = "Not Found"

    content = driver.find_elements(By.CLASS_NAME, 'css-xbvutc-Paragraph')
    content = [str(item.text) + "\n" for item in content]
    content = "".join(content)
    try:
        article_description = driver.find_element(By.CLASS_NAME, 'css-mosdo-Dek-Dek').text
    except:
        article_description = driver.find_element(By.TAG_NAME, 'h2')

    article = {
        "post_category": type,
        "news_url": articles_links,
        "title": title,
        "author": author,
        "date": date,
        "image_url": articles_imgs,
        "description": article_description,
        "original_text": content,
    }
    pprint.pprint(article)


# ===================================STREETWISE=============================================
def export_streetwise():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    STREETWISE_URL = "https://www.wsj.com/news/types/streetwise?mod=nav_top_subsection"
    driver.get(STREETWISE_URL)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'WSJTheme--headline--unZqjb45')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(5)

    images = driver.find_elements(By.CLASS_NAME, 'WSJTheme--image--At42misj')
    links = driver.find_elements(By.CLASS_NAME, 'WSJTheme--headline--unZqjb45')

    articles_imgs = [image.get_attribute('src') for image in images]
    articles_links = [link.find_element(By.TAG_NAME, 'a').get_attribute('href') for link in links]

    # print(articles_imgs)
    # print(articles_links)

    time.sleep(2)

    for i in range(len(articles_links)):
        driver.get(articles_links[i])
        w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
        time.sleep(2)
        try:
            title = driver.find_element(By.CLASS_NAME, 'css-1lvqw7f-StyledHeadline').text
        except:
            title = driver.find_element(By.TAG_NAME, 'h1').text
        try:
            author = driver.find_element(By.CLASS_NAME, 'css-nyr2iw-AuthorContainer').find_element(By.TAG_NAME,
                                                                                                   'a').text
        except:
            author = "Not Found"
        date = driver.find_element(By.TAG_NAME, 'time').text
        try:
            type = driver.find_element(By.CLASS_NAME, 'css-e8qa5r-Link').text
        except:
            type = "Not Found"

        content = driver.find_elements(By.CLASS_NAME, 'css-xbvutc-Paragraph')
        content = [str(item.text) + "\n" for item in content]
        content = "".join(content)
        try:
            article_description = driver.find_element(By.CLASS_NAME, 'css-mosdo-Dek-Dek').text
        except:
            article_description = driver.find_element(By.TAG_NAME, 'h2')

        with open('streetwise.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [articles_links[i], title, articles_imgs[i], author, date, type, article_description, content]
            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_streetwise():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    STREETWISE_URL = "https://www.wsj.com/news/types/streetwise?mod=nav_top_subsection"
    driver.get(STREETWISE_URL)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'WSJTheme--headline--unZqjb45')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(5)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'WSJTheme--image--At42misj')))
    articles_imgs = driver.find_element(By.CLASS_NAME, 'WSJTheme--image--At42misj').get_attribute('src')
    articles_links = driver.find_element(By.CLASS_NAME, 'WSJTheme--headline--unZqjb45').find_element(By.TAG_NAME,
                                                                                                     'a').get_attribute(
        'href')
    time.sleep(2)

    driver.get(articles_links)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
    time.sleep(2)
    try:
        title = driver.find_element(By.CLASS_NAME, 'css-1lvqw7f-StyledHeadline').text
    except:
        title = driver.find_element(By.TAG_NAME, 'h1').text
    try:
        author = driver.find_element(By.CLASS_NAME, 'css-nyr2iw-AuthorContainer').find_element(By.TAG_NAME,
                                                                                               'a').text
    except:
        author = "Not Found"
    date = driver.find_element(By.TAG_NAME, 'time').text
    try:
        type = driver.find_element(By.CLASS_NAME, 'css-e8qa5r-Link').text
    except:
        type = "Not Found"

    content = driver.find_elements(By.CLASS_NAME, 'css-xbvutc-Paragraph')
    content = [str(item.text) + "\n" for item in content]
    content = "".join(content)
    try:
        article_description = driver.find_element(By.CLASS_NAME, 'css-mosdo-Dek-Dek').text
    except:
        article_description = driver.find_element(By.TAG_NAME, 'h2')

    article = {
        "post_category": type,
        "news_url": articles_links,
        "title": title,
        "author": author,
        "date": date,
        "image_url": articles_imgs,
        "description": article_description,
        "original_text": content,
    }
    pprint.pprint(article)


# ===================================THE INTELLIGENT INVESTOR=============================================
def export_intelligent_investor():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    INTELLIGENT_INVESTOR_URL = "https://www.wsj.com/news/types/the-intelligent-investor?mod=nav_top_subsection"
    driver.get(INTELLIGENT_INVESTOR_URL)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'WSJTheme--headline--unZqjb45')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(5)

    images = driver.find_elements(By.CLASS_NAME, 'WSJTheme--image--At42misj')
    links = driver.find_elements(By.CLASS_NAME, 'WSJTheme--headline--unZqjb45')

    articles_imgs = [image.get_attribute('src') for image in images]
    articles_links = [link.find_element(By.TAG_NAME, 'a').get_attribute('href') for link in links]

    # print(articles_imgs)
    # print(articles_links)

    time.sleep(2)

    for i in range(len(articles_links)):
        driver.get(articles_links[i])
        w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
        time.sleep(2)
        try:
            title = driver.find_element(By.CLASS_NAME, 'css-1lvqw7f-StyledHeadline').text
        except:
            title = driver.find_element(By.TAG_NAME, 'h1').text
        try:
            author = driver.find_element(By.CLASS_NAME, 'css-nyr2iw-AuthorContainer').find_element(By.TAG_NAME,
                                                                                                   'a').text
        except:
            author = "Not Found"
        date = driver.find_element(By.TAG_NAME, 'time').text
        try:
            type = driver.find_element(By.CLASS_NAME, 'css-e8qa5r-Link').text
        except:
            type = "Not Found"

        content = driver.find_elements(By.CLASS_NAME, 'css-xbvutc-Paragraph')
        content = [str(item.text) + "\n" for item in content]
        content = "".join(content)
        try:
            article_description = driver.find_element(By.CLASS_NAME, 'css-mosdo-Dek-Dek').text
        except:
            article_description = driver.find_element(By.TAG_NAME, 'h2')

        with open('intelligent_investor.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [articles_links[i], title, articles_imgs[i], author, date, type, article_description, content]
            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_intelligent_investor():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    INTELLIGENT_INVESTOR_URL = "https://www.wsj.com/news/types/the-intelligent-investor?mod=nav_top_subsection"
    driver.get(INTELLIGENT_INVESTOR_URL)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'WSJTheme--headline--unZqjb45')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(5)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'WSJTheme--image--At42misj')))
    articles_imgs = driver.find_element(By.CLASS_NAME, 'WSJTheme--image--At42misj').get_attribute('src')
    articles_links = driver.find_element(By.CLASS_NAME, 'WSJTheme--headline--unZqjb45').find_element(By.TAG_NAME,
                                                                                                     'a').get_attribute(
        'href')
    time.sleep(2)

    driver.get(articles_links)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
    time.sleep(2)
    try:
        title = driver.find_element(By.CLASS_NAME, 'css-1lvqw7f-StyledHeadline').text
    except:
        title = driver.find_element(By.TAG_NAME, 'h1').text
    try:
        author = driver.find_element(By.CLASS_NAME, 'css-nyr2iw-AuthorContainer').find_element(By.TAG_NAME,
                                                                                               'a').text
    except:
        author = "Not Found"
    date = driver.find_element(By.TAG_NAME, 'time').text
    try:
        type = driver.find_element(By.CLASS_NAME, 'css-e8qa5r-Link').text
    except:
        type = "Not Found"

    content = driver.find_elements(By.CLASS_NAME, 'css-xbvutc-Paragraph')
    content = [str(item.text) + "\n" for item in content]
    content = "".join(content)
    try:
        article_description = driver.find_element(By.CLASS_NAME, 'css-mosdo-Dek-Dek').text
    except:
        article_description = driver.find_element(By.TAG_NAME, 'h2')

    article = {
        "post_category": type,
        "news_url": articles_links,
        "title": title,
        "author": author,
        "date": date,
        "image_url": articles_imgs,
        "description": article_description,
        "original_text": content,
    }
    pprint.pprint(article)


# ==============================================HEARD ON THE STREET========================================
def export_heard_on_the_street():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    HEARD_ON_THE_STREET_URL = "https://www.wsj.com/news/heard-on-the-street?mod=nav_top_subsection"
    driver.get(HEARD_ON_THE_STREET_URL)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'WSJTheme--headline--unZqjb45')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(5)

    images = driver.find_elements(By.CLASS_NAME, 'WSJTheme--image--At42misj')
    links = driver.find_elements(By.CLASS_NAME, 'WSJTheme--headline--unZqjb45')

    articles_imgs = [image.get_attribute('src') for image in images]
    articles_links = [link.find_element(By.TAG_NAME, 'a').get_attribute('href') for link in links]

    # print(articles_imgs)
    # print(articles_links)

    time.sleep(2)

    for i in range(len(articles_links)):
        driver.get(articles_links[i])
        w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
        time.sleep(2)
        try:
            title = driver.find_element(By.CLASS_NAME, 'css-1lvqw7f-StyledHeadline').text
        except:
            title = driver.find_element(By.TAG_NAME, 'h1').text
        try:
            author = driver.find_element(By.CLASS_NAME, 'css-nyr2iw-AuthorContainer').find_element(By.TAG_NAME,
                                                                                                   'a').text
        except:
            author = "Not Found"
        date = driver.find_element(By.TAG_NAME, 'time').text
        try:
            type = driver.find_element(By.CLASS_NAME, 'css-e8qa5r-Link').text
        except:
            type = "Not Found"

        content = driver.find_elements(By.CLASS_NAME, 'css-xbvutc-Paragraph')
        content = [str(item.text) + "\n" for item in content]
        content = "".join(content)
        try:
            article_description = driver.find_element(By.CLASS_NAME, 'css-mosdo-Dek-Dek').text
        except:
            article_description = driver.find_element(By.TAG_NAME, 'h2')

        with open('heard_on_the_street.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [articles_links[i], title, articles_imgs[i], author, date, type, article_description, content]
            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_heard_on_the_street():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    HEARD_ON_THE_STREET_URL = "https://www.wsj.com/news/heard-on-the-street?mod=nav_top_subsection"
    driver.get(HEARD_ON_THE_STREET_URL)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'WSJTheme--headline--unZqjb45')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(5)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'WSJTheme--image--At42misj')))
    articles_imgs = driver.find_element(By.CLASS_NAME, 'WSJTheme--image--At42misj').get_attribute('src')
    articles_links = driver.find_element(By.CLASS_NAME, 'WSJTheme--headline--unZqjb45').find_element(By.TAG_NAME,
                                                                                                     'a').get_attribute(
        'href')
    time.sleep(2)

    driver.get(articles_links)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
    time.sleep(2)
    try:
        title = driver.find_element(By.CLASS_NAME, 'css-1lvqw7f-StyledHeadline').text
    except:
        title = driver.find_element(By.TAG_NAME, 'h1').text
    try:
        author = driver.find_element(By.CLASS_NAME, 'css-nyr2iw-AuthorContainer').find_element(By.TAG_NAME,
                                                                                               'a').text
    except:
        author = "Not Found"
    date = driver.find_element(By.TAG_NAME, 'time').text
    try:
        type = driver.find_element(By.CLASS_NAME, 'css-e8qa5r-Link').text
    except:
        type = "Not Found"

    content = driver.find_elements(By.CLASS_NAME, 'css-xbvutc-Paragraph')
    content = [str(item.text) + "\n" for item in content]
    content = "".join(content)
    try:
        article_description = driver.find_element(By.CLASS_NAME, 'css-mosdo-Dek-Dek').text
    except:
        article_description = driver.find_element(By.TAG_NAME, 'h2')

    article = {
        "post_category": type,
        "news_url": articles_links,
        "title": title,
        "author": author,
        "date": date,
        "image_url": articles_imgs,
        "description": article_description,
        "original_text": content,
    }
    pprint.pprint(article)


# ==============================================Greg Ip========================================

def export_grep_id():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    Greg_Ip_URL = "https://www.wsj.com/news/author/greg-ip?mod=nav_top_subsection"
    driver.get(Greg_Ip_URL)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'WSJTheme--headline--unZqjb45')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(5)

    images = driver.find_elements(By.CLASS_NAME, 'WSJTheme--image--At42misj')
    links = driver.find_elements(By.CLASS_NAME, 'WSJTheme--headline--unZqjb45')

    articles_imgs = [image.get_attribute('src') for image in images]
    articles_links = [link.find_element(By.TAG_NAME, 'a').get_attribute('href') for link in links]

    # print(articles_imgs)
    # print(articles_links)

    time.sleep(2)

    for i in range(len(articles_links)):
        driver.get(articles_links[i])
        w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
        time.sleep(2)
        try:
            title = driver.find_element(By.CLASS_NAME, 'css-1lvqw7f-StyledHeadline').text
        except:
            title = driver.find_element(By.TAG_NAME, 'h1').text
        try:
            author = driver.find_element(By.CLASS_NAME, 'css-nyr2iw-AuthorContainer').find_element(By.TAG_NAME,
                                                                                                   'a').text
        except:
            author = "Not Found"
        date = driver.find_element(By.TAG_NAME, 'time').text
        try:
            type = driver.find_element(By.CLASS_NAME, 'css-e8qa5r-Link').text
        except:
            type = "Not Found"

        content = driver.find_elements(By.CLASS_NAME, 'css-xbvutc-Paragraph')
        content = [str(item.text) + "\n" for item in content]
        content = "".join(content)
        try:
            article_description = driver.find_element(By.CLASS_NAME, 'css-mosdo-Dek-Dek').text
        except:
            article_description = driver.find_element(By.TAG_NAME, 'h2')

        with open('greg_ip.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [articles_links[i], title, articles_imgs[i], author, date, type, article_description, content]
            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_grep_id():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    Greg_Ip_URL = "https://www.wsj.com/news/author/greg-ip?mod=nav_top_subsection"
    driver.get(Greg_Ip_URL)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'WSJTheme--headline--unZqjb45')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(5)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'WSJTheme--image--At42misj')))
    articles_imgs = driver.find_element(By.CLASS_NAME, 'WSJTheme--image--At42misj').get_attribute('src')
    articles_links = driver.find_element(By.CLASS_NAME, 'WSJTheme--headline--unZqjb45').find_element(By.TAG_NAME,
                                                                                                     'a').get_attribute(
        'href')
    time.sleep(2)

    driver.get(articles_links)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
    time.sleep(2)
    try:
        title = driver.find_element(By.CLASS_NAME, 'css-1lvqw7f-StyledHeadline').text
    except:
        title = driver.find_element(By.TAG_NAME, 'h1').text
    try:
        author = driver.find_element(By.CLASS_NAME, 'css-nyr2iw-AuthorContainer').find_element(By.TAG_NAME,
                                                                                               'a').text
    except:
        author = "Not Found"
    date = driver.find_element(By.TAG_NAME, 'time').text
    try:
        type = driver.find_element(By.CLASS_NAME, 'css-e8qa5r-Link').text
    except:
        type = "Not Found"

    content = driver.find_elements(By.CLASS_NAME, 'css-xbvutc-Paragraph')
    content = [str(item.text) + "\n" for item in content]
    content = "".join(content)
    try:
        article_description = driver.find_element(By.CLASS_NAME, 'css-mosdo-Dek-Dek').text
    except:
        article_description = driver.find_element(By.TAG_NAME, 'h2')

    article = {
        "post_category": type,
        "news_url": articles_links,
        "title": title,
        "author": author,
        "date": date,
        "image_url": articles_imgs,
        "description": article_description,
        "original_text": content,
    }
    pprint.pprint(article)


# ==============================================Jason Zweig========================================

def export_jason_zweig():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    JASON_Zweig_URL = "https://www.wsj.com/news/author/jason-zweig?mod=nav_top_subsection"
    driver.get(JASON_Zweig_URL)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'WSJTheme--headline--unZqjb45')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(5)

    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'WSJTheme--headline--unZqjb45')))

    images = driver.find_elements(By.CLASS_NAME, 'WSJTheme--image--At42misj')
    links = driver.find_elements(By.CLASS_NAME, 'WSJTheme--headline--unZqjb45')

    articles_imgs = [image.get_attribute('src') for image in images]
    articles_links = [link.find_element(By.TAG_NAME, 'a').get_attribute('href') for link in links]

    # print(articles_imgs)
    # print(articles_links)

    time.sleep(2)

    for i in range(len(articles_links)):
        driver.get(articles_links[i])
        w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
        time.sleep(2)
        try:
            title = driver.find_element(By.CLASS_NAME, 'css-1lvqw7f-StyledHeadline').text
        except:
            title = driver.find_element(By.TAG_NAME, 'h1').text
        try:
            author = driver.find_element(By.CLASS_NAME, 'css-nyr2iw-AuthorContainer').find_element(By.TAG_NAME,
                                                                                                   'a').text
        except:
            author = "Not Found"
        date = driver.find_element(By.TAG_NAME, 'time').text
        try:
            type = driver.find_element(By.CLASS_NAME, 'css-e8qa5r-Link').text
        except:
            type = "Not Found"

        content = driver.find_elements(By.CLASS_NAME, 'css-xbvutc-Paragraph')
        content = [str(item.text) + "\n" for item in content]
        content = "".join(content)
        try:
            article_description = driver.find_element(By.CLASS_NAME, 'css-mosdo-Dek-Dek').text
        except:
            article_description = driver.find_element(By.TAG_NAME, 'h2')

        with open('Jason_Zweig.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [articles_links[i], title, articles_imgs[i], author, date, type, article_description, content]
            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_jason_zweig():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    JASON_Zweig_URL = "https://www.wsj.com/news/author/jason-zweig?mod=nav_top_subsection"
    driver.get(JASON_Zweig_URL)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'WSJTheme--headline--unZqjb45')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(5)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'WSJTheme--headline--unZqjb45')))
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'WSJTheme--image--At42misj')))
    articles_imgs = driver.find_element(By.CLASS_NAME, 'WSJTheme--image--At42misj').get_attribute('src')
    articles_links = driver.find_element(By.CLASS_NAME, 'WSJTheme--headline--unZqjb45').find_element(By.TAG_NAME,
                                                                                                     'a').get_attribute(
        'href')
    time.sleep(2)

    driver.get(articles_links)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
    time.sleep(2)
    try:
        title = driver.find_element(By.CLASS_NAME, 'css-1lvqw7f-StyledHeadline').text
    except:
        title = driver.find_element(By.TAG_NAME, 'h1').text
    try:
        author = driver.find_element(By.CLASS_NAME, 'css-nyr2iw-AuthorContainer').find_element(By.TAG_NAME,
                                                                                               'a').text
    except:
        author = "Not Found"
    date = driver.find_element(By.TAG_NAME, 'time').text
    try:
        type = driver.find_element(By.CLASS_NAME, 'css-e8qa5r-Link').text
    except:
        type = "Not Found"

    content = driver.find_elements(By.CLASS_NAME, 'css-xbvutc-Paragraph')
    content = [str(item.text) + "\n" for item in content]
    content = "".join(content)
    try:
        article_description = driver.find_element(By.CLASS_NAME, 'css-mosdo-Dek-Dek').text
    except:
        article_description = driver.find_element(By.TAG_NAME, 'h2')

    article = {
        "post_category": type,
        "news_url": articles_links,
        "title": title,
        "author": author,
        "date": date,
        "image_url": articles_imgs,
        "description": article_description,
        "original_text": content,
    }
    pprint.pprint(article)


# ==============================================Laura Saunders========================================

def export_laura_saunders():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    LAURA_Saunders_URL = "https://www.wsj.com/news/author/laura-saunders?mod=nav_top_subsection"
    driver.get(LAURA_Saunders_URL)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'WSJTheme--headline--unZqjb45')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(5)

    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'WSJTheme--headline--unZqjb45')))

    images = driver.find_elements(By.CLASS_NAME, 'WSJTheme--image--At42misj')
    links = driver.find_elements(By.CLASS_NAME, 'WSJTheme--headline--unZqjb45')

    articles_imgs = [image.get_attribute('src') for image in images]
    articles_links = [link.find_element(By.TAG_NAME, 'a').get_attribute('href') for link in links]

    # print(articles_imgs)
    # print(articles_links)

    time.sleep(2)

    for i in range(len(articles_links)):
        driver.get(articles_links[i])
        w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
        time.sleep(2)
        try:
            title = driver.find_element(By.CLASS_NAME, 'css-1lvqw7f-StyledHeadline').text
        except:
            title = driver.find_element(By.TAG_NAME, 'h1').text
        try:
            author = driver.find_element(By.CLASS_NAME, 'css-nyr2iw-AuthorContainer').find_element(By.TAG_NAME,
                                                                                                   'a').text
        except:
            author = "Not Found"
        date = driver.find_element(By.TAG_NAME, 'time').text
        try:
            type = driver.find_element(By.CLASS_NAME, 'css-e8qa5r-Link').text
        except:
            type = "Not Found"

        content = driver.find_elements(By.CLASS_NAME, 'css-xbvutc-Paragraph')
        content = [str(item.text) + "\n" for item in content]
        content = "".join(content)
        try:
            article_description = driver.find_element(By.CLASS_NAME, 'css-mosdo-Dek-Dek').text
        except:
            article_description = driver.find_element(By.TAG_NAME, 'h2')

        with open('Laura_Saunders.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [articles_links[i], title, articles_imgs[i], author, date, type, article_description, content]
            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_laura_saunders():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    LAURA_Saunders_URL = "https://www.wsj.com/news/author/laura-saunders?mod=nav_top_subsection"
    driver.get(LAURA_Saunders_URL)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'WSJTheme--headline--unZqjb45')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(5)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'WSJTheme--headline--unZqjb45')))
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'WSJTheme--image--At42misj')))
    articles_imgs = driver.find_element(By.CLASS_NAME, 'WSJTheme--image--At42misj').get_attribute('src')
    articles_links = driver.find_element(By.CLASS_NAME, 'WSJTheme--headline--unZqjb45').find_element(By.TAG_NAME,
                                                                                                     'a').get_attribute(
        'href')
    time.sleep(2)

    driver.get(articles_links)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
    time.sleep(2)
    try:
        title = driver.find_element(By.CLASS_NAME, 'css-1lvqw7f-StyledHeadline').text
    except:
        title = driver.find_element(By.TAG_NAME, 'h1').text
    try:
        author = driver.find_element(By.CLASS_NAME, 'css-nyr2iw-AuthorContainer').find_element(By.TAG_NAME,
                                                                                               'a').text
    except:
        author = "Not Found"
    date = driver.find_element(By.TAG_NAME, 'time').text
    try:
        type = driver.find_element(By.CLASS_NAME, 'css-e8qa5r-Link').text
    except:
        type = "Not Found"

    content = driver.find_elements(By.CLASS_NAME, 'css-xbvutc-Paragraph')
    content = [str(item.text) + "\n" for item in content]
    content = "".join(content)
    try:
        article_description = driver.find_element(By.CLASS_NAME, 'css-mosdo-Dek-Dek').text
    except:
        article_description = driver.find_element(By.TAG_NAME, 'h2')

    article = {
        "post_category": type,
        "news_url": articles_links,
        "title": title,
        "author": author,
        "date": date,
        "image_url": articles_imgs,
        "description": article_description,
        "original_text": content,
    }
    pprint.pprint(article)


# ==============================================James Mackintosh========================================

def export_james_mackintosh():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    James_Mackintosh_URL = "https://www.wsj.com/news/author/james-mackintosh?page=23?mod=nav_top_subsection"
    driver.get(James_Mackintosh_URL)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'WSJTheme--headline--unZqjb45')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(5)

    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'WSJTheme--headline--unZqjb45')))

    images = driver.find_elements(By.CLASS_NAME, 'WSJTheme--image--At42misj')
    links = driver.find_elements(By.CLASS_NAME, 'WSJTheme--headline--unZqjb45')

    articles_imgs = [image.get_attribute('src') for image in images]
    articles_links = [link.find_element(By.TAG_NAME, 'a').get_attribute('href') for link in links]

    # print(articles_imgs)
    # print(articles_links)

    time.sleep(2)

    for i in range(len(articles_links)):
        driver.get(articles_links[i])
        w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
        time.sleep(2)
        try:
            title = driver.find_element(By.CLASS_NAME, 'css-1lvqw7f-StyledHeadline').text
        except:
            title = driver.find_element(By.TAG_NAME, 'h1').text
        try:
            author = driver.find_element(By.CLASS_NAME, 'css-nyr2iw-AuthorContainer').find_element(By.TAG_NAME,
                                                                                                   'a').text
        except:
            author = "Not Found"
        date = driver.find_element(By.TAG_NAME, 'time').text
        try:
            type = driver.find_element(By.CLASS_NAME, 'css-e8qa5r-Link').text
        except:
            type = "Not Found"

        content = driver.find_elements(By.CLASS_NAME, 'css-xbvutc-Paragraph')
        content = [str(item.text) + "\n" for item in content]
        content = "".join(content)
        try:
            article_description = driver.find_element(By.CLASS_NAME, 'css-mosdo-Dek-Dek').text
        except:
            article_description = driver.find_element(By.TAG_NAME, 'h2')

        with open('James_Mackintosh.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [articles_links[i], title, articles_imgs[i], author, date, type, article_description, content]
            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_james_mackintosh():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    James_Mackintosh_URL = "https://www.wsj.com/news/author/james-mackintosh?page=23?mod=nav_top_subsection"
    driver.get(James_Mackintosh_URL)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'WSJTheme--headline--unZqjb45')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(5)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'WSJTheme--headline--unZqjb45')))
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'WSJTheme--image--At42misj')))
    articles_imgs = driver.find_element(By.CLASS_NAME, 'WSJTheme--image--At42misj').get_attribute('src')
    articles_links = driver.find_element(By.CLASS_NAME, 'WSJTheme--headline--unZqjb45').find_element(By.TAG_NAME,
                                                                                                     'a').get_attribute(
        'href')
    time.sleep(2)

    driver.get(articles_links)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
    time.sleep(2)
    try:
        title = driver.find_element(By.CLASS_NAME, 'css-1lvqw7f-StyledHeadline').text
    except:
        title = driver.find_element(By.TAG_NAME, 'h1').text
    try:
        author = driver.find_element(By.CLASS_NAME, 'css-nyr2iw-AuthorContainer').find_element(By.TAG_NAME,
                                                                                               'a').text
    except:
        author = "Not Found"
    date = driver.find_element(By.TAG_NAME, 'time').text
    try:
        type = driver.find_element(By.CLASS_NAME, 'css-e8qa5r-Link').text
    except:
        type = "Not Found"

    content = driver.find_elements(By.CLASS_NAME, 'css-xbvutc-Paragraph')
    content = [str(item.text) + "\n" for item in content]
    content = "".join(content)
    try:
        article_description = driver.find_element(By.CLASS_NAME, 'css-mosdo-Dek-Dek').text
    except:
        article_description = driver.find_element(By.TAG_NAME, 'h2')

    article = {
        "post_category": type,
        "news_url": articles_links,
        "title": title,
        "author": author,
        "date": date,
        "image_url": articles_imgs,
        "description": article_description,
        "original_text": content,
    }
    pprint.pprint(article)

# =====================================RUN_FUNCTION=============================================
