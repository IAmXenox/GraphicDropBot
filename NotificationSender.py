from TwitterBot import *
from DesktopNotifications import *
from Checker import *
from Plateformes import *
from DiscordBot import *
from MessengerBot import *
from InterfaceMenu import *

# Creation des bots de notifications
dsB = DesktopNotifications()
twB = TwitterBot()
diB = DiscordBot()
meB = MessengerBot()

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
        if Plateformes.Messenger.value:
            meB.sendNotification(gCList)
