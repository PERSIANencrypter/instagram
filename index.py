from selenium import webdriver
import requests
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("start-maximized")
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
#chrome_options.add_argument('--no-sandbox')
#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#driver=webdriver.Chrome(executable_path = os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

from selenium.webdriver.common.keys import Keys
import os
os.system("chmod +x chromedriver")
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#driver = webdriver.Chrome('./chromedriver')

driver.get("https://www.instagram.com/accounts/emailsignup/")
#driver.get("https://www.google.com")

print(driver.title)
requests.get("https://api.telegram.org/bot5006110630:AAHkhAo0f3zHVt2Qkpg9UOUb1cg7aJ51538/sendMessage?chat_id=-768673029&text="+driver.title)

#fnam = driver.find_element_by_css_selector("form input[arial-label=Username]")
email = driver.find_element_by_name("emailOrPhone").send_keys("gholamisadegh76@gmail.com")
fullname = driver.find_element_by_name("fullName").send_keys("ifgoke")
user = driver.find_element_by_name("username").send_keys("vaghtsodidjem")
passs = driver.find_element_by_name("password").send_keys("shjsdkw9128ADGOH@@+")
#login_elem = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a')
#login_elem = driver.find_element_by_css_selector("button[type=submit]")
#login_elem.click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Sign up']"))).click()
time.sleep(5)
#select = Select(driver.find_element_by_xpath("//select[@title=Month]"))
selectm = Select(driver.find_element_by_css_selector('select[title="Month:"]'))
selectd = Select(driver.find_element_by_css_selector('select[title="Day:"]'))
selecty = Select(driver.find_element_by_css_selector('select[title="Year:"]'))
selectm.select_by_value('5')
selectd.select_by_value('10')
selecty.select_by_value('1970')
#search_bar = driver.findElement(By.tagName("h2"));
#requests.get("https://api.telegram.org/bot5006110630:AAHkhAo0f3zHVt2Qkpg9UOUb1cg7aJ51538/sendMessage?chat_id=-768673029&text="+search_bar)

