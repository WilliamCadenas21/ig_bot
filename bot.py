from selenium import webdriver
import os
import time

class InstagramBot:

    def __init__(self, username, password):
        """
        Args:
            username:str: The Instagram username for a user
            password:str: The Instagram password for a user

        Attributes:
            driver:Selenium.webdriver.Chrome: The Chromedriver that is used to automate browser actions
        """

        self.username = username
        self.password = password

        self.base_url = 'https://www.instagram.com'

        self.driver = webdriver.Chrome('./chromedriver')
        self.login()

    def login(self):    
        self.driver.get('{}/accounts/login/'.format(self.base_url))
        self.driver.maximize_window() #For maximizing window
        self.driver.implicitly_wait(20) #gives an implicit wait for 20 seconds

        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)

        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button').click()
        time.sleep(5)
        self.driver.implicitly_wait(60)

    def nav_user(self, user):
        self.driver.get('{}/{}'.format(self.base_url, user))


if __name__ == '__main__':
    temp1 = 'wcadenas@uninorte.edu.co'
    temp2 = '/Tempinstagram123'
    ig_bot = InstagramBot(temp1, temp2)
    
    ig_bot.nav_user('williamcad21')

