from flet import *
from views import views_handler




def main(page: Page):


    def change_route(route):
        print(f"Route actuelle: {route}")
        page.views.clear()
        if route in views_handler(page):
            page.views.append(
                views_handler(page)[route]
            )
        else:
            page.views.append(
                views_handler(page)['/']
            )

    page.on_route_change = change_route
    change_route('/')

app(target=main)
