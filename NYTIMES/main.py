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


# ==========================================cryptocurrency==========================================

def export_cryptocurrency():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    NYTINES_URL = "https://www.nytimes.com/spotlight/cryptocurrency"
    driver.get(NYTINES_URL)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(4)

    driver.execute_script("window.scrollTo(0, 1300)")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 2000)")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 2300)")
    time.sleep(2)

    images = driver.find_elements(By.CLASS_NAME, 'css-rq4mmj')
    links = driver.find_elements(By.CLASS_NAME, 'css-1l4spti')
    titles = driver.find_elements(By.CLASS_NAME, 'css-1kv6qi')
    descriptions = driver.find_elements(By.CLASS_NAME, 'css-1pga48a')
    authors = driver.find_elements(By.CLASS_NAME, 'css-1n7hynb')
    dates = driver.find_elements(By.CLASS_NAME, 'css-e0xall')

    articles_imgs = [image.get_attribute('src') for image in images]
    articles_links = [link.find_element(By.TAG_NAME, 'a').get_attribute('href') for link in links]
    articles_titles = [title.text for title in titles]
    articles_authors = [author.text for author in authors]
    articles_descriptions = [description.text for description in descriptions]

    time.sleep(2)

    for i in range(len(articles_links)):
        driver.get(articles_links[i])
        w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
        time.sleep(2)

        content = driver.find_elements(By.CLASS_NAME, 'css-at9mc1')
        content = [str(item.text) + "\n" for item in content]
        content = "".join(content)

        try:
            articles_dates = driver.find_element(By.TAG_NAME, 'time').get_attribute('datetime').split('T')[0]
        except:
            articles_dates = driver.find_element(By.CLASS_NAME, 'css-1iqjk4r').text.split('•')[1]


        with open('cryptocurrency.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [articles_links[i], articles_titles[i], articles_imgs[i], articles_authors[i],
                           articles_dates,
                           articles_descriptions[i], content]
            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_cryptocurrency():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    NYTINES_URL = "https://www.nytimes.com/spotlight/cryptocurrency"
    driver.get(NYTINES_URL)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(4)

    articles_imgs = driver.find_element(By.CLASS_NAME, 'css-rq4mmj').get_attribute('src')
    articles_links = driver.find_element(By.CLASS_NAME, 'css-1l4spti').find_element(By.TAG_NAME, 'a').get_attribute(
        'href')
    articles_titles = driver.find_element(By.CLASS_NAME, 'css-1kv6qi').text
    articles_descriptions = driver.find_element(By.CLASS_NAME, 'css-1pga48a').text
    articles_authors = driver.find_element(By.CLASS_NAME, 'css-1n7hynb').text

    time.sleep(2)

    driver.get(articles_links)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
    time.sleep(2)

    content = driver.find_elements(By.CLASS_NAME, 'css-at9mc1')
    content = [str(item.text) + "\n" for item in content]
    content = "".join(content)

    try:
        articles_dates = driver.find_element(By.TAG_NAME, 'time').get_attribute('datetime').split('T')[0]
    except:
        articles_dates = driver.find_element(By.CLASS_NAME, 'css-1iqjk4r').text.split('•')[1]

    article = {
        "post_category": "cryptocurrency",
        "news_url": articles_links,
        "title": articles_titles,
        "author": articles_authors,
        "date": articles_dates,
        "image_url": articles_imgs,
        "description": articles_descriptions,
        "original_text": content,
    }
    pprint.pprint(article)


# ==========================================TECHNOLOGY==========================================

def export_technology():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    TECH_URL = "https://www.nytimes.com/section/technology"
    driver.get(TECH_URL)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(4)

    driver.execute_script("window.scrollTo(0, 1300)")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 2000)")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 2300)")
    time.sleep(3)

    images = driver.find_elements(By.CLASS_NAME, 'css-rq4mmj')
    links = driver.find_elements(By.CLASS_NAME, 'css-1l4spti')
    titles = driver.find_elements(By.CLASS_NAME, 'css-1kv6qi')
    descriptions = driver.find_elements(By.CLASS_NAME, 'css-1pga48a')
    authors = driver.find_elements(By.CLASS_NAME, 'css-1n7hynb')
    dates = driver.find_elements(By.CLASS_NAME, 'css-e0xall')

    articles_imgs = [image.get_attribute('src') for image in images]
    articles_links = [link.find_element(By.TAG_NAME, 'a').get_attribute('href') for link in links]
    articles_titles = [title.text for title in titles]
    articles_authors = [author.text for author in authors]
    articles_descriptions = [description.text for description in descriptions]

    time.sleep(2)

    for i in range(len(articles_links)):
        driver.get(articles_links[i])
        w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
        time.sleep(2)

        content = driver.find_elements(By.CLASS_NAME, 'css-at9mc1')
        content = [str(item.text) + "\n" for item in content]
        content = "".join(content)

        try:
            articles_dates = driver.find_element(By.TAG_NAME, 'time').get_attribute('datetime').split('T')[0]
        except:
            articles_dates = driver.find_element(By.CLASS_NAME, 'css-1iqjk4r').text.split('•')[1]

        with open('technology.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [articles_links[i], articles_titles[i], articles_imgs[i], articles_authors[i],
                           articles_dates,
                           articles_descriptions[i], content]
            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_technology():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    TECH_URL = "https://www.nytimes.com/section/technology"
    driver.get(TECH_URL)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(4)

    driver.execute_script("window.scrollTo(0, 1300)")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 2000)")
    time.sleep(2)

    articles_imgs = driver.find_element(By.CLASS_NAME, 'css-rq4mmj').get_attribute('src')
    articles_links = driver.find_element(By.CLASS_NAME, 'css-1l4spti').find_element(By.TAG_NAME, 'a').get_attribute(
        'href')
    articles_titles = driver.find_element(By.CLASS_NAME, 'css-1kv6qi').text
    articles_descriptions = driver.find_element(By.CLASS_NAME, 'css-1pga48a').text
    articles_authors = driver.find_element(By.CLASS_NAME, 'css-1n7hynb').text

    time.sleep(2)

    driver.get(articles_links)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
    time.sleep(2)

    content = driver.find_elements(By.CLASS_NAME, 'css-at9mc1')
    content = [str(item.text) + "\n" for item in content]
    content = "".join(content)

    try:
        articles_dates = driver.find_element(By.TAG_NAME, 'time').get_attribute('datetime').split('T')[0]
    except:
        articles_dates = driver.find_element(By.CLASS_NAME, 'css-1iqjk4r').text.split('•')[1]

    article = {
        "post_category": "TECHNOLOGY",
        "news_url": articles_links,
        "title": articles_titles,
        "author": articles_authors,
        "date": articles_dates,
        "image_url": articles_imgs,
        "description": articles_descriptions,
        "original_text": content,
    }
    pprint.pprint(article)


# ==========================================ECONOMY==========================================

def export_economy():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    ECON_URL = "https://www.nytimes.com/section/business/economy"
    driver.get(ECON_URL)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(4)

    driver.execute_script("window.scrollTo(0, 1300)")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 1600)")
    time.sleep(3)

    images = driver.find_elements(By.CLASS_NAME, 'css-rq4mmj')
    links = driver.find_elements(By.CLASS_NAME, 'css-1l4spti')
    titles = driver.find_elements(By.CLASS_NAME, 'css-1kv6qi')
    descriptions = driver.find_elements(By.CLASS_NAME, 'css-1pga48a')
    authors = driver.find_elements(By.CLASS_NAME, 'css-1n7hynb')
    dates = driver.find_elements(By.CLASS_NAME, 'css-e0xall')

    articles_imgs = [image.get_attribute('src') for image in images]
    articles_links = [link.find_element(By.TAG_NAME, 'a').get_attribute('href') for link in links]
    articles_titles = [title.text for title in titles]
    articles_authors = [author.text for author in authors]
    articles_descriptions = [description.text for description in descriptions]

    time.sleep(2)

    for i in range(len(articles_links)):
        driver.get(articles_links[i])
        w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
        time.sleep(2)

        content = driver.find_elements(By.CLASS_NAME, 'css-at9mc1')
        content = [str(item.text) + "\n" for item in content]
        content = "".join(content)

        try:
            articles_dates = driver.find_element(By.TAG_NAME, 'time').get_attribute('datetime').split('T')[0]
        except:
            articles_dates = driver.find_element(By.CLASS_NAME, 'css-1iqjk4r').text.split('•')[1]

        with open('economy.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [articles_links[i], articles_titles[i], articles_imgs[i], articles_authors[i],
                           articles_dates,
                           articles_descriptions[i], content]
            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_economy():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    ECON_URL = "https://www.nytimes.com/section/business/economy"
    driver.get(ECON_URL)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(4)

    driver.execute_script("window.scrollTo(0, 1300)")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 1600)")
    time.sleep(2)

    articles_imgs = driver.find_element(By.CLASS_NAME, 'css-rq4mmj').get_attribute('src')
    articles_links = driver.find_element(By.CLASS_NAME, 'css-1l4spti').find_element(By.TAG_NAME, 'a').get_attribute(
        'href')
    articles_titles = driver.find_element(By.CLASS_NAME, 'css-1kv6qi').text
    articles_descriptions = driver.find_element(By.CLASS_NAME, 'css-1pga48a').text
    articles_authors = driver.find_element(By.CLASS_NAME, 'css-1n7hynb').text

    time.sleep(2)

    driver.get(articles_links)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
    time.sleep(2)

    content = driver.find_elements(By.CLASS_NAME, 'css-at9mc1')
    content = [str(item.text) + "\n" for item in content]
    content = "".join(content)

    try:
        articles_dates = driver.find_element(By.TAG_NAME, 'time').get_attribute('datetime').split('T')[0]
    except:
        articles_dates = driver.find_element(By.CLASS_NAME, 'css-1iqjk4r').text.split('•')[1]

    article = {
        "post_category": "ECONOMY",
        "news_url": articles_links,
        "title": articles_titles,
        "author": articles_authors,
        "date": articles_dates,
        "image_url": articles_imgs,
        "description": articles_descriptions,
        "original_text": content,
    }
    pprint.pprint(article)


# ==========================================MEDIA==========================================

def export_media():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    MEDIA_URL = "https://www.nytimes.com/section/business/media"
    driver.get(MEDIA_URL)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(4)

    driver.execute_script("window.scrollTo(0, 1300)")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 1600)")
    time.sleep(3)

    images = driver.find_elements(By.CLASS_NAME, 'css-rq4mmj')
    links = driver.find_elements(By.CLASS_NAME, 'css-1l4spti')
    titles = driver.find_elements(By.CLASS_NAME, 'css-1kv6qi')
    descriptions = driver.find_elements(By.CLASS_NAME, 'css-1pga48a')
    authors = driver.find_elements(By.CLASS_NAME, 'css-1n7hynb')
    dates = driver.find_elements(By.CLASS_NAME, 'css-e0xall')

    articles_imgs = [image.get_attribute('src') for image in images]
    articles_links = [link.find_element(By.TAG_NAME, 'a').get_attribute('href') for link in links]
    articles_titles = [title.text for title in titles]
    articles_authors = [author.text for author in authors]
    articles_descriptions = [description.text for description in descriptions]

    time.sleep(2)

    for i in range(len(articles_links)):
        driver.get(articles_links[i])
        w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
        time.sleep(2)

        content = driver.find_elements(By.CLASS_NAME, 'css-at9mc1')
        content = [str(item.text) + "\n" for item in content]
        content = "".join(content)

        try:
            articles_dates = driver.find_element(By.TAG_NAME, 'time').get_attribute('datetime').split('T')[0]
        except:
            articles_dates = driver.find_element(By.CLASS_NAME, 'css-1iqjk4r').text.split('•')[1]

        with open('media.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [articles_links[i], articles_titles[i], articles_imgs[i], articles_authors[i],
                           articles_dates,
                           articles_descriptions[i], content]
            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_media():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    MEDIA_URL = "https://www.nytimes.com/section/business/media"
    driver.get(MEDIA_URL)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(4)

    driver.execute_script("window.scrollTo(0, 1300)")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 1600)")
    time.sleep(2)

    articles_imgs = driver.find_element(By.CLASS_NAME, 'css-rq4mmj').get_attribute('src')
    articles_links = driver.find_element(By.CLASS_NAME, 'css-1l4spti').find_element(By.TAG_NAME, 'a').get_attribute(
        'href')
    articles_titles = driver.find_element(By.CLASS_NAME, 'css-1kv6qi').text
    articles_descriptions = driver.find_element(By.CLASS_NAME, 'css-1pga48a').text
    articles_authors = driver.find_element(By.CLASS_NAME, 'css-1n7hynb').text

    time.sleep(2)

    driver.get(articles_links)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
    time.sleep(2)

    content = driver.find_elements(By.CLASS_NAME, 'css-at9mc1')
    content = [str(item.text) + "\n" for item in content]
    content = "".join(content)

    try:
        articles_dates = driver.find_element(By.TAG_NAME, 'time').get_attribute('datetime').split('T')[0]
    except:
        articles_dates = driver.find_element(By.CLASS_NAME, 'css-1iqjk4r').text.split('•')[1]

    article = {
        "post_category": "MEDIA",
        "news_url": articles_links,
        "title": articles_titles,
        "author": articles_authors,
        "date": articles_dates,
        "image_url": articles_imgs,
        "description": articles_descriptions,
        "original_text": content,
    }
    pprint.pprint(article)


# ==========================================YOUR MONEY==========================================

def export_money():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    MONEY_URL = "https://www.nytimes.com/section/your-money"
    driver.get(MONEY_URL)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(4)

    driver.execute_script("window.scrollTo(0, 1300)")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 2000)")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 2300)")
    time.sleep(3)

    images = driver.find_elements(By.CLASS_NAME, 'css-rq4mmj')
    links = driver.find_elements(By.CLASS_NAME, 'css-1l4spti')
    titles = driver.find_elements(By.CLASS_NAME, 'css-1kv6qi')
    descriptions = driver.find_elements(By.CLASS_NAME, 'css-1pga48a')
    authors = driver.find_elements(By.CLASS_NAME, 'css-1n7hynb')
    dates = driver.find_elements(By.CLASS_NAME, 'css-e0xall')

    articles_imgs = [image.get_attribute('src') for image in images]
    articles_links = [link.find_element(By.TAG_NAME, 'a').get_attribute('href') for link in links]
    articles_titles = [title.text for title in titles]
    articles_authors = [author.text for author in authors]
    articles_descriptions = [description.text for description in descriptions]

    time.sleep(2)

    for i in range(len(articles_links)):
        driver.get(articles_links[i])
        w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
        time.sleep(2)

        content = driver.find_elements(By.CLASS_NAME, 'css-at9mc1')
        content = [str(item.text) + "\n" for item in content]
        content = "".join(content)

        try:
            articles_dates = driver.find_element(By.TAG_NAME, 'time').get_attribute('datetime').split('T')[0]
        except:
            articles_dates = driver.find_element(By.CLASS_NAME, 'css-1iqjk4r').text.split('•')[1]

        with open('money.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [articles_links[i], articles_titles[i], articles_imgs[i], articles_authors[i],
                           articles_dates,
                           articles_descriptions[i], content]
            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_money():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    MONEY_URL = "https://www.nytimes.com/section/your-money"
    driver.get(MONEY_URL)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(4)

    driver.execute_script("window.scrollTo(0, 1300)")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 1600)")
    time.sleep(2)

    articles_imgs = driver.find_element(By.CLASS_NAME, 'css-rq4mmj').get_attribute('src')
    articles_links = driver.find_element(By.CLASS_NAME, 'css-1l4spti').find_element(By.TAG_NAME, 'a').get_attribute(
        'href')
    articles_titles = driver.find_element(By.CLASS_NAME, 'css-1kv6qi').text
    articles_descriptions = driver.find_element(By.CLASS_NAME, 'css-1pga48a').text
    articles_authors = driver.find_element(By.CLASS_NAME, 'css-1n7hynb').text

    time.sleep(2)

    driver.get(articles_links)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
    time.sleep(2)

    content = driver.find_elements(By.CLASS_NAME, 'css-at9mc1')
    content = [str(item.text) + "\n" for item in content]
    content = "".join(content)

    try:
        articles_dates = driver.find_element(By.TAG_NAME, 'time').get_attribute('datetime').split('T')[0]
    except:
        articles_dates = driver.find_element(By.CLASS_NAME, 'css-1iqjk4r').text.split('•')[1]

    article = {
        "post_category": "YOUR MONEY",
        "news_url": articles_links,
        "title": articles_titles,
        "author": articles_authors,
        "date": articles_dates,
        "image_url": articles_imgs,
        "description": articles_descriptions,
        "original_text": content,
    }
    pprint.pprint(article)


# ==========================================DealBook==========================================

def export_dealbook():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    dealbook_URL = "https://www.nytimes.com/section/business/dealbook"
    driver.get(dealbook_URL)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(4)

    driver.execute_script("window.scrollTo(0, 1300)")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 2000)")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 2300)")
    time.sleep(3)

    images = driver.find_elements(By.CLASS_NAME, 'css-rq4mmj')
    links = driver.find_elements(By.CLASS_NAME, 'css-1l4spti')
    titles = driver.find_elements(By.CLASS_NAME, 'css-1kv6qi')
    descriptions = driver.find_elements(By.CLASS_NAME, 'css-1pga48a')
    authors = driver.find_elements(By.CLASS_NAME, 'css-1n7hynb')
    dates = driver.find_elements(By.CLASS_NAME, 'css-e0xall')

    articles_imgs = [image.get_attribute('src') for image in images]
    articles_links = [link.find_element(By.TAG_NAME, 'a').get_attribute('href') for link in links]
    articles_titles = [title.text for title in titles]
    articles_authors = [author.text for author in authors]
    articles_descriptions = [description.text for description in descriptions]

    time.sleep(2)

    for i in range(len(articles_links)):
        driver.get(articles_links[i])
        w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
        time.sleep(2)

        content = driver.find_elements(By.CLASS_NAME, 'css-at9mc1')
        content = [str(item.text) + "\n" for item in content]
        content = "".join(content)

        try:
            articles_dates = driver.find_element(By.TAG_NAME, 'time').get_attribute('datetime').split('T')[0]
        except:
            articles_dates = driver.find_element(By.CLASS_NAME, 'css-1iqjk4r').text.split('•')[1]

        with open('dealbook.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [articles_links[i], articles_titles[i], articles_imgs[i], articles_authors[i],
                           articles_dates,
                           articles_descriptions[i], content]
            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_dealbook():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    dealbook_URL = "https://www.nytimes.com/section/business/dealbook"
    driver.get(dealbook_URL)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(4)

    driver.execute_script("window.scrollTo(0, 1300)")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 1600)")
    time.sleep(2)

    articles_imgs = driver.find_element(By.CLASS_NAME, 'css-rq4mmj').get_attribute('src')
    articles_links = driver.find_element(By.CLASS_NAME, 'css-1l4spti').find_element(By.TAG_NAME, 'a').get_attribute(
        'href')
    articles_titles = driver.find_element(By.CLASS_NAME, 'css-1kv6qi').text
    articles_descriptions = driver.find_element(By.CLASS_NAME, 'css-1pga48a').text
    articles_authors = driver.find_element(By.CLASS_NAME, 'css-1n7hynb').text

    time.sleep(2)

    driver.get(articles_links)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
    time.sleep(2)

    content = driver.find_elements(By.CLASS_NAME, 'css-at9mc1')
    content = [str(item.text) + "\n" for item in content]
    content = "".join(content)

    try:
        articles_dates = driver.find_element(By.TAG_NAME, 'time').get_attribute('datetime').split('T')[0]
    except:
        articles_dates = driver.find_element(By.CLASS_NAME, 'css-1iqjk4r').text.split('•')[1]

    article = {
        "post_category": "DealBook",
        "news_url": articles_links,
        "title": articles_titles,
        "author": articles_authors,
        "date": articles_dates,
        "image_url": articles_imgs,
        "description": articles_descriptions,
        "original_text": content,
    }
    pprint.pprint(article)

# =====================================RUN FUNCTIONS=============================================
