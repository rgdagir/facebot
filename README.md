# Facebot

Facebot is an open-source Telegram bot that fetches all your unread Facebook notifications and send them through Telegram, with the intent of saving you time and have quicker access to all your notifications, without having the need to open Facebook's app.

## How to download and start using

### Clone this repo with 

```
$ git clone git@github.com:rgdagir/facebot.git
```

### Set your environment variables

If you are in a Mac/UNIX-based system, go to your home directory, open the `.bashprofile` file and set your environment variables for your Facebook login. In Windows, follow these instructions: https://www.computerhope.com/issues/ch000549.htm. Your email variable has to be set as LIAME and your password variable has to be named DROWSSAP.
 
Example (in .bash_profile):
```
export LIAME='user@domain.com'
export DROWSSAP='password123'
```

### Running the bot

When all of the above is done, go back to the folder where you cloned the repo, open your terminal and type 

```
python facebook_bot.py
```
...and BANG! Your notifications will be on yout phone.

### Disclaimer

This is a project I used to run locally on my machine every 8 hours, but that I am now making public because I want people to use it. If you're interested in the project or in helping, hit me up!
