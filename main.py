import  os
import glob
cookie_del=glob.glob("config/*cookie.json")
os.remove(cookie_del[0])

from instabot import  Bot

bot = Bot()

#login

bot.login(username= "user_id", password= "password")

#uploading photo

#bot.upload_photo("12.jpg", caption="Give me some sunshine")

#to follow someone

#bot.follow("arijitsingh")

#to send message

#bot.send_message("Hi, i am asfak...", ['rik2001q'])

#to unfollow

bot.unfollow_everyone()




