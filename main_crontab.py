# Facebot v2.0 For Use With Crontab
# Author: Raul Dagir (github.com/rgdagir)
# IMPORTANT NOTE: given this program is not responding to user input,
# and is meant to be used with crontab, the client has to configure its
# chat_id in the facebook_bot.py program (line 61)
# To do this, create a bot in Telegram, start a conversation with it, it https://api.telegram.org/bot<yourtoken>/getUpdates with your Bot Token, then find the chat object and get your chat id.
# This version of Facebot assumes previous experience with APIs and some 
# familiarity with Telegram Bots
#importing useful libraries
import requests
import os
import facebook_bot as fbot
import json

def run_bot():
    driver = fbot.start_selenium()
    email = os.environ["LIAME"]
    password = os.environ["DROWSSAP"]
    telegram_token = os.environ["TELEGRAM_TOKEN"]
    fbot.login(driver, email, password)
    notifs = fbot.fetch_notifs(driver)
    fbot.send_notif_telegram(notifs, telegram_token)

# main function
if __name__ == "__main__":
    run_bot()
    print("Done!")
