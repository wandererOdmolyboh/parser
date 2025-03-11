import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

from settings import settings

logger = logging.getLogger(__name__)


class Element:

    def __init__(self, href, id):
        self.href = href
        self.id = id


class Post:
    def __init__(self, post_id, url, description, likes, comments, hashtags, has_required_hashtag):
        self.post_id = post_id
        self.url = url
        self.description = description
        self.likes = likes
        self.comments = comments
        self.hashtags = hashtags
        self.has_required_hashtag = has_required_hashtag

    def __repr__(self):
        return f"Post(id={self.post_id}, url={self.url}, description={self.description}, likes={self.likes}, comments={self.comments}, hashtags={self.hashtags}, has_required_hashtag={self.has_required_hashtag})"


def get_instagram_posts(username: str, hashtag: str = None):
    if not hashtag.startswith('#'):
        hashtag = '#' + hashtag

    url = f"https://www.instagram.com/{username}/"
    driver = __get_driver()
    driver.get(url)

    login_instagram(driver, settings.LOGIN, settings.PASSWORD)

    driver.get(url)
    time.sleep(5)

    elements = driver.find_elements(By.CSS_SELECTOR, "a[href^='/nasa/p/']")
    elements = {Element(element.get_attribute('href'), element.id) for element in elements}

    posts = []
    wait = WebDriverWait(driver, 10)

    for i, element in enumerate(elements[:10]):
        try:
            time.sleep(3)
            driver.get(element.href)
            time.sleep(1)

            description = get_description(driver)
            likes_number = get_likes(wait)
            comments = get_count_comments(driver)

            hashtags = get_hash_tag(driver)
            has_hashtag = hashtag in hashtags

            post = Post(
                post_id=element.id,
                url=element.href,
                description=description,
                likes=likes_number,
                comments=comments,
                hashtags=hashtags,
                has_required_hashtag=has_hashtag
            )
            posts.append(post)

        except Exception as e:
            logger.error(f"Error with post {i + 1}: {e}")

    driver.quit()
    return posts


def __get_driver():
    chrome_driver_path = 'C:/Users/dmoly/Downloads/chromedriver-win64/chromedriver.exe'
    service = Service(chrome_driver_path)
    options = Options()

    driver = webdriver.Chrome(service=service, options=options)
    return driver


def login_instagram(driver, username, password):
    driver.get('https://www.instagram.com/')
    wait = WebDriverWait(driver, 10)
    allow_cookies_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(@class, '_a9-- _ap36 _a9_0') and text()='Allow all cookies']")))
    allow_cookies_button.click()

    time.sleep(5)
    __input_form(driver, "username", username)
    __input_form(driver, "password", password)
    time.sleep(10)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()


def __input_form(driver, name, value):
    form_input = driver.find_element(By.NAME, name)
    form_input.clear()
    form_input.send_keys(value)


def get_hash_tag(driver):
    try:
        hashtags_elems = driver.find_elements(By.CSS_SELECTOR, "a[href^='/explore/tags/']")
        hashtags = [tag.text for tag in hashtags_elems]
    except:
        hashtags = []
    return hashtags


def get_likes(wait):
    try:
        outer_span = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                "span.x193iq5w.xeuugli.x1fj9vlw.x13faqbe.x1vvkbs.xt0psk2.x1i0vuye.xvs91rp.x1s688f.x5n08af.x10wh9bi.x1wdrske.x8viiok.x18hxmgj")))
        inner_span = outer_span.find_element(By.CSS_SELECTOR,
                                             "span.html-span.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1hl2dhg.x16tdsg8.x1vvkbs")
        likes_text = inner_span.text
        likes_number = int(likes_text.replace(',', '').strip())
    except:
        likes_number = 0
    return likes_number


def get_count_comments(driver):
    # # Комментарии
    # comments_elems = driver.find_elements(By.CSS_SELECTOR, "ul._a9ym li")
    # comments = len(comments_elems)
    return []


def get_description(driver):
    try:
        description_elem = driver.find_element(By.CSS_SELECTOR, 'h1._ap3a')
        description = description_elem.text if description_elem else ""
    except:
        description = ''
    return description
