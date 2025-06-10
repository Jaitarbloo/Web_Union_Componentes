import reflex as rx
from Estilos import hero_bg_style, hero_text_style



def Cambio_fondo():
    
    return rx.box(
        
                rx.text("El fondo también comunica. Hagámoslo dinámico", style= hero_text_style ),#class_name="hero-text"
                        
            style=hero_bg_style,# class_name="hero-bg"
            margin_top="20em",
                    )
    
    
    
                
app = rx.App ()  # Tus hojas de estilo si las tienes,stylesheets=["/animation.css"]
app.add_page(Cambio_fondo, title="Cambio de Fondo")