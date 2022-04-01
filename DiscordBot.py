import json
import requests

from ListToDiscordJson import ListToDiscordJson

# Url du webhook sur le channel discord ou les messages sont envoyés
webhook_url = 'https://discord.com/api/webhooks/951494877227647047/hbCxDG5ATbAxitF7Kno6VBqNLJj96GdUR_rhSK9mw2O4X8PNPL1-RvAT7hpE0nwJmNCD'


class DiscordBot:
    def sendNotif(self, gClist):
        payload = ListToDiscordJson().toJson(gClist)
        # Définition du header nécéssaire au bon fonctionnement de la méthode POST
        headers = {
            'Content-Type': 'application/json',
        }
        # POST du json sur le webhook discord puis récupération de la réponse pour vérifier les codes d'erreurs
        response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
        print(response)
