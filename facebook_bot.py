# FaceBot v2.0
# author: rgdagir (www.github.com/rgdagir)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import requests
import re
import json
import time 

def start_selenium():
    # setting up driver and accessing page
    driver = webdriver.Chrome()
    access_link = driver.get("https://www.facebook.com/notifications")
    assert "Facebook" in driver.title
    return driver

def login(driver, email, password):
    # logging in
    email = driver.find_element_by_id("email").send_keys(email)
    pw = driver.find_element_by_id("pass").send_keys(password + Keys.ENTER)

def fetch_notifs(driver):
    notif_content = []
    notif_ids = []
    # find notifications
    # alert = driver.switch_to_alert()
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    time.sleep(1)
    new_notifs = driver.find_elements_by_xpath("//li[@class='_33c jewelItemNew']")    
    for notif in new_notifs:
        notif_text = notif.text
        notif_content.append(notif_text)
    driver.close()
    notif_content = "\n -> ".join(notif_content)
    return notif_content

def send_notif_telegram(notifs, token):
    # sending telegram message #chupaTeleVoice
    method = "sendMessage"
    post_url = "https://api.telegram.org/bot" + token + "/" + method
    data = { 
        "chat_id":"564174252",
        "text":notifs
    }
    headers = {
        "Content-Type":"application/json"    
    }

    send_message = requests.post(post_url, data=json.dumps(data), headers=headers)

# if __name__ == "__main__":
#     driver = start_selenium()
#     email = os.environ["LIAME"]
#     password = os.environ["DROWSSAP"]
#     telegram_token = os.environ["TELEGRAM_TOKEN"]
#     login(driver, email, password)
#     notifs = fetch_notifs(driver)
#     send_notif_telegram(notifs, telegram_token)
