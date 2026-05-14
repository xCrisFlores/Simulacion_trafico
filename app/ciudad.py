from models.camino import Camino
from models.interseccion import Interseccion


class Ciudad:

    def __init__(
        self,
        config
    ):

        self.grid_size = config["grid_size"]
        self.config = config

        self.intersecciones = []
        self.caminos = []

        self.generar()

    def generar(self):

        for y in range(self.grid_size):

            row = []

            for x in range(self.grid_size):

                interseccion = Interseccion(
                    f"{x}-{y}",
                    x,
                    y
                )

                row.append(interseccion)

            self.intersecciones.append(row)

        for y in range(self.grid_size):

            for x in range(self.grid_size):

                current = self.intersecciones[y][x]

                if y % 2 == 0:

                    if x < self.grid_size - 1:

                        right = self.intersecciones[y][x + 1]

                        self.caminos.append(
                            Camino(current, right)
                        )

                        current.vecinos.append(right)

                else:

                    if x > 0:

                        left = self.intersecciones[y][x - 1]

                        self.caminos.append(
                            Camino(current, left)
                        )

                        current.vecinos.append(left)

                if x % 2 == 0:

                    if y < self.grid_size - 1:

                        down = self.intersecciones[y + 1][x]

                        self.caminos.append(
                            Camino(current, down)
                        )

                        current.vecinos.append(down)

                else:

                    if y > 0:

                        up = self.intersecciones[y - 1][x]

                        self.caminos.append(
                            Camino(current, up)
                        )

                        current.vecinos.append(up)
        self.generar_semaforos()
    
    def generar_semaforos(self):

        semaforos = [

            (2, 2, "HORIZONTAL"),
            (2, 5, "VERTICAL"),
            (2, 8, "HORIZONTAL"),

            (5, 2, "VERTICAL"),
            (5, 5, "HORIZONTAL"),
            (5, 8, "VERTICAL"),

            (8, 2, "HORIZONTAL"),
            (8, 5, "VERTICAL"),
            (8, 8, "HORIZONTAL"),

            (4, 4, "VERTICAL")
        ]

        for x, y, direccion in semaforos:

            interseccion = self.intersecciones[y][x]

            interseccion.agregar_semaforo(
                direccion,
                self.config["semaforo_verde"],
                self.config["semaforo_amarillo"],
                self.config["semaforo_rojo"]
            )