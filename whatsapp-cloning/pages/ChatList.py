from cProfile import label

from flet import *

class ChatList:
    def __init__(self, page: Page):
        self.page = page
        self.page.bgcolor = "black"
        self.container = self.GlobalListChat()



    def GlobalListChat(self):
        return Column(
            controls=[
                self.menuBarTop(),
                self.containerListChat(),
                self.menuBarBottom()
            ]
        )





    def menuBarTop(self):
        return Container(
            height=50,
            bgcolor="black",
            content=Row(
                        controls=[
                                    Row(
                                        controls=[
                                                    Text("Whatsapp",
                                                         size=20,
                                                         color=colors.WHITE,
                                                         weight='bold'),
                                        ]
                                    ),
                                    Row(
                                        controls=[
                                                    IconButton(icons.PHOTO_CAMERA_OUTLINED, icon_color=colors.WHITE),
                                                    IconButton(icons.SEARCH, icon_color=colors.WHITE),
                                                    PopupMenuButton(
                                                                    items=[
                                                                            PopupMenuItem(text="Nouveau groupe"),
                                                                            PopupMenuItem(text="Nouvelle diffusion"),
                                                                            PopupMenuItem(text="Appareils importants"),
                                                                            PopupMenuItem(text="Paramètres"),
                                                                            PopupMenuItem(text="Changer de compte")
                                                                    ],
                                                                    icon_color=colors.WHITE
                                            ),
                                        ]
                                    )
                        ],
                        alignment="spaceBetween"
            ),
            padding=10,
        )



    def containerListChat(self):
        # Exemple de données simulées
        chats = [
            {"name": "Chris Agoh", "message": "http://192.168.43.88:8551/main...", "time": "            Hier",
             "avatar": "/Users/misterpy/Desktop/Trainning-Flet/whatsapp-cloning/assets/icons/IMG_2264.JPG"},

            {"name": "Audrey", "message": "Ce message a été supprimé.", "time": "14:27",
             "avatar": "assets/icons/audrey.png"},
            {"name": "Beerens", "message": "Thanks bro❤️", "time": "12:08", "avatar": "assets/icons/beerens.png"},
            {"name": "Emmanuel UTA", "message": "❤️", "time": "11:45", "avatar": "assets/icons/emmanuel.png"},
            {"name": "Horlys", "message": "🤠😸💔", "time": "11:43", "avatar": "assets/icons/horlys.png"},
            {"name": "Christ Junior", "message": "Vous avez réagi par 👍 à 'yf je vais garde...", "time": "Hier",
             "avatar": "assets/icons/christ.png"},
            {"name": "Alloma", "message": "Ok d'acc mann", "time": "                                       Hier", "avatar": "assets/icons/alloma.png"},
            {"name": "Alloma", "message": "Ok d'acc mann", "time": "                                       Hier", "avatar": "assets/icons/alloma.png"},
            {"name": "Alloma", "message": "Ok d'acc mann", "time": "                                       Hier", "avatar": "assets/icons/alloma.png"},
            {"name": "Alloma", "message": "Ok d'acc mann", "time": "                                       Hier", "avatar": "assets/icons/alloma.png"},

        ]

        # Construction dynamique de la liste de discussions
        chat_controls = []
        for chat in chats:
            chat_controls.append(
                Container(
                    padding=10,
                    content=Row( scroll="auto",
                        controls=[
                            Image(src=chat["avatar"],
                                  width=40,
                                  height=40,
                                  fit="cover", border_radius=40),
                            Column(
                                controls=[
                                    Text(chat["name"], color=colors.WHITE, weight='bold'),
                                    Text(chat["message"], color=colors.GREY),
                                ],
                            ),
                            Text(chat["time"], color=colors.GREY),
                        ],
                        alignment="spaceBetween",
                    )
                )
            )

        return Container(
            height=600,
            content=Column(
                scroll='auto',
                controls=chat_controls
            )
        )




    def menuBarBottom(self):

        return Container(
                            height=50,
                            bgcolor="white",

                            content=CupertinoNavigationBar(
                                                            bgcolor=colors.BLACK,
                                                            inactive_color=colors.GREY,
                                                            active_color=colors.WHITE,

                                                            destinations=[
                                                                            NavigationBarDestination(
                                                                                                    icon=icons.MARK_UNREAD_CHAT_ALT,
                                                                                                    label="Discussions"),
                                                                            NavigationBarDestination(
                                                                                                    icon=icons.AMP_STORIES,
                                                                                                    label="Actus"),
                                                                            NavigationBarDestination(
                                                                                                    icon=icons.GROUPS_OUTLINED,
                                                                                                    label="Communautés",),
                                                                            NavigationBarDestination(
                                                                                                    icon=icons.CALL_SHARP,
                                                                                                    label="Appels"),
                                                            ]
                            )




        )










    def run(self):
        self.page.add(self.container)

def main(page: Page):
    app = ChatList(page)
    app.run()

app(target=main, assets_dir="../assets")
