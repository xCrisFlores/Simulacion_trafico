import pygame
from concurrent.futures import ThreadPoolExecutor
from app.ciudad import Ciudad
from app.render import Render
from models.auto import Auto
from rutas.astaralg import AStarAlg


class Simulacion:

    def __init__(self, config):

        pygame.init()

        self.screen = pygame.display.set_mode(
            (
                config["window_width"],
                config["window_height"]
            )
        )

        pygame.display.set_caption(
            "Simulacion de Trafico"
        )

        self.clock = pygame.time.Clock()

        self.running = True

        self.tile_size = config["tile_size"]

        self.ciudad = Ciudad(
            config["grid_size"]
        )


        self.alg = AStarAlg()

        self.renderer = Render(
            self.screen,
            self.ciudad,
            self.tile_size
        )

        self.autos = []

        self.create_autos()

    def create_autos(self):
        """ Creacion de autos con rutas predefinidas para testing"""

        puntos = [

            (
                self.ciudad.intersecciones[2][1],
                self.ciudad.intersecciones[8][8]
            ),

            (
                self.ciudad.intersecciones[8][5],
                self.ciudad.intersecciones[1][8]
            ),

            (
                self.ciudad.intersecciones[8][8],
                self.ciudad.intersecciones[7][8]
            ),

            (
                self.ciudad.intersecciones[8][0],
                self.ciudad.intersecciones[1][7]
            ),

            (
                self.ciudad.intersecciones[4][5],
                self.ciudad.intersecciones[1][3]
            ),

            (
                self.ciudad.intersecciones[3][2],
                self.ciudad.intersecciones[1][3]
            )

        ]

        for inicio, destino in puntos:

            auto = Auto(
                inicio,
                destino
            )

            self.autos.append(auto)

        with ThreadPoolExecutor() as executor:

            rutas = list(
                executor.map(
                    lambda auto:
                        self.alg.calcular_ruta(
                            auto.inicio,
                            auto.destino
                        ),
                    self.autos
                )
            )

        for auto, ruta in zip(
            self.autos,
            rutas
        ):

            auto.ruta = ruta

        

    def update(self):

        for auto in self.autos:
            auto.update()

    def handle_events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                self.running = False

    def run(self):

        while self.running:

            self.handle_events()

            self.update()

            self.renderer.render(
                self.autos
            )

            pygame.display.flip()

            self.clock.tick(60)

        pygame.quit()