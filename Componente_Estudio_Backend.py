"""
import reflex as rx
import requests
import os

# Noticias de ejemplo para no depender de la API
NOTICIAS_EJEMPLO = [
    {
        "title": "Python en el Desarrollo Web Moderno",
        "description": "Descubre cómo Python está transformando el desarrollo web con frameworks modernos",
        "url": "#"
    },
    {
        "title": "Novedades en Python 2025",
        "description": "Las características más esperadas que llegarán a Python este año",
        "url": "#"
    }
]

class NoticiasState(rx.State):
    noticias: list[dict] = NOTICIAS_EJEMPLO

    def fetch_news(self):
        # Usar noticias de ejemplo por ahora
        self.noticias = NOTICIAS_EJEMPLO

def Noticias():
    return rx.vstack(
        rx.heading(
            "Noticias de Código Python", 
            font_size="2em", 
            color="white", 
            margin_bottom="1em",
            margin_top="8em"  # Añadido para evitar que se oculte bajo el navbar
        ),
        rx.foreach(
            NoticiasState.noticias,
            lambda noticia: rx.card(
                rx.vstack(
                    rx.text(
                        noticia["title"],
                        font_weight="bold",
                        font_size="1.2em",
                        color="gray.800"
                    ),
                    rx.text(
                        noticia["description"],
                        color="gray.600",
                        font_size="0.9em",
                        no_of_lines=3
                    ),
                    rx.link(
                        "Leer más",
                        href=noticia["url"],
                        color="blue.500",
                        _hover={"color": "blue.700"}
                    ),
                ),
                width="100%",
                max_width="600px",
                margin_y="0.5em",
                padding="1em",
                shadow="lg",
                border_radius="md",
                background_color="white"
            )
        ),
        spacing="2",
        align="center",
        padding="2em",
        width="100%",
        min_height="100vh"
    )


app = rx.App()
app.add_page(Noticias, title="Noticias de Código Python")

"""

import reflex as rx

class EstudioState(rx.State):

    numero = 0
    

    def incrementar(self):
        self.numero += 1
    
    def decrementar(self):
        self.numero -= 1
   

def Estudio_Backend():
    
    return rx.center(

        rx.vstack(
            rx.heading("Estudio Backend", font_size="2em", color="white", margin_bottom="1em"),
            rx.text("Contador: ", font_size="1.2em", color="white"),
            rx.text(EstudioState.numero, font_size="1.5em", color="yellow"),
            rx.button("Incrementar", on_click=EstudioState.incrementar, background_color="green", color="white"),
            rx.button("Decrementar", on_click=EstudioState.decrementar, background_color="red", color="white"),
        ),
        #width="100%",
        align="center",
        display="flex",
        justify="center",
        align_items="center",
        
        
    )
    

app = rx.App()
app.add_page(Estudio_Backend) 


    

















