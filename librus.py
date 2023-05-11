from turtle import title
from webbrowser import Chrome
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os

sciezka = Service('chrome/chromedriver')
chrome_options = Options()
chrome_options.headless = True
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
chrome_options.add_argument('user-agent={0}'.format(user_agent))
driver = webdriver.Chrome(chrome_options=chrome_options, service=sciezka)
driver.implicitly_wait(30)
driver.get("https://portal.librus.pl/rodzina")

# -content = driver.find_element(By.CLASS_NAME, 'themeScrp').text
element = driver.find_element(
    By.XPATH, '/html/body/nav/div/div[1]/div/div[2]/a[3]')
driver.execute_script("arguments[0].click();", element)

element = driver.find_element(
    By.XPATH, '/html/body/nav/div/div[1]/div/div[2]/div/a[2]')
driver.execute_script("arguments[0].click();", element)


driver.switch_to.frame(driver.find_element(By.ID, 'caLoginIframe'))
#driver.find_element(By.XPATH, '//*[@id="Login"]').send_keys('//login//')
#driver.find_element(By.XPATH, '//*[@id="Pass"]').send_keys('//hasło//')
driver.find_element(By.XPATH, '//*[@id="LoginBtn"]').click()


driver.find_element(
    By.XPATH, '//*[@id="centrumPowiadomien"]/div[2]/div[1]/span[2]').click()
numerek = driver.find_element(
    By.XPATH, '//*[@id="user-section"]/span[1]/b').text
wiadomosci = driver.find_element(
    By.XPATH, '//*[@id="graphic-menu"]/ul/li[4]/a[2]').text


def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))


notify("Librus", 'Szczęśliwy numerek to:  '+str(numerek) +
       '\nLiczba nieodczytanych wiadomości: '+str(wiadomosci))
quit()
# //*[@id="graphic-menu"]/ul/li[4]/a[2]
