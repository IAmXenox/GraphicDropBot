import tweepy
import random


class TwitterBot:
    def sendNotif(self, gCList):
        CONSUMER_KEY = 'sB7TArIgtrjwn23QVu6Y4PRcX'
        CONSUMER_SECRET = 'gdlTUt7P4W0H3od8s9y1I9CvzIt1NQd1lXoenkikUOnKO9KvWf'
        ACCESS_KEY = '1497862310932758533-51tXlem3xvV2rteF2XUkOORGJQc4I3'
        ACCESS_SECRET = 'n1vsZjWgjizW5sN7w2OzEfAKPQexcrhUKvOwASg3gEWNg'
        # Clé obtenu en passant le niveau de sécurité 2 pour créer un bot Twitter

        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

        api = tweepy.API(auth)
        # Post d'un tweet contenant les différents lien et cartes graphiques disponibles
        for card in gCList:
            api.update_status(
                card[0] + " is available at : " + card[1] + " #GeForce" + " id: " + str(random.randint(1000, 9999)))
