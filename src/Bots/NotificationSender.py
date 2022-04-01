from src.Bots.TwitterBot import *
from src.Bots.DesktopNotifications import *
from src.Plateformes import *
from src.Bots.DiscordBot import *

# Creation des bots de notifications
dsB = DesktopNotifications()
twB = TwitterBot()
diB = DiscordBot()

class NotificationSender:
    def notificationDrop(self, gCList):
        # Envoi des listes de carte graphique et de lien récupérer au différents bots de notifications
        for i in gCList:
            print(str(i[0]) + " : " + str(i[1]))
        if Plateformes.Twitter.value:
            twB.sendNotif(gCList)
        if Plateformes.Desktop.value:
            dsB.sendNotif(gCList)
        if Plateformes.Discord.value:
            diB.sendNotif(gCList)
