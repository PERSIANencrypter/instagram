import os
import time
import json
import requests
import random
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver.v2 as uc
#driver = uc.Chrome()
chatIdForLog = "-520315918"


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
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#driver=webdriver.Chrome(executable_path = os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

os.system("chmod +x chromedriver")
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.instagram.com/accounts/emailsignup/")
#requests.get("https://api.telegram.org/bot5006110630:AAHkhAo0f3zHVt2Qkpg9UOUb1cg7aJ51538/sendMessage?chat_id="+chatIdForLog+"&text="+driver.title+"1")
time.sleep(5)
requests.get("https://api.telegram.org/bot5006110630:AAHkhAo0f3zHVt2Qkpg9UOUb1cg7aJ51538/sendMessage?chat_id="+chatIdForLog+"&text="+driver.title+"2")
time.sleep(1.5)
requests.get("https://api.telegram.org/bot5006110630:AAHkhAo0f3zHVt2Qkpg9UOUb1cg7aJ51538/sendMessage?chat_id="+chatIdForLog+"&text="+driver.title+"3")
time.sleep(2)
#requests.get("https://api.telegram.org/bot5006110630:AAHkhAo0f3zHVt2Qkpg9UOUb1cg7aJ51538/sendMessage?chat_id="+chatIdForLog+"&text="+emm.text+"¢")
#emailMovaghat = driver.find_element_by_id("mail")
#requests.get("https://api.telegram.org/bot5006110630:AAHkhAo0f3zHVt2Qkpg9UOUb1cg7aJ51538/sendMessage?chat_id="+chatIdForLog+"&text="+emailMovaghat+"4")
#getting mail
url = "https://www.developermail.com/api/v1/mailbox"
fristHeader = {"accept": "application/json"}
createMail = requests.put(url, headers=fristHeader)
time.sleep(4)
struct1 = json.loads(createMail.text)
emailName = struct1["result"]["name"]
time.sleep(1.5)
tokenMail = struct1["result"]["token"]
time.sleep(1.5)
requests.get("https://api.telegram.org/bot5006110630:AAHkhAo0f3zHVt2Qkpg9UOUb1cg7aJ51538/sendMessage?chat_id="+chatIdForLog+"&text="+"this email: "+emailName+"\nwith this token: "+tokenMail+"\n going to be created")
time.sleep(1.5)
emailForSignUp = emailName+"@developermail.com"
time.sleep(3)
email = driver.find_element_by_name("emailOrPhone").send_keys(emailForSignUp)
time.sleep(4)
fristHalf = "Immortal_Guard"
for i in range(8):
	shans = random.randint(0, 9)
	fristHalf += str(shans)

requests.get("https://api.telegram.org/bot5006110630:AAHkhAo0f3zHVt2Qkpg9UOUb1cg7aJ51538/sendMessage?chat_id="+chatIdForLog+"&text="+"this username"+fristHalf+"is going yo be create")
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
time.sleep(25)
#gettin id of email from Instagram
url2 = "https://www.developermail.com/api/v1/mailbox/"+emailName
hdd = {
"accept": "application/json",
"X-MailboxToken": tokenMail
}
reqq = requests.get(url2, headers=hdd)
jsonForId = json.loads(reqq.text)["result"][0]
#getting message body
url3 = "https://www.developermail.com/api/v1/mailbox/"+emailName+"/messages/"+jsonForId
reqqq = requests.get(url3, headers=hdd)
matn = reqqq.text
mm = matn.split("Subject")
mmm = mm[2].split("code")[0].split(" ")
#mmm is final code

time.sleep(4)
user = driver.find_element_by_name("email_confirmation_code").send_keys(mmm[1])
time.sleep(4)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Next']"))).click()
time.sleep(4)
requests.get("https://api.telegram.org/bot5006110630:AAHkhAo0f3zHVt2Qkpg9UOUb1cg7aJ51538/sendMessage?chat_id="+chatIdForLog+"&text="+driver.title+"5"+"\n created")

#search_bar = driver.findElement(By.tagName("h2"));
#requests.get("https://api.telegram.org/bot5006110630:AAHkhAo0f3zHVt2Qkpg9UOUb1cg7aJ51538/sendMessage?chat_id=-768673029&text="+search_bar)

