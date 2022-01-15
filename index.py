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
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver.v2 as uc
driver = uc.Chrome()


options = Options()
#options = webdriver.ChromeOptions()
options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
#chrome_options.add_argument('--no-sandbox')
#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--disable-gpu')
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#driver=webdriver.Chrome(executable_path = os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

os.system("chmod +x chromedriver")
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.instagram.com/accounts/emailsignup/")
#requests.get("https://api.telegram.org/bot5006110630:AAHkhAo0f3zHVt2Qkpg9UOUb1cg7aJ51538/sendMessage?chat_id=-520315918&text="+driver.title+"1")
driver.execute_script("window.open('about:blank', 'ftab');")
driver.switch_to.window("ftab")

driver.get("https://www.instagram.com/accounts/emailsignup/")
time.sleep(5)
requests.get("https://api.telegram.org/bot5006110630:AAHkhAo0f3zHVt2Qkpg9UOUb1cg7aJ51538/sendMessage?chat_id=-520315918&text="+driver.title+"2")
#going get email
driver.execute_script("window.open('about:blank', 'secondtab');")
driver.switch_to.window("secondtab")
driver.get('https://mail.tm/en/')
time.sleep(4)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='accounts-menu']"))).click()
time.sleep(4)
emm = driver.find_element_by_css_selector('p[class="dark:text-gray-300 text-gray-900 text-sm font-medium leading-5 cursor-pointer select-all truncate"]')
time.sleep(1.5)
requests.get("https://api.telegram.org/bot5006110630:AAHkhAo0f3zHVt2Qkpg9UOUb1cg7aJ51538/sendMessage?chat_id=-520315918&text="+driver.title+"3")
time.sleep(1.5)
requests.get("https://api.telegram.org/bot5006110630:AAHkhAo0f3zHVt2Qkpg9UOUb1cg7aJ51538/sendMessage?chat_id=-520315918&text="+emm.text+"¢")
#emailMovaghat = driver.find_element_by_id("mail")
#requests.get("https://api.telegram.org/bot5006110630:AAHkhAo0f3zHVt2Qkpg9UOUb1cg7aJ51538/sendMessage?chat_id=-520315918&text="+emailMovaghat+"4")
#requests.get("https://api.telegram.org/bot5006110630:AAHkhAo0f3zHVt2Qkpg9UOUb1cg7aJ51538/sendMessage?chat_id=-520315918&text="+emailMovaghat+"4")
m = str(emm.text)

driver.switch_to.window("ftab")
time.sleep(9)
email = driver.find_element_by_name("emailOrPhone").send_keys(m)
time.sleep(4)
fristHalf = "Immortal_Guard"
for i in range(8):
	shans = random.randint(0, 9)
	fristHalf += str(shans)

time.sleep(2)
fullname = driver.find_element_by_name("fullName").send_keys("Immortal")
time.sleep(4)
user = driver.find_element_by_name("username").send_keys(fristHalf)
time.sleep(4)
passs = driver.find_element_by_name("password").send_keys("im@a@normal@person9956iswear")
time.sleep(4)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Sign up']"))).click()
time.sleep(5)
selectm = Select(driver.find_element_by_css_selector('select[title="Month:"]'))
time.sleep(4)
selectd = Select(driver.find_element_by_css_selector('select[title="Day:"]'))
time.sleep(4)
selecty = Select(driver.find_element_by_css_selector('select[title="Year:"]'))
time.sleep(4)
selectm.select_by_value('5')
time.sleep(4)
selectd.select_by_value('10')
time.sleep(4)
selecty.select_by_value('1990')
time.sleep(4)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Next']"))).click()
time.sleep(30)
driver.switch_to.window("secondtab")
time.sleep(10)
#WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='accounts-menu']"))).click()
time.sleep(8)
driver.get('https://mail.tm/en/')

time.sleep(10)
driver.find_element_by_css_selector("span[calss='truncate']").click()
time.sleep(3)
#WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='accounts-menu']"))).click()
time.sleep(4)
emmm = driver.find_element_by_css_selector('p[class="dark:text-gray-300 text-gray-900 text-sm font-medium leading-5 cursor-pointer select-all truncate"]')
time.sleep(4)
requests.get("https://api.telegram.org/bot5006110630:AAHkhAo0f3zHVt2Qkpg9UOUb1cg7aJ51538/sendMessage?chat_id=-520315918&text="+emmm.text)
requests.get("https://api.telegram.org/bot5006110630:AAHkhAo0f3zHVt2Qkpg9UOUb1cg7aJ51538/sendMessage?chat_id=-520315918&text="+driver.title+"5")
time.sleep(4)

#search_bar = driver.findElement(By.tagName("h2"));
#requests.get("https://api.telegram.org/bot5006110630:AAHkhAo0f3zHVt2Qkpg9UOUb1cg7aJ51538/sendMessage?chat_id=-768673029&text="+search_bar)

