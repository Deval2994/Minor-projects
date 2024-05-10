"""
Author: Deval Patel
Description: This Python script automates sending messages via Instagram Direct Messages. It logs into an Instagram
account, sends a pre-defined message to the author (Deval Patel), and can also include an additional message.
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By



def login(username, password):
    driver.find_element(By.NAME, 'username').send_keys(username)
    driver.find_element(By.NAME, 'password').send_keys(password)
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]').click()
    time.sleep(5)  # Wait for the page to load after logging in
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div').click()
    time.sleep(1)  # Wait for the direct messages section to load

def messageReceiverIdentity(messageSender, message):
    driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
    time.sleep(1)  # Wait for the search bar to appear
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[5]/div/div/div/span/div/a/div').click()
    time.sleep(2)  # Wait for the search results to load
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[1]/div/div[1]/div[2]/div/div').click()
    time.sleep(2)  # Wait for the chat to open
    driver.find_element(By.CSS_SELECTOR, 'body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div > div > div.x9f619.x1ja2u2z.x1k90msu.x6o7n8i.x1qfuztq.x10l6tqk.x17qophe.x13vifvy.x1hc1fzr.x71s49j.xh8yej3 > div > div:nth-child(2) > div > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1iyjqo2.x2lwn1j.xeuugli.x1q0g3np.x1a02dak.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 > input').send_keys('deval')
    time.sleep(1)  # Wait for the input field to become active
    driver.find_element(By.CSS_SELECTOR, 'body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div > div > div.x9f619.x1ja2u2z.x1k90msu.x6o7n8i.x1qfuztq.x10l6tqk.x17qophe.x13vifvy.x1hc1fzr.x71s49j.xh8yej3 > div > div.xjp7ctv > div > div > div:nth-child(1) > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1pi30zi.x1swvt13.xwib8y2.x1y1aw1k.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1').click()
    time.sleep(1)  # Wait for the chat to open

    driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[4]').click()
    time.sleep(1)  # Wait for the text input field to become active
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]').send_keys(f'Hi, I am {messageSender}\nI had ran your code')
    time.sleep(1)  # Wait for the message to be typed
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[3]').click()

    if message != "":
        driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]').send_keys(message)
        driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[3]').click()

    time.sleep(5)  # Wait for the message to be sent

if __name__ == "__main__":
    print("**************************************** Welcome to my Instagram Auto message sender bot ****************************************")
    print("\n>>>Login Instruction: TO LOGIN PLEASE DISABLE YOUR 2 STEP VERIFICATION, because of OPT reason...\n")
    username = input("Enter your username or email: ")
    password = input("Enter password: ")
    messageSender = input("Please Enter your name: ")
    message = input("Your message: ")

    # Initialize the WebDriver instance
    BASE_URL = "https://www.instagram.com/"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(BASE_URL)
    login(username, password)
    messageReceiverIdentity(messageSender, message)
    print("\nMessage sent successfully...")
