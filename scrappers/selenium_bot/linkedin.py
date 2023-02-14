from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pathlib import Path
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import schedule
import time as t
import random
import pyautogui
BASE_DIR = Path(__file__).resolve().parent
chrome_path = f"{BASE_DIR}/chromedriver.exe"
chrome_options = Options()
chrome_options.add_extension('leadleaper.crx')
chrome_service = Service(executable_path=chrome_path)
# driver = uc.Chrome()
driver = webdriver.Chrome(options=chrome_options, service=chrome_service)
driver.maximize_window()
wait = WebDriverWait(driver, 10)
profile_links = []
usernames = []
data = {}

fake_accounts = ['foluvuce@finews.biz', 'dipohe4793@breazeim.com']

def Login():
    driver.get('https://www.linkedin.com/m/logout')
    t.sleep(5)
    random_username2 = random.choice(fake_accounts)
    username = driver.find_element(By.XPATH, "//input[@autocomplete='username']")
    username.send_keys(random_username2)
    t.sleep(5)
    password = driver.find_element(By.XPATH, "//input[@autocomplete='current-password']")
    password.send_keys("Sahildhiman_007")
    t.sleep(3)
    driver.find_element(By.XPATH, "//button[@class='sign-in-form__submit-button']").click()
try:
    t.sleep(30)
    pyautogui.hotkey('ctrl', 'l')
    t.sleep(5)
    parent = driver.current_window_handle
    print(parent)
    handles = driver.window_handles
    print(handles)
    for ha in handles[1:]:
        driver.switch_to.window(ha)
        try:
            print("selenium switched to next driver")
            print(driver.title)
            driver.find_element(By.XPATH, "//a[@id='exUsr']").click()
            t.sleep(3)
            user_email = driver.find_element(By.XPATH, "//input[@id='ue']")
            user_email.send_keys('sahildhiman@zestgeek.com')
            password = driver.find_element(By.XPATH, "//input[@id='pw']")
            password.send_keys('sahildhiman_007')
            driver.find_element(By.XPATH, "//button[@id='signBtn']").click()
            checkbox = driver.find_element(By.XPATH, "//input[@id='llTC']").click()
            submit_button = driver.find_element(By.XPATH, "//button[@id='signBtn']").click()
            t.sleep(10)
            driver.close()
            driver.switch_to.window(parent)
        except:
            print('Leadleaper account not able to login')
    driver.get(url='https://www.linkedin.com')
    driver.implicitly_wait(10)
    random_username = random.choice(fake_accounts)
    username = driver.find_element(By.XPATH, "//input[@autocomplete='username']")
    username.send_keys(random_username)
    t.sleep(5)
    password = driver.find_element(By.XPATH, "//input[@autocomplete='current-password']")
    password.send_keys("Sahildhiman_007")
    t.sleep(3)
    sign_in = driver.find_element(By.XPATH, "//button[@class='sign-in-form__submit-button']").click()
    t.sleep(5)
    driver.get("https://www.linkedin.com/feed/update/urn:li:activity:7025757036814417920/")
    t.sleep(5)
    driver.execute_script("window.scrollTo(0, 600)")
    driver.find_element(By.XPATH, "//span[@class='social-details-social-counts__reactions-count']").click()
    t.sleep(30)
    full_names = driver.find_elements(By.XPATH, "//ul[@class='artdeco-list artdeco-list--offset-1']/li/div/div/a")
    for names in full_names:
        links =  names.get_attribute('href')
        profile_links.append(links)
        # print(links)
    chunked_list = list()
    chunk_size = 30
    lister = []
    for i in range(0, len(profile_links), chunk_size):
        chunked_list.append(profile_links[i:i + chunk_size])
        for user in profile_links[i:i + chunk_size]:
            # schedule.every(5).minutes.do(Login())
            driver.get(user)
            t.sleep(2)
            pyautogui.hotkey('ctrl', 'l')
            try:
                username = driver.find_element(By.XPATH, "//div[@class='mt2 relative']/div/div/h1").text
                print(username)
                usernames.append(username)
            except:
                pass
            t.sleep(15)
            pyautogui.hotkey('ctrl', 'l')
        Login()
except Exception as e_:
    print(e_)
