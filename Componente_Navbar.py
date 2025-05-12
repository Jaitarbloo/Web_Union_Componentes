import reflex as rx
from rxconfig import config

def navbar() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.image(
                "/Logotipo Jb.jpg",
                height=rx.breakpoints(initial="60px", sm="80px", lg="100px"),
            ),
            rx.link(
                rx.text(
                    "Desarrollo y Diseño",
                    size="6",
                    color_scheme="gray",
                ),
                href="https://reflex.dev",
            ),
            rx.link(
                rx.text(
                    "Frameworks modernos",
                    size="6",
                    color_scheme="gray",
                ),
                href="https://reflex.dev",
            ),
            rx.link(
                rx.text(
                    "Trato cercano",
                    size="6",
                    color_scheme="gray",
                ),
                href="https://reflex.dev",
            ),
            rx.link(
                rx.text(
                    "Contáctame",
                    size="6",
                    color_scheme="gray",
                ),
                href="https://reflex.dev",
            ),
            rx.spacer(),
            rx.image(
                "Logotipo Jb.jpg",
                height=rx.breakpoints(initial="60px", sm="80px", lg="100px"),
            ),
            width="100%",
            height=rx.breakpoints(initial="60px", sm="80px", lg="100px"),      
            # Cambiamos a un gradiente negro-azul
            background="linear-gradient(45deg, #000033, #0000FF)",
            # Alternativas:
            # background="linear-gradient(45deg, #000022, #000088)"
            # background="linear-gradient(45deg, #1a1a2e, #000066)"
            spacing="9",
            align="center",
            position="fixed",
            top="0",
            z_index="999"
        ),
        background="linear-gradient(45deg, #000033, #0000FF)",  # Mismo gradiente
        justify="center",
        align="center",
        width="100%",
    )

app = rx.App()
app.add_page(navbar, title="Componente Navbar")