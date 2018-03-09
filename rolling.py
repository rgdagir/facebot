# Facebot v2.0 Loop Update Script
# Author: Raul Dagir (github.com/rgdagir)

#importing useful libraries
import requests
import os
import facebook_bot as fbot
import json

def fetch_updates(last_id, telegram_token):
    # fetching updates
    method = "getUpdates"
    updates_url = "https://api.telegram.org/bot" + telegram_token + "/" + method
    data = { 
        "offset": last_id,
        "timeout":10
    }
    headers = {
        "Content-Type":"application/json"    
    }
    fetched_data = requests.get(updates_url, data=json.dumps(data), headers=headers)
    return fetched_data

def analyze_updates(updates, last_id):
    # parse data and get text messages sent by user
    if (updates.status_code == 200):
        updates = updates.json()
        results = updates["result"]
        if (len(results)>0):
            for result in results:
                update_id = result["update_id"]
                chat_id = result["message"]["chat"]["id"]
                text_content = result["message"]["text"]
                print("update id: ", update_id, " chat id: ", chat_id, " text: ", text_content)
                if (text_content == "notifications" and update_id > last_id):
                    last_id = update_id
                    run_bot()
    return last_id

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
    counter = 0
    last_id = 0
    telegram_token = os.environ["TELEGRAM_TOKEN"]
    while(True):
        updates = fetch_updates(last_id, telegram_token)
        last_id = analyze_updates(updates, last_id)
        print(last_id)
        counter += 1
        print ("times fetched: ", counter)