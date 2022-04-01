from fbchat import Client
from fbchat.models import Message
import requests

class MessengerBot:
    token = "EAAJ5lYNjeTgBAKt1ZC9NIuJYKTUbM8SX5lqwcf5ZBA3QtzDnygFhVq4mTpgQ6tzjCJSWOkO7dnnFLgQlC1tdAnTn0ZBM9A4VIZCIsRn1uaVNr73T1MkVSGI1M4gY7YMwV9qLpemrd8PZBQZAANHV08z6eHWDoTcwxHz2ZBo2b6KtwgarBJ8UioVvQtBEkszKUUZD"

    def login(self):
        appID = "696633014843704"

    def sendNotification(self, gCList):
        token = requests.args.get("hub.verify_token")
        pass

if __name__ == '__main__':
    mes = MessengerBot()
    mes.login()
