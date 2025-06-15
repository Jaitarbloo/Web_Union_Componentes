import reflex as rx
import smtplib
from email.mime.text import MIMEText

class State(rx.State):
    pass

def Zabalgana_web_Vercel():
    
    fotos = [
        {"src": "Reflex.png",                        "texto": "Con Reflex desarrollo aplicaciones web completas (frontend y backend), optimizando tanto tiempo de desarrollo como consistencia entre vistas estáticas y funcionalidades dinámicas."},
        {"src": "Logotipo python.webp",              "texto": "Python me permite desarrollar sitios y aplicaciones web de forma ágil y estructurada, sin sacrificar rendimiento ni calidad. Es la base perfecta para construir productos web sólidos y fáciles de mantener."},
        {"src": "Visual-Studio-Code-Toolkit.jpg",    "texto": "El potencial de bibliotecas de estilos de CSS y TailWind CSS, son imprescindibles para darle a tu web una apariencia única e innovadora."},
        {"src": "visual-studio-code.jpg",            "texto": "Visual Studio Code es mi entorno de desarrollo preferido, por su versatilidad y porque me permite mantener un flujo de trabajo ágil y organizado."},
        {"src": "vercel-docker-proxy.jpg",           "texto": "Vercel & Docker...gracias a ellos publico interfaces de webs modernas con tiempos de respuesta mínimos y una infraestructura optimizada para el SEO técnico, buscadores de Google, etc."},
        {"src": "IrfanView-1.webp",                  "texto": "IrfanView, como gestor de imágenes, me permite reducir el peso de los recursos gráficos sin sacrificar la calidad y de esa forma consigo que tu proyecto web sea visualmente atractivo y altamente optimizado."},
        {"src": "6zTkyqP0n_2000x1500__1.jpg",        "texto": "Mi estructura es flexible y autónoma, trabajo en conjunto con diseñadores, programadores y otros expertos dependiendo de las necesidades de cada proyecto."},
        {"src": "Inteligencia-Artificial-.jpg",      "texto": "La IA me ayuda con el trabajo tedioso y repetitivo. De esa forma yo me centro en el trabajo que requiere criterio. Permitiéndome un trato más cercano con el cliente."},
    
    ]

    
    return rx.center(
                    
                    rx.vstack(
                            
                                rx.heading("Desarrollador Web Fullstack", size="9"),
                                
                                rx.text( "Hola, mi nombre es Jaitarbloo y me dedico a la creación integral de páginas web.",
                                    size="5",
                                    align="center",
                                    width=rx.breakpoints(initial="95%", md="70%", lg="60%"),
                                    margin_top="1em"
                                    ),
                            
                                rx.heading("Tecnologías que utilizo", size="8", margin_top="2em"),
                                
                                rx.grid(
                                        
                                        *[
                                    
                                        rx.vstack(
                                            rx.image( src=f["src"],
                                            width=rx.breakpoints(initial="95vw", md="350px", lg="450px"),
                                            height=rx.breakpoints(initial="200px", md="250px", lg="300px"),
                                            border_radius="8px"
                                            ),
                                    
                                        rx.text( f["texto"],
                                            width=rx.breakpoints(initial="100%", md="90%", lg="70%"),
                                            size="3"
                                            ),
                                            justify="center",
                                            align="center",
                                            ) for f in fotos
                                        ],

                                    columns=rx.breakpoints(initial="1", md="2", lg="2"),
                                    spacing=rx.breakpoints(initial="4", md="7", lg="9"),
                                    padding=rx.breakpoints(initial="1em", md="3em", lg="5em"),
                                    margin_top="2em",
                                        ),
            
                        align="center",
                        spacing="2",
                        padding=rx.breakpoints(initial="1em", md="2em", lg="4em"),
                        width=rx.breakpoints(initial="95%", md="90%", lg="80%"),
                             ),
        
                justify="center",
                align="center",
                width="100%",
                margin_top="2em",
                bg="#1a1a2e"
                    )

app = rx.App()
app.add_page(Zabalgana_web_Vercel, title="Zabalgana Web")
