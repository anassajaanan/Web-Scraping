from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from csv import writer
import pprint
import time

# ========================================config===================================
op = Options()
op.add_extension('config/pay.crx')
op.add_extension('config/uorigin.crx')
op.add_extension('config/cockies.crx')
PATH = 'config/chromedriver.exe'
cc = DesiredCapabilities.CHROME
cc["pageLoadStrategy"] = "none"
headers = {
    "Accept-Language": "en-US,en;q=0.5",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/108.0.0.0 Safari/537.36"
}


# ===========================================CRYPTOCURRENCY===================================================
def export_cryptocurrency():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    CRYPTOCURRENCY_URL = "https://www.washingtonpost.com/business/cryptocurrency/?itid=nb_business_cryptocurrency"
    driver.get(CRYPTOCURRENCY_URL)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h3')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(4)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'story-headline')))
    articles = driver.find_elements(By.CLASS_NAME, 'story-headline')
    time.sleep(1)
    articles_links = [article.find_element(By.CLASS_NAME, 'flex').get_attribute('href') for article in articles]
    titles = [article.find_element(By.TAG_NAME, 'h3').text for article in articles]
    descriptions = [article.find_element(By.TAG_NAME, 'p').text for article in articles]
    dates = driver.find_elements(By.CSS_SELECTOR, '.story-headline .font-xxxs')
    dates = [date.text for date in dates]
    authors = []

    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'wpds-c-knSWeD')))
    for i in range(len(articles)):
        article = articles[i]
        author = article.find_elements(By.CLASS_NAME, 'wpds-c-knSWeD')
        author = [item.text + " " for item in author]
        author = [item for item in author if author.index(item) % 2 != 0]
        author = "".join(author)
        authors.append(author)

    for i in range(len(articles_links)):
        driver.get(articles_links[i])
        w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
        time.sleep(2)

        driver.execute_script("window.scrollTo(0, 500)")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, 1000)")
        time.sleep(1)
        article_type = "CRYPTOCURRENCY"
        w.until(EC.presence_of_element_located((By.CLASS_NAME, 'wpds-c-cYdRxM')))
        text = driver.find_elements(By.CLASS_NAME, 'wpds-c-cYdRxM')
        content = [paragraph.text + "\n" for paragraph in text]
        content = "".join(content)

        with open('cryptocurrency.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [articles_links[i], titles[i], authors[i], dates[i], article_type, descriptions[i], content]
            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_cryptocurrency():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    CRYPTOCURRENCY_URL = "https://www.washingtonpost.com/business/cryptocurrency/?itid=nb_business_cryptocurrency"
    driver.get(CRYPTOCURRENCY_URL)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h3')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(4)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'story-headline')))
    article = driver.find_element(By.CLASS_NAME, 'story-headline')

    article_link = article.find_element(By.CLASS_NAME, 'flex').get_attribute('href')
    title = article.find_element(By.TAG_NAME, 'h3').text
    description = article.find_element(By.TAG_NAME, 'p').text
    date = driver.find_element(By.CSS_SELECTOR, '.story-headline .font-xxxs').text

    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'wpds-c-knSWeD')))
    author = article.find_elements(By.CLASS_NAME, 'wpds-c-knSWeD')
    author = [item.text + " " for item in author]
    author = [item for item in author if author.index(item) % 2 != 0]
    author = "".join(author)

    driver.get(article_link)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
    time.sleep(2)

    driver.execute_script("window.scrollTo(0, 500)")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 1000)")
    time.sleep(1)
    article_type = "CRYPTOCURRENCY"
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'wpds-c-cYdRxM')))
    original_text = driver.find_elements(By.CLASS_NAME, 'wpds-c-cYdRxM')
    content = [paragraph.text + "\n" for paragraph in original_text]
    content = "".join(content)

    article = {
        "post_category": article_type,
        "news_url": article_link,
        "title": title,
        "author": author,
        "date": date,
        "description": description,
        "original_text": content,
    }
    pprint.pprint(article)


# ===========================================ECONOMIC POLICY===================================================
def export_economic_policy():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    ECONOMIC_POLICY_URL = "https://www.washingtonpost.com/economic-policy/?itid=nb_business_economic-policy"
    driver.get(ECONOMIC_POLICY_URL)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h3')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(4)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'story-headline')))
    articles = driver.find_elements(By.CLASS_NAME, 'story-headline')
    time.sleep(1)
    articles_links = [article.find_element(By.CLASS_NAME, 'flex').get_attribute('href') for article in articles]
    titles = [article.find_element(By.TAG_NAME, 'h3').text for article in articles]
    descriptions = [article.find_element(By.TAG_NAME, 'p').text for article in articles]
    dates = driver.find_elements(By.CSS_SELECTOR, '.story-headline .font-xxxs')
    dates = [date.text for date in dates]
    authors = []

    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'wpds-c-knSWeD')))
    for i in range(len(articles)):
        article = articles[i]
        author = article.find_elements(By.CLASS_NAME, 'wpds-c-knSWeD')
        author = [item.text + " " for item in author]
        author = [item for item in author if author.index(item) % 2 != 0]
        author = "".join(author)
        authors.append(author)

    for i in range(len(articles_links)):
        driver.get(articles_links[i])
        w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
        time.sleep(2)

        driver.execute_script("window.scrollTo(0, 500)")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, 1000)")
        time.sleep(1)
        article_type = "ECONOMIC POLICY"
        w.until(EC.presence_of_element_located((By.CLASS_NAME, 'wpds-c-cYdRxM')))
        text = driver.find_elements(By.CLASS_NAME, 'wpds-c-cYdRxM')
        content = [paragraph.text + "\n" for paragraph in text]
        content = "".join(content)

        with open('economic policy.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [articles_links[i], titles[i], authors[i], dates[i], article_type, descriptions[i], content]
            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_economic_policy():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    ECONOMIC_POLICY_URL = "https://www.washingtonpost.com/economic-policy/?itid=nb_business_economic-policy"
    driver.get(ECONOMIC_POLICY_URL)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h3')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(4)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'story-headline')))
    article = driver.find_element(By.CLASS_NAME, 'story-headline')

    article_link = article.find_element(By.CLASS_NAME, 'flex').get_attribute('href')
    title = article.find_element(By.TAG_NAME, 'h3').text
    description = article.find_element(By.TAG_NAME, 'p').text
    date = driver.find_element(By.CSS_SELECTOR, '.story-headline .font-xxxs').text

    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'wpds-c-knSWeD')))
    author = article.find_elements(By.CLASS_NAME, 'wpds-c-knSWeD')
    author = [item.text + " " for item in author]
    author = [item for item in author if author.index(item) % 2 != 0]
    author = "".join(author)

    driver.get(article_link)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
    time.sleep(2)

    driver.execute_script("window.scrollTo(0, 500)")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 1000)")
    time.sleep(1)
    article_type = "ECONOMIC POLICY"
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'wpds-c-cYdRxM')))
    original_text = driver.find_elements(By.CLASS_NAME, 'wpds-c-cYdRxM')
    content = [paragraph.text + "\n" for paragraph in original_text]
    content = "".join(content)

    article = {
        "post_category": article_type,
        "news_url": article_link,
        "title": title,
        "author": author,
        "date": date,
        "description": description,
        "original_text": content,
    }
    pprint.pprint(article)


# ===========================================ECONOMY===================================================
def export_economy():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    ECONOMY_URL = "https://www.washingtonpost.com/economy/?itid=nb_business_economy"
    driver.get(ECONOMY_URL)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h3')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(4)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'story-headline')))
    articles = driver.find_elements(By.CLASS_NAME, 'story-headline')
    time.sleep(1)
    articles_links = [article.find_element(By.CLASS_NAME, 'flex').get_attribute('href') for article in articles]
    titles = [article.find_element(By.TAG_NAME, 'h3').text for article in articles]
    descriptions = [article.find_element(By.TAG_NAME, 'p').text for article in articles]
    dates = driver.find_elements(By.CSS_SELECTOR, '.story-headline .font-xxxs')
    dates = [date.text for date in dates]
    authors = []

    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'wpds-c-knSWeD')))
    for i in range(len(articles)):
        article = articles[i]
        author = article.find_elements(By.CLASS_NAME, 'wpds-c-knSWeD')
        author = [item.text + " " for item in author]
        author = [item for item in author if author.index(item) % 2 != 0]
        author = "".join(author)
        authors.append(author)

    for i in range(len(articles_links)):
        driver.get(articles_links[i])
        w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
        time.sleep(2)

        driver.execute_script("window.scrollTo(0, 500)")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, 1000)")
        time.sleep(1)
        article_type = "ECONOMY"

        try:
            text = driver.find_elements(By.CLASS_NAME, 'wpds-c-cYdRxM')
            content = [paragraph.text + "\n" for paragraph in text]
            content = "".join(content)
        except:
            text = driver.find_elements(By.TAG_NAME, 'p')
            content = [paragraph.text + "\n" for paragraph in text]
            content = "".join(content)
        if len(descriptions[i]) == 0:
            descriptions[i] = 'NOT FOUND'
        if len(content) == 0:
            content = 'NOT FOUND'

        with open('economy.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [articles_links[i], titles[i], authors[i], dates[i], article_type, descriptions[i], content]
            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_economy():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    ECONOMY_URL = "https://www.washingtonpost.com/economy/?itid=nb_business_economy"
    driver.get(ECONOMY_URL)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h3')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(4)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'story-headline')))
    article = driver.find_element(By.CLASS_NAME, 'story-headline')

    article_link = article.find_element(By.CLASS_NAME, 'flex').get_attribute('href')
    title = article.find_element(By.TAG_NAME, 'h3').text
    description = article.find_element(By.TAG_NAME, 'p').text
    date = driver.find_element(By.CSS_SELECTOR, '.story-headline .font-xxxs').text

    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'wpds-c-knSWeD')))
    author = article.find_elements(By.CLASS_NAME, 'wpds-c-knSWeD')
    author = [item.text + " " for item in author]
    author = [item for item in author if author.index(item) % 2 != 0]
    author = "".join(author)

    driver.get(article_link)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
    time.sleep(2)

    driver.execute_script("window.scrollTo(0, 500)")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 1000)")
    time.sleep(1)
    article_type = "ECONOMY"
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'wpds-c-cYdRxM')))
    original_text = driver.find_elements(By.CLASS_NAME, 'wpds-c-cYdRxM')
    content = [paragraph.text + "\n" for paragraph in original_text]
    content = "".join(content)

    article = {
        "post_category": article_type,
        "news_url": article_link,
        "title": title,
        "author": author,
        "date": date,
        "description": description,
        "original_text": content,
    }
    pprint.pprint(article)


# ===========================================ENERGY===================================================
def export_energy():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    ENERGY_URL = "https://www.washingtonpost.com/energy/?itid=nb_business_energy"
    driver.get(ENERGY_URL)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h3')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(4)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'story-headline')))
    articles = driver.find_elements(By.CLASS_NAME, 'story-headline')
    time.sleep(1)
    articles_links = [article.find_element(By.CLASS_NAME, 'flex').get_attribute('href') for article in articles]
    titles = [article.find_element(By.TAG_NAME, 'h3').text for article in articles]
    descriptions = [article.find_element(By.TAG_NAME, 'p').text for article in articles]
    dates = driver.find_elements(By.CSS_SELECTOR, '.story-headline .font-xxxs')
    dates = [date.text for date in dates]
    authors = []

    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'wpds-c-knSWeD')))
    for i in range(len(articles)):
        article = articles[i]
        author = article.find_elements(By.CLASS_NAME, 'wpds-c-knSWeD')
        author = [item.text + " " for item in author]
        author = [item for item in author if author.index(item) % 2 != 0]
        author = "".join(author)
        authors.append(author)

    for i in range(len(articles_links)):
        driver.get(articles_links[i])
        w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
        time.sleep(2)

        driver.execute_script("window.scrollTo(0, 500)")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, 1000)")
        time.sleep(1)
        article_type = "ENERGY"
        time.sleep(1)
        text = driver.find_elements(By.CLASS_NAME, 'wpds-c-cYdRxM')
        content = [paragraph.text + "\n" for paragraph in text]
        content = "".join(content)

        if len(descriptions[i]) == 0:
            descriptions[i] = 'NOT FOUND'
        if len(content) == 0:
            content = 'NOT FOUND'

        with open('energy.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [articles_links[i], titles[i], authors[i], dates[i], article_type, descriptions[i], content]
            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_energy():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    ENERGY_URL = "https://www.washingtonpost.com/energy/?itid=nb_business_energy"
    driver.get(ENERGY_URL)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h3')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(4)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'story-headline')))
    article = driver.find_element(By.CLASS_NAME, 'story-headline')

    article_link = article.find_element(By.CLASS_NAME, 'flex').get_attribute('href')
    title = article.find_element(By.TAG_NAME, 'h3').text
    description = article.find_element(By.TAG_NAME, 'p').text
    date = driver.find_element(By.CSS_SELECTOR, '.story-headline .font-xxxs').text

    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'wpds-c-knSWeD')))
    author = article.find_elements(By.CLASS_NAME, 'wpds-c-knSWeD')
    author = [item.text + " " for item in author]
    author = [item for item in author if author.index(item) % 2 != 0]
    author = "".join(author)

    driver.get(article_link)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
    time.sleep(2)

    driver.execute_script("window.scrollTo(0, 500)")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 1000)")
    time.sleep(1)
    article_type = "ENERGY"
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'wpds-c-cYdRxM')))
    original_text = driver.find_elements(By.CLASS_NAME, 'wpds-c-cYdRxM')
    content = [str(paragraph.text) + "\n" for paragraph in original_text]
    content = "".join(content)

    article = {
        "post_category": article_type,
        "news_url": article_link,
        "title": title,
        "author": author,
        "date": date,
        "description": description,
        "original_text": content,
    }
    pprint.pprint(article)


# ===========================================HEALTH CARE===================================================
def export_health_care():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    HEALTH_CARE_URL = "https://www.washingtonpost.com/health-care/?itid=nb_business_health-care"
    driver.get(HEALTH_CARE_URL)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h3')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(4)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'story-headline')))
    articles = driver.find_elements(By.CLASS_NAME, 'story-headline')
    time.sleep(1)
    articles_links = [article.find_element(By.CLASS_NAME, 'flex').get_attribute('href') for article in articles]
    titles = [article.find_element(By.TAG_NAME, 'h3').text for article in articles]
    descriptions = [article.find_element(By.TAG_NAME, 'p').text for article in articles]
    dates = driver.find_elements(By.CSS_SELECTOR, '.story-headline .font-xxxs')
    dates = [date.text for date in dates]
    authors = []

    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'wpds-c-knSWeD')))
    for i in range(len(articles)):
        article = articles[i]
        author = article.find_elements(By.CLASS_NAME, 'wpds-c-knSWeD')
        author = [item.text + " " for item in author]
        author = [item for item in author if author.index(item) % 2 != 0]
        author = "".join(author)
        authors.append(author)

    for i in range(len(articles_links)):
        driver.get(articles_links[i])
        w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
        time.sleep(2)

        driver.execute_script("window.scrollTo(0, 500)")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, 1000)")
        time.sleep(1)
        article_type = "HEALTH CARE"
        time.sleep(1)
        text = driver.find_elements(By.CLASS_NAME, 'wpds-c-cYdRxM')
        content = [paragraph.text + "\n" for paragraph in text]
        content = "".join(content)

        if len(descriptions[i]) == 0:
            descriptions[i] = 'NOT FOUND'
        if len(content) == 0:
            content = 'NOT FOUND'

        with open('health care.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [articles_links[i], titles[i], authors[i], dates[i], article_type, descriptions[i], content]
            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_health_care():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    HEALTH_CARE_URL = "https://www.washingtonpost.com/health-care/?itid=nb_business_health-care"
    driver.get(HEALTH_CARE_URL)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h3')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(4)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'story-headline')))
    article = driver.find_element(By.CLASS_NAME, 'story-headline')

    article_link = article.find_element(By.CLASS_NAME, 'flex').get_attribute('href')
    title = article.find_element(By.TAG_NAME, 'h3').text
    description = article.find_element(By.TAG_NAME, 'p').text
    date = driver.find_element(By.CSS_SELECTOR, '.story-headline .font-xxxs').text

    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'wpds-c-knSWeD')))
    author = article.find_elements(By.CLASS_NAME, 'wpds-c-knSWeD')
    author = [item.text + " " for item in author]
    author = [item for item in author if author.index(item) % 2 != 0]
    author = "".join(author)

    driver.get(article_link)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
    time.sleep(2)

    driver.execute_script("window.scrollTo(0, 500)")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 1000)")
    time.sleep(1)
    article_type = "HEALTH CARE"
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'wpds-c-cYdRxM')))
    original_text = driver.find_elements(By.CLASS_NAME, 'wpds-c-cYdRxM')
    content = [str(paragraph.text) + "\n" for paragraph in original_text]
    content = "".join(content)

    article = {
        "post_category": article_type,
        "news_url": article_link,
        "title": title,
        "author": author,
        "date": date,
        "description": description,
        "original_text": content,
    }
    pprint.pprint(article)


# ===========================================PERSONAL FINANCE===================================================
def export_personal_finance():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    PERSONAL_FINANCE_URL = "https://www.washingtonpost.com/personal-finance/?itid=nb_business_personal-finance"
    driver.get(PERSONAL_FINANCE_URL)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h3')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(4)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'story-headline')))
    articles = driver.find_elements(By.CLASS_NAME, 'story-headline')
    time.sleep(1)
    articles_links = [article.find_element(By.CLASS_NAME, 'flex').get_attribute('href') for article in articles]
    titles = [article.find_element(By.TAG_NAME, 'h3').text for article in articles]
    descriptions = [article.find_element(By.TAG_NAME, 'p').text for article in articles]
    dates = driver.find_elements(By.CSS_SELECTOR, '.story-headline .font-xxxs')
    dates = [date.text for date in dates]
    authors = []

    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'wpds-c-knSWeD')))
    for i in range(len(articles)):
        article = articles[i]
        author = article.find_elements(By.CLASS_NAME, 'wpds-c-knSWeD')
        author = [item.text + " " for item in author]
        author = [item for item in author if author.index(item) % 2 != 0]
        author = "".join(author)
        authors.append(author)

    for i in range(len(articles_links)):
        driver.get(articles_links[i])
        w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
        time.sleep(2)

        driver.execute_script("window.scrollTo(0, 500)")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, 1000)")
        time.sleep(1)
        article_type = "PERSONAL FINANCE"
        time.sleep(1)
        text = driver.find_elements(By.CLASS_NAME, 'wpds-c-cYdRxM')
        content = [paragraph.text + "\n" for paragraph in text]
        content = "".join(content)

        if len(descriptions[i]) == 0:
            descriptions[i] = 'NOT FOUND'
        if len(content) == 0:
            content = 'NOT FOUND'

        with open('personal finance.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [articles_links[i], titles[i], authors[i], dates[i], article_type, descriptions[i], content]
            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_personal_finance():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    PERSONAL_FINANCE_URL = "https://www.washingtonpost.com/personal-finance/?itid=nb_business_personal-finance"
    driver.get(PERSONAL_FINANCE_URL)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h3')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(4)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'story-headline')))
    article = driver.find_element(By.CLASS_NAME, 'story-headline')

    article_link = article.find_element(By.CLASS_NAME, 'flex').get_attribute('href')
    title = article.find_element(By.TAG_NAME, 'h3').text
    description = article.find_element(By.TAG_NAME, 'p').text
    date = driver.find_element(By.CSS_SELECTOR, '.story-headline .font-xxxs').text

    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'wpds-c-knSWeD')))
    author = article.find_elements(By.CLASS_NAME, 'wpds-c-knSWeD')
    author = [item.text + " " for item in author]
    author = [item for item in author if author.index(item) % 2 != 0]
    author = "".join(author)

    driver.get(article_link)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
    time.sleep(2)

    driver.execute_script("window.scrollTo(0, 500)")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 1000)")
    time.sleep(1)
    article_type = "PERSONAL FINANCE"
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'wpds-c-cYdRxM')))
    original_text = driver.find_elements(By.CLASS_NAME, 'wpds-c-cYdRxM')
    content = [str(paragraph.text) + "\n" for paragraph in original_text]
    content = "".join(content)

    article = {
        "post_category": article_type,
        "news_url": article_link,
        "title": title,
        "author": author,
        "date": date,
        "description": description,
        "original_text": content,
    }
    pprint.pprint(article)


# ===========================================SMALL BUSINESS===================================================
def export_small_business():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    SMALL_BUSINESS_URL = "https://www.washingtonpost.com/business/on-small-business/?itid=nb_business_small-business"
    driver.get(SMALL_BUSINESS_URL)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h3')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(4)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'story-headline')))
    articles = driver.find_elements(By.CLASS_NAME, 'story-headline')
    time.sleep(1)
    articles_links = [article.find_element(By.CLASS_NAME, 'flex').get_attribute('href') for article in articles]
    titles = [article.find_element(By.TAG_NAME, 'h3').text for article in articles]
    descriptions = [article.find_element(By.TAG_NAME, 'p').text for article in articles]
    dates = driver.find_elements(By.CSS_SELECTOR, '.story-headline .font-xxxs')
    dates = [date.text for date in dates]
    authors = []

    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'wpds-c-knSWeD')))
    for i in range(len(articles)):
        article = articles[i]
        author = article.find_elements(By.CLASS_NAME, 'wpds-c-knSWeD')
        author = [item.text + " " for item in author]
        author = [item for item in author if author.index(item) % 2 != 0]
        author = "".join(author)
        authors.append(author)

    for i in range(len(articles_links)):
        driver.get(articles_links[i])
        w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
        time.sleep(2)

        driver.execute_script("window.scrollTo(0, 500)")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, 1000)")
        time.sleep(1)
        article_type = "SMALL BUSINESS"
        time.sleep(1)
        text = driver.find_elements(By.CLASS_NAME, 'wpds-c-cYdRxM')
        content = [paragraph.text + "\n" for paragraph in text]
        content = "".join(content)

        if len(descriptions[i]) == 0:
            descriptions[i] = 'NOT FOUND'
        if len(content) == 0:
            content = 'NOT FOUND'

        with open('small business.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [articles_links[i], titles[i], authors[i], dates[i], article_type, descriptions[i], content]
            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_small_business():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    SMALL_BUSINESS_URL = "https://www.washingtonpost.com/business/on-small-business/?itid=nb_business_small-business"
    driver.get(SMALL_BUSINESS_URL)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h3')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(4)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'story-headline')))
    article = driver.find_element(By.CLASS_NAME, 'story-headline')

    article_link = article.find_element(By.CLASS_NAME, 'flex').get_attribute('href')
    title = article.find_element(By.TAG_NAME, 'h3').text
    description = article.find_element(By.TAG_NAME, 'p').text
    date = driver.find_element(By.CSS_SELECTOR, '.story-headline .font-xxxs').text

    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'wpds-c-knSWeD')))
    author = article.find_elements(By.CLASS_NAME, 'wpds-c-knSWeD')
    author = [item.text + " " for item in author]
    author = [item for item in author if author.index(item) % 2 != 0]
    author = "".join(author)

    driver.get(article_link)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
    time.sleep(2)

    driver.execute_script("window.scrollTo(0, 500)")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 1000)")
    time.sleep(1)
    article_type = "SMALL BUSINESS"
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'wpds-c-cYdRxM')))
    original_text = driver.find_elements(By.CLASS_NAME, 'wpds-c-cYdRxM')
    content = [str(paragraph.text) + "\n" for paragraph in original_text]
    content = "".join(content)

    article = {
        "post_category": article_type,
        "news_url": article_link,
        "title": title,
        "author": author,
        "date": date,
        "description": description,
        "original_text": content,
    }
    pprint.pprint(article)

# ========================================RUN FUNCTION=========================================
