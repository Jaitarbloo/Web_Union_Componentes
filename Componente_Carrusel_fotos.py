import reflex as rx

class CarruselState(rx.State):
    imagenes: list[str] = [
        "/minimal-landscape-sunrise-4k-jy-1280x720.jpg",
        "/556334.jpg", 
        "/Arcoiris.jpg",
        "/Aurora _voreal.jpg"
    ]
    indice_actual: int = 0

    @rx.event
    def siguiente_imagen(self):
        self.indice_actual = (self.indice_actual + 1) % len(self.imagenes)

def Carrusel():
    
    return rx.vstack(
                    rx.text("Talento freelance listo para tu proyecto", align="center", width="100%", size="8"),
                    rx.image(
                            src=CarruselState.imagenes[CarruselState.indice_actual],
                            width="700px",
                            height="300px",
                            border_radius="10px",
                            margin_top="7em"
                            ),
                    rx.moment(
                             interval=3000,  # milisegundos
                             on_change=CarruselState.siguiente_imagen,
                             display="none"  # el componente moment no se muestra
                            ),
                
                justify="center",
                align="center",
                width="100%",
                min_height="100vh"
                )





