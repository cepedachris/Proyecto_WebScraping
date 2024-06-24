# -*- coding: utf-8 -*-
import json
from configparser import ConfigParser
from time import sleep

from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

MARKETPLACE_YOUR_POSTS = "https://www.facebook.com/marketplace/you/selling"
MAIN_URL = "https://www.facebook.com/"
MARKETPLACE_URL = "https://www.facebook.com/marketplace/create/item"

class App:
    def __init__(self, email="", password="", language="en", time_to_sleep="0.7", browser="chrome"):
        self.email = email
        self.password = password
        self.language = language
        self.marketplace_options = None
        self.ask_to_continue = True
        self.time_to_sleep = float(time_to_sleep)
        with open('marketplace_options.json', encoding='utf-8') as f:
            self.marketplace_options = json.load(f)
            self.marketplace_options = self.marketplace_options[self.language]
        # To remove the pop up notification window
        if browser == "Firefox":
            self.emojis_available = True
            options = FirefoxOptions()
            options.set_preference("dom.webnotifications.enabled", False)
            self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        else:
            # geckodriver allows you to use emojis, chromedriver does not
            self.emojis_available = False
            options = ChromeOptions()
            options.add_argument("--disable-notifications")
            self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)

        self.driver.maximize_window()
        self.main_url = MAIN_URL
        self.marketplace_your_posts = MARKETPLACE_YOUR_POSTS
        self.driver.get(self.main_url)
        self.log_in()
        self.move_from_home_to_marketplace_your_posts()
        #while(self.ask_to_continue):
        self.delete_current_post() 
        sleep(self.time_to_sleep)
        #self.driver.quit()
        
        
    def log_in(self):
        email_input = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "email")))
        email_input.send_keys(self.email)
        password_input = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "pass")))
        password_input.send_keys(self.password)
        login_button = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@type='submit']")))
        login_button.click()
        

    def move_from_home_to_marketplace_your_posts(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//a[@aria-label="Facebook"]')))
        self.driver.get(self.marketplace_your_posts)


    def delete_current_post(self):
        try:
            button_options = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='x1y1aw1k']"))).click()
            sleep(self.time_to_sleep)
            sleep(self.time_to_sleep)
            button_delete = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n xe8uvvx x1hl2dhg xggy1nq x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x87ps6o x1lku1pv x1a2a7pz xjyslct x9f619 x1ypdohk x78zum5 x1q0g3np x2lah0s xnqzcj9 x1gh759c x1i6fsjq xfvfia3 x1n2onr6 x16tdsg8 x1ja2u2z x6s0dn4 x1q8cg2c xnjli0 x1y1aw1k xwib8y2']"))).click()
            sleep(self.time_to_sleep)
            sleep(self.time_to_sleep)
            sleep(self.time_to_sleep)
            button_confirm_delete = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.x1i10hfl.xjbqb8w.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x972fbf.xcfux6l.x1qhh985.xm0m39n.x1ypdohk.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1o1ewxj.x3x9cwd.x1e5q0jg.x13rtm0m.x87ps6o.x1lku1pv.x1a2a7pz.x9f619[aria-label='Eliminar']")))
            sleep(self.time_to_sleep)
            sleep(self.time_to_sleep)
            sleep(self.time_to_sleep)

            button_confirm_delete = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.x1i10hfl.xjbqb8w.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x972fbf.xcfux6l.x1qhh985.xm0m39n.x1ypdohk.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1o1ewxj.x3x9cwd.x1e5q0jg.x13rtm0m.x87ps6o.x1lku1pv.x1a2a7pz.x9f619[aria-label='Eliminar']")))
            sleep(self.time_to_sleep)
            button_confirm_delete.click()
        except:
            sleep(self.time_to_sleep)
            sleep(self.time_to_sleep)
            button_options = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='x1y1aw1k']"))).click()
            sleep(self.time_to_sleep)
            sleep(self.time_to_sleep)
            button_delete = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n xe8uvvx x1hl2dhg xggy1nq x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x87ps6o x1lku1pv x1a2a7pz xjyslct x9f619 x1ypdohk x78zum5 x1q0g3np x2lah0s xnqzcj9 x1gh759c x1i6fsjq xfvfia3 x1n2onr6 x16tdsg8 x1ja2u2z x6s0dn4 x1q8cg2c xnjli0 x1y1aw1k xwib8y2']"))).click()
            sleep(self.time_to_sleep)
            sleep(self.time_to_sleep)
            sleep(self.time_to_sleep)
            button_confirm_delete = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.x1i10hfl.xjbqb8w.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x972fbf.xcfux6l.x1qhh985.xm0m39n.x1ypdohk.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1o1ewxj.x3x9cwd.x1e5q0jg.x13rtm0m.x87ps6o.x1lku1pv.x1a2a7pz.x9f619[aria-label='Eliminar']")))
            sleep(self.time_to_sleep)
            sleep(self.time_to_sleep)
            sleep(self.time_to_sleep)

            button_confirm_delete = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.x1i10hfl.xjbqb8w.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x972fbf.xcfux6l.x1qhh985.xm0m39n.x1ypdohk.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1o1ewxj.x3x9cwd.x1e5q0jg.x13rtm0m.x87ps6o.x1lku1pv.x1a2a7pz.x9f619[aria-label='Eliminar']")))
            sleep(self.time_to_sleep)
            button_confirm_delete.click()
      

if __name__ == '__main__':
    config_object = ConfigParser()
    config_object.read("config.ini")
    facebook = config_object["FACEBOOK"]
    configuration = config_object["CONFIG"]
    app = App(facebook["email"], facebook["password"], configuration["language"], configuration["time_to_sleep"], configuration["browser"])