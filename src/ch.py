import time
from selenium.webdriver.support.ui import WebDriverWait

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

chrome_driver_path = 'C:/Users/dmoly/Downloads/chromedriver-win64/chromedriver.exe'
service = Service(chrome_driver_path)
options = Options()

driver = webdriver.Chrome(service=service, options=options)
driver.get('https://www.instagram.com/')

# Wait for the button to be present and clickable
wait = WebDriverWait(driver, 10)
allow_cookies_button = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//button[contains(@class, '_a9-- _ap36 _a9_0') and text()='Allow all cookies']")))

# Click the button
allow_cookies_button.click()

time.sleep(5)

username_input = driver.find_element(By.NAME, "username")
username_input.clear()
username_input.send_keys('+380665895176')
# username_input.send_keys('d_molyboh')

password_input = driver.find_element(By.NAME, "password")
password_input.clear()
password_input.send_keys('19CVBwer03')

login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()
# password_input = driver.find_element(By.NAME, "password")





log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

# not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()
# not_now_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Не зараз']")))
# not_now_button.click()

time.sleep(5)
not_now_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//div[@role='button' and contains(@class, 'x3nfvp2')]")))
not_now_button.click()
time.sleep(5)

url = f"https://www.instagram.com/nasa/"
driver.get(url)
time.sleep(5)

posts = []
# elements = driver.find_elements(By.CSS_SELECTOR, "article div div div div a")
elements = driver.find_elements(By.CSS_SELECTOR, "a[href^='/nasa/p/']")
hashtag = 'Stars'


class Eelemnts:

    def __init__(self, href, id):
        self.href = href
        self.id = id


elements_set = {Eelemnts(element.get_attribute('href'), element.id) for element in elements}

for i, element in enumerate(elements_set):
    try:
        time.sleep(3)

        driver.get(element.href)

        try:
            description_elem = driver.find_element(By.CSS_SELECTOR, 'h1._ap3a')
            description = description_elem.text if description_elem else ""
        except:
            description = ''

        try:
            outer_span = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                    "span.x193iq5w.xeuugli.x1fj9vlw.x13faqbe.x1vvkbs.xt0psk2.x1i0vuye.xvs91rp.x1s688f.x5n08af.x10wh9bi.x1wdrske.x8viiok.x18hxmgj")))
            inner_span = outer_span.find_element(By.CSS_SELECTOR,
                                                 "span.html-span.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1hl2dhg.x16tdsg8.x1vvkbs")
            # Extract the text value
            likes_text = inner_span.text
            likes_number = int(likes_text.replace(',', '').strip())
        except:
            likes_number = 0

        # # Комментарии
        # comments_elems = driver.find_elements(By.CSS_SELECTOR, "ul._a9ym li")
        # comments = len(comments_elems)

        try:
            hashtags_elems = driver.find_elements(By.CSS_SELECTOR, "a[href^='/explore/tags/']")
            hashtags = [tag.text for tag in hashtags_elems]
        except:
            hashtags = []
        # Проверяем нужный хэштег
        if not hashtag.startswith('#'):
            hashtag = '#' + hashtag
        has_hashtag = hashtag in hashtags

        posts.append({
            "id": element.id,
            "url": element.href,
            "description": description,
            "likes": likes_number,
            # "comments": comments,
            "hashtags": hashtags,
            "has_required_hashtag": has_hashtag
        })

        print(f"[✔] Пост {i + 1} собран")

    except Exception as e:
        print(f"[❌] Ошибка с постом {i + 1}: {e}")

driver.quit()

# Вывод результата
for post in posts:
    print(post)

print()
print(posts)
time.sleep(30)
time.sleep(30)

driver.quit()
# from bs4 import BeautifulSoup
# html = '<h1 class="_ap3a _aaco _aacu _aacx _aad7 _aade" dir="auto">Looking at the big picture 🔭<br><br>This 100-million-year-old star cluster is brought to us with data from not one, but a trio of telescopes. Visible in the constellation Dorado and located within the Large Magellanic Cloud – this smaller neighbor galaxy to the Milky Way – NGC 1850 is about 63,000 times the mass of our Sun, and its core is roughly 20 light-years in diameter.<br><br>Data from each of the three telescopes can be identified by their colors. X-rays from <a class="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz notranslate _a6hd" href="/ChandraXray/" role="link" tabindex="0">@ChandraXray</a> are magenta, while optical wavelengths from <a class="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz notranslate _a6hd" href="/NASAHubble/" role="link" tabindex="0">@NASAHubble</a> are in red, yellow, green, cyan, and blue. Infrared energy from the Spitzer Space Telescope is also in red.<br><br>Image description: A blue tinted cloud in space is surrounded by several neon purple dots. Bright golden stars fill the upper center of the image. Extending beyond the upper and lower edges of the image, the cloud resembles wafting smoke.<br><br>Credit: X-ray: NASA/CXC/SAO; Infrared: NASA/ESA/CSA/STScI; Image Processing: NASA/CXC/SAO/J. Major, S. Wolk<br><br><a class="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz  _aa9_ _a6hd" href="/explore/tags/nasa/" role="link" tabindex="0">#NASA</a> <a class="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz  _aa9_ _a6hd" href="/explore/tags/space/" role="link" tabindex="0">#Space</a> <a class="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz  _aa9_ _a6hd" href="/explore/tags/astronomy/" role="link" tabindex="0">#Astronomy</a> <a class="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz  _aa9_ _a6hd" href="/explore/tags/telescope/" role="link" tabindex="0">#Telescope</a> <a class="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz  _aa9_ _a6hd" href="/explore/tags/starcluster/" role="link" tabindex="0">#StarCluster</a> <a class="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz  _aa9_ _a6hd" href="/explore/tags/stars/" role="link" tabindex="0">#Stars</a> <a class="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz  _aa9_ _a6hd" href="/explore/tags/perspective/" role="link" tabindex="0">#Perspective</a></h1>'
#
# soup = BeautifulSoup(html, "html.parser")
#
# # Найти все ссылки <a>, у которых есть "/explore/tags/" в href
# hashtags = [a.get_text() for a in soup.find_all("a", href=True) if "/explore/tags/" in a["href"]]

print(hashtags)
