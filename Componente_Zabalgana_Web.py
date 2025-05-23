import reflex as rx
import smtplib
from email.mime.text import MIMEText

class State(rx.State):
    pass

def Zabalgana_web_Vercel():
    fotos = [
        {"src": "20250413_113851.jpg", "texto": "Desarrollo de sitios web rápidos y modernos."},
        {"src": "python.webp", "texto": "Diseño responsivo para móviles y escritorio."},
        {"src": "Visual-Studio-Code-Toolkit.jpg", "texto": "Trato directo con el cliente."},
        {"src": "visual-studio-code.jpg", "texto": "Soporte y mantenimiento personalizado."},
    ]
    return rx.center(
        
                    rx.vstack(
                            
                            rx.heading("Desarrollador Web Freelancer", size="8"),
                            
                            rx.text("Hola, soy desarrollador web freelance..."),
                            
                            rx.grid(
                                    *[
                                    rx.vstack( rx.image(src=f["src"], width="400px", height="250px"),
                                               rx.text(f["texto"], align="center"),
                                             ) for f in fotos
                                     ],
                        
                                columns="2",
                                spacing="6",
                                padding="4em",
                                  ),
        
                        align="center",
                        spacing="2",
                        padding="2em"
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