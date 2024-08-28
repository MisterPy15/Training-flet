from flet import *


class Inscription :
    def __init__(self, page: Page):
            self.page = page
            self.page.bgcolor = "black"
            self.container = self.container_Inscr()
           # self.page.adaptive  = True

    def on_next_click(self, e):
        self.page.route = '/Verification'  # Changer de route vers VerificationsNumber
        self.page.update()


    def container_Inscr(self):
        return Column(
               controls=[
                    self.ContenueTextuel(),
                    self.InfoNumberContry(),
                    self.CreateButtonn()
               ]
        )


    def ContenueTextuel(self):
        return Column(
                    controls=[
                                Row(alignment='center',
                                    controls=[



                                        Text("Saisisez votre numéro de téléphone",
                                             size=20,
                                             color="green",
                                             weight='bold'
                                             ),

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




                                ),



                                Container(height=20),
                                Row(alignment='center',
                                    controls=[
                                        Text(
                                            "     Whatsapp devra utilisé votre numéro de \ntélephone. Des frais peuvent s'appliquer selon\n             l'opérateur.",
                                                size=18,
                                            spans=[
                                                TextSpan(" Quel est mon numéro ?", TextStyle(color='blue'))
                                            ]

                                            )
                                    ]
                                )


            ]
        )


    def InfoNumberContry(self):
        return Column(
                        controls=[
                                    Container(height=40),
                                    Row(alignment='center',
                                        controls=[
                                            Dropdown(
                                                    hint_text="Côte d'ivoire",
                                                    padding=padding.symmetric(horizontal=10),
                                                    width=360,
                                                    height=40,
                                                    border_color="green",
                                                    border_radius=1,
                                                    border_width=0.1,
                                                    bgcolor="#2C2C2C",
                                                    options=[
                                                        dropdown.Option("Côte d'ivoire"),
                                                        dropdown.Option("État Unis"),
                                                        dropdown.Option("Allemagne"),
                                                        dropdown.Option("Espagnz"),
                                                        dropdown.Option("Russie"),
                                                        dropdown.Option("Chine"),
                                                    ],
                                                    text_style=TextStyle(color="white"),
                                            ),
                                        ]
                                    ),
                                    Container(height=20),
                                    Row(alignment='center',
                                        controls=[
                                            Dropdown(
                                                hint_text="+225",
                                                padding=padding.symmetric(horizontal=10),
                                                width=100,
                                                height=50,
                                                border_color="green",
                                                border_radius=1,
                                                border_width=0.1,
                                                bgcolor="#2C2C2C",

                                                options=[
                                                    dropdown.Option("+225"),
                                                    dropdown.Option("+225"),
                                                    dropdown.Option("+225"),
                                                    dropdown.Option("+225"),
                                                    dropdown.Option("+225"),
                                                    dropdown.Option("+225"),

                                                ]
                                            ),
                                            TextField(
                                                width=245,
                                                height=50,
                                                border_color='green',
                                                label="Numéro de téléphone",
                                                label_style=TextStyle(
                                                                    color="#808080",
                                                                    size=18,
                                                                    weight='bold'
                                                                    )
                                            )

                                        ]
                                    ),
                                    Container(height=240)
                                ]
                        )


    def CreateButtonn(self):
        return Column(
                        controls=[
                                    Row(alignment='center',
                                        controls=[
                                                    Row(
                                                            alignment='center',
                                                            controls=[
                                                                ElevatedButton(
                                                                    text="Suivant",
                                                                    width=350,
                                                                    height=50,
                                                                    color="white",
                                                                    bgcolor='green'

                                                        ),
                                                    ]
                                                )

                                        ]
                                    )
                        ]
        )



    def run(self):
        self.page.add(self.container)


def main(page : Page):
    app = Inscription(page)
    app.run()

app(target=main, assets_dir="assets")