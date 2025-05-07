import reflex as rx
from rxconfig import config

from Componente_Ampliacion_fotos import Ampliacion_fotos
from Componente_Carrusel_fotos import Carrusel
from Componente_Favicon_rotando import Favicon_rotando
from Componente_Navbar import navbar
from Componente_Cambio_imagen import Cambio_imagen
from Componente_Zabalgana_Web import Zabalgana_web_Vercel


class State(rx.State):
    """The app state."""
    pass

def index():
      return rx.vstack(
        navbar(),
        rx.heading(
            "WEB en construcción....disculpen las molestias",
            align="center",
            width="100%",
            size="8",
            margin_top="3em",
            color="red"),
        Ampliacion_fotos(),
        rx.text(
            "Talento freelance listo para tu proyecto",
            align="center",
            width="100%",
            size="8"
        ),
        Carrusel(),
        rx.text(
            "Trabajo rápido, resultados profesionales.",
            align="center",
            width="100%",
            size="8"
        ), 
        Favicon_rotando(),
        rx.text(
            "¡Contáctame y hagamos magia juntos!",
            align="center",
            width="100%",
            size="8"
        ),
        Cambio_imagen(),
        Zabalgana_web_Vercel(),
        width="100%",
        min_height="100vh",  # Asegura que el fondo cubra toda la altura
        bg="linear-gradient(90deg, #11998e 0%, #38ef7d 100%)",  # Cambia el color de fondo aquí
    )

app = rx.App(
    stylesheets=[],  # Tus hojas de estilo si las tienes
    head_components=[
        rx.html("<html lang='es'>"),  # Indica el idioma español
    ]
)
app.add_page(index)
