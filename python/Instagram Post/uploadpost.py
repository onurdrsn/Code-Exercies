#pip install instabot

from instabot import Bot
bot=Bot()
bot.login(username = "yourusername", password = "yourpass")
bot.upload_photo("img", caption = "Description")       
