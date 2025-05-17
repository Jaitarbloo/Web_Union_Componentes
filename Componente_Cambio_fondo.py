import reflex as rx

app = rx.App (stylesheets=["/animation.css"])  # Tus hojas de estilo si las tienes)

def Cambio_fondo():
    
    return rx.box(
        
                rx.text("Freelance Developer", class_name="hero-text"),
                        class_name="hero-bg",
                        margin_top="20em",
                 )

app.add_page(Cambio_fondo, title="Cambio de Fondo")