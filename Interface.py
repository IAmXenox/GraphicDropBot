import json
from tkinter import *

import requests
import tweepy


def window():
    # Creating the window
    master = Tk()

    # Personalization of the window
    master.title("Message Sender")
    master.geometry("1080x720")
    master.minsize(480, 360)
    master.config(bg="#DFDFDF")

    # Creating the frames
    frameTitle = Frame(master, bg="#DFDFDF")
    frameText = Frame(master, bg="#DFDFDF")
    frameButtons = Frame(master, bg="#DFDFDF")

    # Adding message title
    message_title = Label(frameTitle, text="Message à envoyer", font=("Helvetica", 10), bg="#DFDFDF")
    message_title.pack()

    # Adding entry of user
    message_entry = Text(frameText, font=("Helvetica", 10), width=1, height=1)
    message_entry.grid(row=5, column=1, ipadx=50, ipady=20)

    # Adding Check buttons
    isDiscordChecked = IntVar()
    isTwitterChecked = IntVar()
    Checkbutton(frameButtons, text="Discord", font=("Helvetica", 10), variable=isDiscordChecked, onvalue=1,
                offvalue=0, bg="#DFDFDF").pack(side=LEFT)
    Checkbutton(frameButtons, text="Twitter", font=("Helvetica", 10), variable=isTwitterChecked, onvalue=1,
                offvalue=0, bg="#DFDFDF").pack(side=LEFT)

    # Add a send button
    Button(frameButtons, text="Envoyer",
           command=lambda: sendMessage(str(message_entry.get("1.0", END)), isDiscordChecked, isTwitterChecked),
           font=("Helvetica", 10)).pack()

    # Show the frame
    frameTitle.pack()
    frameText.pack()
    frameButtons.pack()

    # Show the window (master)
    master.mainloop()


def sendMessage(message, isDiscordChecked, isTwitterChecked):
    # Checking of CheckButton value
    if isDiscordChecked.get() == 1:
        messageDiscord(message)
    if isTwitterChecked.get() == 1:
        postTwitter(message)


def messageDiscord(message):
    webhook_url = 'https://discord.com/api/webhooks/951494877227647047' \
                  '/hbCxDG5ATbAxitF7Kno6VBqNLJj96GdUR_rhSK9mw2O4X8PNPL1-RvAT7hpE0nwJmNCD'
    payload = {
        "content": message,
        "embeds": [
            {
                "type": "rich",
                "title": 'Graphics cards available :',
                "fields": [
                    {
                        "name": "1",
                        "value": "field 1",
                        "inline": True
                    },
                    {
                        "name": "2",
                        "value": "field 2",
                        "inline": True
                    },
                    {
                        "name": "3",
                        "value": "field 3",
                        "inline": True
                    },
                    {
                        "name": "4",
                        "value": "field 4",
                        "inline": True
                    },
                    {
                        "name": "5",
                        "value": "field 5",
                        "inline": True
                    },
                    {
                        "name": "6",
                        "value": "https://google.com",
                        "inline": True
                    }]
            }]
    }
    headers = {
        'Content-Type': 'application/json',
    }
    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    print(response)


def postTwitter(message):
    CONSUMER_KEY = 'sB7TArIgtrjwn23QVu6Y4PRcX'
    CONSUMER_SECRET = 'gdlTUt7P4W0H3od8s9y1I9CvzIt1NQd1lXoenkikUOnKO9KvWf'
    ACCESS_KEY = '1497862310932758533-51tXlem3xvV2rteF2XUkOORGJQc4I3'
    ACCESS_SECRET = 'n1vsZjWgjizW5sN7w2OzEfAKPQexcrhUKvOwASg3gEWNg'
    # Get level 2 on https://developer.twitter.com/en in order to get these keys

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    api = tweepy.API(auth)
    api.update_status(message)


if __name__ == '__main__':
    window()
