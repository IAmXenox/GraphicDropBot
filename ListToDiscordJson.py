import json


class ListToDiscordJson:
    # Création du json vide
    payload = {"embeds": []}
    sub_payload = None

    def toJson(self, list):
        # Création de l'embed sans fields
        self.sub_payload = {
            "type": "rich",
            "title": "Graphics cards available :",
            "fields": [],
            "color": 1146986
        }
        # Commande nécéssaire au bon fonctionnement de l'append sur un json
        self.sub_payload = str(self.sub_payload).replace("\'", "\"")
        self.sub_payload = json.loads(str(self.sub_payload))
        # Ajout de différents embeds contenant chacun un lien et un nom de carte graphique
        self.addFields(list)
        # Ajout du sous-json au json principal dans le field 'embeds'
        self.payload['embeds'].append(self.sub_payload)
        return self.payload

    def addFields(self, list):
        for i in list:
            self.sub_payload['fields'].append(
                {
                    "name": i[0],
                    "value": "[Link](" + i[1] + ")",
                    "inline": True
                }
            )
