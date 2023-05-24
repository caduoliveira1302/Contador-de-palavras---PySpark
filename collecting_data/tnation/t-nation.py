from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import warnings
import re
warnings.filterwarnings("ignore")
import pandas as pd


class tNation:
    def __init__(self):
        self.url = "https://www.t-nation.com/"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # self.product_path = [f"""//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[{i}]/div/div/div""" for i in range(1,63)]
        self.final_collection_list = []

    def open_url(self):
        self.driver.get(self.url)
        sleep(2)

    def search_product(self):
        articles_menu = self.driver.find_element(By.XPATH, """//*[@id="primary-menu"]/li[2]/a""")
        articles_menu.click()
        sleep(2)

        search_input = self.driver.find_element(By.XPATH, """//*[@id="s"]""")
        search_input.send_keys("whey protein")
        search_input.click()
        sleep(1)



    







tnation = tNation()
tnation.open_url()
tnation.search_product()