import reflex as rx
import asyncio

class State(rx.State):
    imagenes: list[str] = [
        "/concorde 1.jpg",
        "/concorde 2.jpg", 
        "/concorde 3.jpg",
        "/concorde 7.jpg"
    ]
    indice_actual: int = 0

    async def auto_slider(self):
        while True:
            await asyncio.sleep(3)
            self.indice_actual = (self.indice_actual + 1) % len(self.imagenes)
            yield

def Carrusel():
    return rx.flex(
        rx.image(
            src=State.imagenes[State.indice_actual],
            width="700px",
            height="300px"
        ),
          justify="center",
          align="center",
          width="100%",
          min_height="100vh"
    )

app = rx.App()
app.add_page(Carrusel,on_load=State.auto_slider)
