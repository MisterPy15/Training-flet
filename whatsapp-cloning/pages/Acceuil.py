
import os
from flet import *


class Acceuil:
    def __init__(self, page: Page):
        self.page = page
        self.page.bgcolor = "black"
        self.container = self.create_container()

    def on_accept_button_click(self, e):
        self.page.go('/Inscription')


    def create_container(self):
        return Column(
                controls=[
                    self.create_menu_bar(),
                    Container(height=20),
                    self.create_image(),
                    Container(height=30),
                    self.create_welcome_text(),
                    self.create_privacy_policy_text(),
                    self.create_language_selector(),
                    Container(height=40),
                    self.create_accept_button(),
                ]
            )


    def create_menu_bar(self):
        return Row(
            alignment='end',
            controls=[
                MenuBar(
                    expand=False,
                    controls=[
                        SubmenuButton(
                            content=Icon(icons.MENU, size=10),
                            controls=[
                                MenuItemButton(
                                    content=Text("aide", color="white"),
                                    style=ButtonStyle(
                                        bgcolor={
                                            ControlState.HOVERED: colors.GREEN
                                        }
                                    ),
                                ),
                            ]
                        ),
                    ]
                ),
            ]
        )


    def create_image(self):
        image_path = "/Users/misterpy/Desktop/Trainning-Flet/whatsapp-cloning/assets/icons/Acceuil.png"

        if os.path.exists(image_path):

            return Row(
                alignment='center', controls=[
                    Image(src=image_path, width=350, height=250)
                ]
            )
        else:
            print(f"Image non trouvée à l'emplacement : {image_path}")
            return Row(
                alignment='center', controls=[
                    Text("Image non trouvée", color="red", size=20)
                ]
            )


    def create_welcome_text(self):
        return Row(
            alignment='center',
            controls=[
                Text("Bienvenue sur WhatsApp", size=25, weight=FontWeight.W_500, font_family='poppins')
            ]
        )


    def create_privacy_policy_text(self):
        return Row(
            alignment='center',
            controls=[
                Text("  Veuillez lire notre ",
                     color='#808080',
                     size=12,
                     font_family='poppins',
                     spans=[
                         TextSpan("Politique de confidentialité.",
                                  TextStyle(color='blue')),
                         TextSpan('Appuyez \n sur "Accepter et continuer" pour accepter les'),
                         TextSpan(' Conditions\n                                       d\'utilisation.',
                                  TextStyle(color='blue'))
                     ]
                     )
            ]
        )


    def create_language_selector(self):
        return Row(
            alignment='center',
            controls=[
                Container(
                    height=60,
                    width=240,
                    border_radius=40,
                    padding=padding.all(10),
                    bgcolor="#2C2C2C",
                    content=Row(alignment='center', spacing=10,
                                controls=[
                                    Icon(icons.LANGUAGE, size=20, color="green"),
                                    Dropdown(
                                        hint_text="Français",
                                        padding=padding.symmetric(horizontal=10),
                                        width=160,
                                        height=40,
                                        border_color="#2C2C2C",
                                        border_radius=40,
                                        bgcolor="#2C2C2C",
                                        options=[
                                            dropdown.Option("Français"),
                                            dropdown.Option("Anglais"),
                                            dropdown.Option("Allemand"),
                                            dropdown.Option("Espagnol"),
                                            dropdown.Option("Russe"),
                                            dropdown.Option("Chinois"),
                                        ],
                                        text_style=TextStyle(color="white"),
                                    )
                                ],
                                )
                )
            ]
        )




    def create_accept_button(self):
        return Column(
            controls=[
                Row(alignment='center',
                    controls=[
                        Row(
                            alignment='center',
                            controls=[
                                ElevatedButton(
                                    text="Accepter et continuer",
                                    width=350,
                                    height=50,
                                    color="white",
                                    bgcolor='green',
                                    on_click=self.on_accept_button_click
                                    ),
                                ]
                            )
                        ]
                    )
                ]
            )

    def run(self):
        self.page.add(self.container)



def main(page: Page):
    app = Acceuil(page)
    app.run()




app(target=main, assets_dir="assets")