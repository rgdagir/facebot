# FaceBot v2.0
# author: rgdagir (www.github.com/rgdagir)

#inporting useful libs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import requests
import re
import json
import time 

# start_selenium is where the program kickoffs. It starts the 
# Chrome webdriver and goes to Facebook notifications page (login
# will still be rewuired, though)
def start_selenium():
    # setting up driver and accessing page
    driver = webdriver.Chrome()
    access_link = driver.get("https://www.facebook.com/notifications")
    assert "Facebook" in driver.title
    return driver

# The login function is pretty simple: it takes the driver, and 
# the user's email and password (set as environment variables,
# at least for now) and types them into Facebook login landing page.
def login(driver, email, password):
    # logging in
    email = driver.find_element_by_id("email").send_keys(email)
    pw = driver.find_element_by_id("pass").send_keys(password + Keys.ENTER)

# fetch_notifs will work with the open browser, after the user
# was logged into Facebook, and fetch all NEW (aka unread) 
# notifications for the user. This function does not mark the 
# fetched notifications as read, though

def fetch_notifs(driver):
    notif_content = []
    # escape the standard popup
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    time.sleep(1)
    # locating elements
    new_notifs = driver.find_elements_by_xpath("//li[@class='_33c jewelItemNew']")    
    for notif in new_notifs:
        notif_text = notif.text
        notif_content.append(notif_text)
    driver.close()
    # turning list into string
    notif_content = "\n -> ".join(notif_content)
    return notif_content

# This fucntion sends the notifications to the user on Telegram,
# using the string with all notifications and the Telegram token
# to make a POST on the Telegram's API

def send_notif_telegram(notifs, token):
    # sending telegram message 
    method = "sendMessage"
    post_url = "https://api.telegram.org/bot" + token + "/" + method
    # setting params as dicts
    data = { 
        "chat_id":"564174252",
        "text":notifs
    }
    headers = {
        "Content-Type":"application/json"    
    }
    # calling the API
    send_message = requests.post(post_url, data=json.dumps(data), headers=headers)

