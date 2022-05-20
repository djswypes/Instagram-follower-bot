import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException

USERNAME = "testttesttest5"
PASSWORD = "olaola03"
INSTA_URL = "https://www.instagram.com/"
SIMILAR_ACC = "moriahmillsofficialpage"
CHROME_DRIVER_PATH = r"C:\Users\OLA\Development\chromedriver.exe"


class InstaFollower:
    def __init__(self):
        driver_path = Service(CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=driver_path)
        self.following = None

    def login(self):
        self.driver.get(INSTA_URL)

        time.sleep(3)
        username = self.driver.find_element(by=By.NAME, value='username')
        username.send_keys(USERNAME)

        time.sleep(3)
        password = self.driver.find_element(by=By.NAME, value='password')
        password.send_keys(PASSWORD)
        time.sleep(3)
        password.send_keys(Keys.ENTER)

    def find_following(self):
        time.sleep(10)
        self.driver.get(INSTA_URL + SIMILAR_ACC)

        time.sleep(5)
        following = self.driver.find_elements(by=By.CSS_SELECTOR, value='section ul a')[1]
        following.click()
        time.sleep(5)
        pop_up = self.driver.find_element(by=By.XPATH, value='/html/body/div[6]/div/div/div/div[3]')

        for i in range(20):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", pop_up)
            time.sleep(2)

        self.following = self.driver.find_elements(by=By.CSS_SELECTOR, value="ul li button")
        return self.following

    def follow(self, all_followers):
        for follower in all_followers:
            try:
                follower.click()
                time.sleep(3.5)
            except ElementClickInterceptedException:
                self.driver.find_element(by=By.XPATH, value='/html/body/div[7]/div/div/div/div[3]/button[2]').click()


insta = InstaFollower()
insta.login()
following = insta.find_following()
insta.follow(following)
