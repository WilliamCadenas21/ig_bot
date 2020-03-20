from selenium import webdriver
import os
import time

import configparser


class InstagramBot:

    def __init__(self, username, password):
        """
        Initializes an instance of the InstagramBot class.

        Call the login method to authenticate a user with IG.

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
        """
        Logs a user into Instagram via the web portal 
        """    
        self.driver.get('{}/accounts/login/'.format(self.base_url))
        self.driver.maximize_window() #For maximizing window
        self.driver.implicitly_wait(20) #gives an implicit wait for 20 seconds

        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)

        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button').click()
        time.sleep(5)

    def nav_user(self, user):
        self.driver.get('{}/{}/'.format(self.base_url, user))

    def follow_user(self, user):
        self.nav_user(user)
        time.sleep(2) # wait for load the page
        follow_button = self.driver.find_element_by_xpath("//button[contains(text(), 'Follow')]")
        follow_button.click()

    def unfollow_user(self, user):
        self.nav_user(user)
        time.sleep(2) # wait for load the page 
        unfollow_button_action = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/span/span[1]/button')
        unfollow_button_action.click()                             #//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/span/span[1]/button/div/span
        unfollow_button_confirm = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]')
        unfollow_button_confirm.click()


if __name__ == '__main__':
    config_path = './config.ini'
    cparser = configparser.ConfigParser()
    cparser.read(config_path)

    username = cparser['AUTH']['USERNAME']
    password = cparser['AUTH']['PASSWORD']
    
    ig_bot = InstagramBot(username, password)
    #ig_bot.follow_user('mafelopez.03') #user that you want to navigate

    
    user = 'tonyrobbins'
    #user = 'garyvee'
    #ig_bot.follow_user(user) #user that you want to navigate
    #time.sleep(5)
    ig_bot.unfollow_user(user)