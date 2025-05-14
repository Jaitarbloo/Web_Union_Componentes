import reflex as rx
from rxconfig import config

from Componente_Ampliacion_fotos import Ampliacion_fotos
from Componente_Carrusel_fotos import Carrusel
from Componente_Favicon_rotando import Favicon_rotando
from Componente_Navbar import navbar
from Componente_Cambio_imagen import Cambio_imagen
from Componente_Zabalgana_Web import Zabalgana_web_Vercel
from Componente_Cambio_fondo import Cambio_fondo
from Componente_Reborde_llamativo import Reborde_llamativo

class State(rx.State):
    pass


def index():
    return rx.vstack(
                    
                    navbar(),
                    
                    rx.heading( "WEB en construcción....disculpen las molestias",
                                align="center",
                                width="100%",
                                size="9",
                                margin_top="3em",
                                color="red"
                                ),
                    
                    Ampliacion_fotos(),
        
                    Cambio_fondo(), 
        
                    rx.text("Talento freelance listo para tu proyecto",
                            align="center",
                            width="100%",
                            size="8",
                            ),
        
                    Carrusel(),
        
                    Favicon_rotando(),
        
                    Cambio_imagen(),
        
                    Reborde_llamativo(),
        
                    Zabalgana_web_Vercel(),
        
                width="100%",
                min_height="100vh", 
                background_color="Blue",
                padding="0px"
                
                )



app = rx.App( stylesheets=["/animation.css"],  # Tus hojas de estilo si las tienes
            head_components=[rx.html("<html lang='es'>")]# Indica en el leguaje en el que está la página
)
app.add_page(index)
