from flet import *
import time
import threading



class VerificationsNumber:

    def __init__(self, page: Page):
        self.page = page
        self.page.bgcolor = "black"
        self.timer_seconds = 60
        self.timer_text = Text("Vous pourrez demander un nouveau code dans 1:00",
                               size=15,
                               color="white")

        self.code_fields = []
        self.container = self.container_Verif()
        self.run_timer()


    def container_Verif(self):
        return Column(
            controls=[
                self.ContenueTextuel(),
                self.InputsCodes(),
                self.timesResponseSMS()
            ]
        )


    def ContenueTextuel(self):
        return Column(
            controls=[
                Row(alignment='center',
                    controls=[
                        Text("Vérification de votre numéro",
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
                            "En attente de détection automatique d'un SMS \n envoyé au +XXXXXXXXXXXXX",
                            size=15,
                            spans=[
                                TextSpan(" Numéro incorrect ?", TextStyle(color='blue'))
                            ]
                        )
                    ]
                    )
            ]
        )


    def InputsCodes(self):
        # Clear previous fields
        self.code_fields = []

        return Column(
            controls=[
                Container(height=40),
                Row(alignment=MainAxisAlignment.CENTER,
                    controls=[
                        self.create_code_field(),
                        self.create_code_field(),
                        self.create_code_field(),
                        Container(width=10),
                        self.create_code_field(),
                        self.create_code_field(),
                        self.create_code_field(),
                    ]
                    ),
                Container(height=40),
                Row(alignment='center',
                    controls=[
                        Text("Vous n'avez pas reçu de code?",
                             size=13,
                             color="#808080")
                    ]
                    )
            ]
        )



    def create_code_field(self):
        field = TextField(
            width=50,
            text_align=TextAlign.CENTER,
            border_color="#808080",
            border_width=2,
            keyboard_type=KeyboardType.NUMBER,  # Restrict input to numbers
            on_change=self.check_all_fields_filled
        )
        self.code_fields.append(field)
        return field



    def check_all_fields_filled(self, e):
        all_filled = all(field.value.isdigit() and field.value != "" for field in self.code_fields)
        if all_filled:
            self.page.dialog = AlertDialog(
                title=Text("Success"),
                content=Text("Tous les champs sont remplis! Passer à la page suivante."),
                actions=[
                    TextButton("OK", on_click=self.go_to_next_page)
                ],
            )
            self.page.dialog.open = True
            self.page.update()



    def go_to_next_page(self, e):
        # Logique pour passer à la page suivante
        self.page.dialog.open = False
        self.page.update()



    def timesResponseSMS(self):
        return Column(
            controls=[
                Row(
                    alignment='center',
                    controls=[
                        self.timer_text
                    ]
                )
            ]
        )



    def run_timer(self):
        threading.Thread(target=self.start_countdown).start()



    def start_countdown(self):
        for i in range(self.timer_seconds, 0, -1):
            time.sleep(1)
            self.timer_text.value = f"Vous pourrez demander un nouveau code dans {i // 60}:{i % 60:02d}"
            self.page.update()



    def run(self):
        self.page.add(self.container)


def main(page: Page):
    app = VerificationsNumber(page)
    app.run()


app(target=main, assets_dir="assets")
