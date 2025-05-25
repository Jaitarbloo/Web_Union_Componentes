import reflex as rx
import smtplib
from email.mime.text import MIMEText

class State(rx.State):
    pass

def Zabalgana_web_Vercel():
    fotos = [
        {"src": "20250413_113851.jpg",            "texto": "Desarrollo de sitios web rápidos y modernos."},
        {"src": "python.webp",                    "texto": "Diseño responsivo para móviles y escritorio."},
        {"src": "Visual-Studio-Code-Toolkit.jpg", "texto": "El potencial de bibliotecas de estilos de CSS y TailWind CSS, son imprescindibles para darle a tu web una apariencia única e innovadora."},
        {"src": "visual-studio-code.jpg",         "texto": "Visual Studio Code es mi entorno de desarrollo preferido, por su versatilidad y porque me permite mantener un flujo de trabajo ágil y organizado."},
        {"src": "20250413_113851.jpg",            "texto": "Desarrollo de sitios web rápidos y modernos."},
        {"src": "python.webp",                    "texto": "Diseño responsivo para móviles y escritorio."},
    ]
    return rx.center(
        
                    rx.vstack(
                            
                            rx.heading("Desarrollador Web Fullstack", size="9"),
                            
                            rx.text("Hola, mi nombre es Jaitarbloo y me dedico a la creación integral de páginas web.",
                                    "Aunque trabajo de forma independiente, formo parte de una gran comunidad de profesonales",
                                    
                                size="5",
                                align="center",
                                width="60%",
                                margin_top="1em",),
                            
                            rx.grid(
                                    *[
                                    rx.vstack( rx.image(src=f["src"], width="450px", height="300px",border_radius="8px"),
                                               rx.text(f["texto"] ,width="70%", size="3"),
                                             ) for f in fotos
                                     ],
                        
                                columns="2",
                                spacing="9",
                                padding="4em",
                                margin_top="2em",
                                  ),
        
                        align="center",
                        spacing="2",
                        padding="2em",
                            ),
                
                #spacing="4",
                justify="center",
                align="center",
                width="100%",
                #height="30vh",
                margin_top="2em",
                bg="#1a1a2e"
                    )
    
                

app = rx.App()
app.add_page(Zabalgana_web_Vercel, title="Zabalgana Web")