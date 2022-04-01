import datetime
import time

from src import ApiNvidia
from src.Bots.NotificationSender import NotificationSender


# Graphic Cards available for checking :
#     - name: RTX 3090, id: NVGFT090_
#     - name: RTX 3080 Ti, id: NVGFT080T_
#     - name: RTX 3080, id: NVGFT080_
#     - name: RTX 3070 Ti, id: NVGFT070T_
#     - name: RTX 3070, id: NVGFT070_
#     - name: RTX 3060 Ti, id: NVGFT060T_

GraphicCards = []

notifier = NotificationSender()

# Locales : FR, UK, IT, ES, DE
region = 'FR'

link = "https://api.store.nvidia.com/partner/v1/feinventory?skus=" + region + "&locale=" + region

expiringTime = 12

class Checker:
    global listOfCgActivated

    def __init__(self, listOfCg):
        # Message de confirmation de création de l'instance
        self.listOfCgActivated = listOfCg
        for i in listOfCg:
            if i != "":
                separation = i.find("+")
                GraphicCards.append([i[:separation],i[separation+1:]])

        print("Nouveau checker")

    def notificationDrop(self, message):
        notifier.notificationDrop(message)

    def checkingAlreadyUsedLinks(self, linkUsed, link):
        ret = True
        for i in linkUsed:
            if link in i:
                ret = False
        return ret

    def Checking(self):
        global cgdef
        # Aarray des liens déjà envoyé au bots de notifications sur les 12 dernières heures
        linkAlreadyUsed = []
        # Array des cartes graphiques marqués comme disponible sur l'api NVIDIA
        graphicCardsAvailable = []

        while True:
            time.sleep(2)
            print("Actually cheking " + str(len(GraphicCards)) + " graphic cards at : " + link)

            # Enregistrement du texte de l'api dans une variable
            ## myfile = requests.get(link).text

            # Suppréssion du texte inutile au fonctionnement de l'application de l'api NVIDIA
            ## withoutb = myfile[27:-2]

            withoutb = ApiNvidia.apitxt


            start = 0
            end = 0

            # Parcours du texte récupéré
            for i in range(0, len(withoutb)):
                # Création d'une variable contenant le texte de chaque élément
                if withoutb[i] == "{":
                    start = i
                if withoutb[i] == "}":
                    end = i
                cgdef = withoutb[start:end]
                if end > start:
                    for GC in GraphicCards:
                        # Vérification si l'élément obtenu est bien un de ceux recherché
                        if GC[1] + region in cgdef:
                            cgname = GC[0]
                            # Vérification si l'élément obtenu est disponible (true) ou non (false)
                            if "\"is_active\":\"false\"" in cgdef:
                                # Enregistrement du lien de l'élément obtenu dans l'array de liens déjà utilisés
                                linkofCg = cgdef[36:cgdef.find("price") - 3]
                                # Suppression de tout les liens présent dans l'array depuis plus de 12h
                                for i in linkAlreadyUsed:
                                    if int(datetime.datetime.utcnow().timestamp() - i[1]) > expiringTime * 3600:
                                        linkAlreadyUsed.remove(i)
                                # Vérification si le lien de l'élément obtenu à déjà été envoyé
                                if self.checkingAlreadyUsedLinks(linkAlreadyUsed, linkofCg):
                                    linkAlreadyUsed.append([linkofCg, datetime.datetime.utcnow().timestamp()])
                                    # Ajout d'un array contenant le nom de la carte graphique et le lien sur lequel elle est disponible
                                    graphicCardsAvailable.append([cgname, linkofCg])

                    end = 0
                    start = 0
            # Envoie de l'array contenant les cartes graphiques disponibles si il n'est pas vide
            if len(graphicCardsAvailable) != 0:
                self.notificationDrop(graphicCardsAvailable[:len(graphicCardsAvailable)-1])
                # Suppression de tout les cartes graphiques disponibles de l'array
                graphicCardsAvailable.clear()
