from flet import *
from pages.Acceuil import Acceuil
from pages.Inscription import Inscription
from pages.VerificationsNumber import VerificationsNumber


def views_handler(page):

    return {
        '/': View(
            route='/',
            controls=[
                Acceuil(page)
            ]
        ),
        '/Inscription': View(
            route='/Inscription',
            controls=[
                Inscription(page)
            ]
        ),
        '/Verification': View(  # Ajouter la route pour la page de vérification
            route='/Verification',
            controls=[
                VerificationsNumber(page)
            ]
        ),

    }

