from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from Telegram_Msg_File import telegram_bot_sendtext
import pyotp


from kiteconnect import KiteConnect
from time import sleep
import urllib.parse as urlparse
import datetime

from  Zerodha_Credentials import api_key,api_secret,account_username,account_password,totp_key
from  Access_Token import access_token_store

kite = KiteConnect(api_key=api_key)

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

s = Service('C:/chromedriver.exe');
driver = webdriver.Chrome(service=s)


driver.get(kite.login_url())
print(kite.login_url())



form = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="login-form"]')))


driver.find_element(by=By.XPATH, value='//*[@id="userid"]').send_keys(account_username)
driver.find_element(by=By.XPATH, value='//*[@id="password"]').send_keys(account_password)
driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div/div[2]/form/div[4]/button').click()
sleep(1)
form = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="login-form"]//form')))
authkey = pyotp.TOTP(totp_key)

driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div/div[2]/form/div[2]/input').send_keys(authkey.now())
sleep(100)
driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div/div[2]/form/div[3]/button').click()
sleep(1)
current_url = driver.current_url
#driver.quit()
parsed = urlparse.urlparse(current_url)
request_token = urlparse.parse_qs(parsed.query)['request_token'][0]
Access_Token_value = kite.generate_session(request_token=request_token,api_secret=api_secret)['access_token']
access_token_store(Access_Token_value)
now = datetime.datetime.now()
telegram_bot_sendtext("Hi Good Morning, Program Logged in Successfully at "+ str(now)[:-10])
