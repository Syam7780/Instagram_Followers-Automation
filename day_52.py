import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


path = "D:\programs\chromedriver-win64\chromedriver.exe"

class LoginInsta:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(executable_path=path))
        self.driver.get(url="https://www.instagram.com/")
        mail = self.driver.find_element(By.CSS_SELECTOR, "input[type='text']")
        mail.send_keys("your mail")
        password = self.driver.find_element(By.CSS_SELECTOR, "input[type='password']")
        password.send_keys("your password")
        mail = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        mail.click()

    def find_common_interest(self):
        time.sleep(10)
        search_icon = self.driver.find_elements(By.CSS_SELECTOR, '.xh8yej3 div span .x78zum5 a div div div div svg')
        for item in search_icon:
            if item.get_attribute("aria-label") == "Search":
                item.click()
                break
        time.sleep(5)
        ip = self.driver.find_element(By.CSS_SELECTOR, ".xjoudau input")
        ip.send_keys("technology")
        time.sleep(2)
        channel = self.driver.find_element(By.CSS_SELECTOR, ".x6s0dn4 .xocp1fn a .x9f619")
        channel.click()

    def follow_members(self):
        time.sleep(10)
        followers = self.driver.find_element(By.CSS_SELECTOR, '.xc3tme8 ul li div a span span')
        followers.click()
        time.sleep(5)
        followers_div = self.driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]" )
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_div)
            time.sleep(2)
        time.sleep(5)
        users = followers_div.find_elements(By.CSS_SELECTOR, '.xyi19xy .x1dm5mii')
        for user in users:
            # users = followers_div.find_element(By.CSS_SELECTOR, '.xyi19xy .x1dm5mii')
            current_user = user.find_elements(By.CSS_SELECTOR, '.xqjyukv button')
            for btn in current_user:
                print(user.text)
                if btn.text == "Follow":
                    btn.click()
                    print("followed")

        print(users)
        time.sleep(20)

o = LoginInsta()
o.find_common_interest()
o.follow_members()