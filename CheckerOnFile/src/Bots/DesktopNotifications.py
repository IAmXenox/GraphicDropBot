import webbrowser

from win10toast_click import ToastNotifier


class DesktopNotifications:
    def __init__(self):
        self.toast = ToastNotifier()

    def sendNotif(self, gCList):
        # Envoi de la notification de bureau
        for card in gCList:
            self.toast.show_toast(title=card[0], msg=card[0] + " is available !!", duration=2,
                                  callback_on_click=lambda: webbrowser.open(card[1]))
