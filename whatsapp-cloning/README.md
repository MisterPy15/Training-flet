# A whatsapp-cloning Flet app

An example of a minimal Flet app.

To run the app:

```
flet run [app_directory]
```


     
     
     
   img = Image(src="icons/Acceuil.png")

        if os.path.exists(img):

            return Row(
                alignment='center', controls=[
                    foreground_image_src='images/Profil.JPG',
            Image(src=img, width=350, height=250)
                ]
            )
        else:
            print(f"Image non trouvée à l'emplacement : {img}")
            return Row(
                alignment='center', controls=[
                    Text("Image non trouvée", color="red", size=20)
                ]
            )






 def create_image(self):
        image_path = "Acceuil.png"

        return Row(
            alignment='center',
            controls=[
                Container(
                    width=400,
                    height=300,
                    border_radius=50,
                    content=CircleAvatar(
                        opacity=0.1,
                        foreground_image_src=image_path,
                    )
                )
            ]
        )








categories_cards = Row(scroll='auto')
    categories = ['Famille', 'Busnesse', 'Amis', 'Travail', 'Loisir']
    
    for i, Catego in enumerate(categories):
        categories_cards.controls.append(Container(bgcolor=BG, height=100, 
                                                    width=170, border_radius=15, padding=15, content=Column(
                                                        controls=[
                                                            Text('0 Tâche'),
                                                            Text(Catego),
                                                            Container(width=160, height=5, bgcolor='white12', 
                                                                      border_radius=20, padding=padding.only(right=60, left=60), 
                                                                      content=Container(bgcolor=ORANGE))
                                                        ]
                                                    )))
