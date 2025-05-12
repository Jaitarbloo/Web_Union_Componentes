import reflex as rx

app = rx.App(
    stylesheets=["/animation.css"],
)

def Cambio_fondo():
    return rx.box(
        rx.text("Freelance Developer", class_name="hero-text"),
        class_name="hero-bg",
        
    )

app.add_page(Cambio_fondo, title="Cambio de Fondo")