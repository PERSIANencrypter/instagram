from selenium import webdriver
import requests
from selenium import webdriver
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
fullname = driver.find_element_by_name("fullName").send_keys("ifgodisexistthat is me")
user = driver.find_element_by_name("username").send_keys("vaghti1salamboodgangboodam")
passs = driver.find_element_by_name("password").send_keys("shayan82")
login_elem = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a')
login_elem.click()
#search_bar = driver.findElement(By.tagName("h2"));
#requests.get("https://api.telegram.org/bot5006110630:AAHkhAo0f3zHVt2Qkpg9UOUb1cg7aJ51538/sendMessage?chat_id=-768673029&text="+search_bar)
#search_bar.clear()

#search_bar.send_keys("getting started with python")

#search_bar.send_keys(Keys.RETURN)

#print(driver.current_url)

#driver.close()
