import flet as ft


def main(page: ft.Page):
    LargeurMobile = 450
    HauteurMobile = 780
    Bg_main = "#323232"
    Btn_ColorYellowGreen = "#adff2f"
    grayText = "#808080"
    
   
    
    page.adaptive = True
    
    PageConnection = ft.Container(
        width=LargeurMobile, 
        height=HauteurMobile, 
        bgcolor=Bg_main,
        border_radius=40,
        

        
        
        content=ft.Column(controls=[
            ft.Container(height=200),
           
           
            ft.Row(alignment='center', controls=[ 
                ft.Text('Indiquez Votre Numéro', size=27, color='white', 
                            weight='bold',font_family='poppins'),
                ]),           
           
            ft.Row(alignment='center',controls=[
                        ft.Text("Nous vous enverrons un code pour vérifier \n                votre numéro de téléphone",
                            size=17, color=grayText),
           ]
               ),

            ft.Container(height=30),
            
            ft.Row(alignment='center' ,controls=[
                ft.TextField(label="Numéro de téléphone", width=330,
                             border_radius=13, bgcolor=grayText)
                
                ]),
            
            ft.Row(alignment='center', controls=[
                                                ft.ElevatedButton(
                                                    text="Envoyer le code",width=320, height=50,
                                                    bgcolor=Btn_ColorYellowGreen,
                                                    color='black'
                                                )
            
                                        ]),
            
            
            ft.Row(alignment='center',controls=[
                ft.Text("Ou connectez vous sur", size=12, color=grayText)
                
            ]
                
                ),
            
            
            ft.Row(alignment='center',controls=[
                                                ft.ElevatedButton(                                                    
                                                    text ="Continuer avec Google", 
                                                    width=320, height=50,
                                                    bgcolor=grayText,
                                                    color='black'
                                                )
            
                                        ]),
            
            
            
            ft.Container(
             content=ft.Column( alignment='center',
                 controls=[
                    ft.Text("                L'adhésion à notre application signifie que vous acceptez\n                         nos ",
                            spans=[ft.TextSpan("Conditions d'utilisation ",ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE)),
                                                ft.TextSpan(" et notre "),
                                               ft.TextSpan("Politique de \n", ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE)),
                                               ft.TextSpan("                                                   "),
                                               ft.TextSpan("Confidentialité", ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE))
                                   
                                   ], 
                            size=12, color=grayText),
                            
                 ]
             )
         )
           
        ]
                          
            )
    )

    page.add(PageConnection)


ft.app(target=main, assets_dir='assets')
