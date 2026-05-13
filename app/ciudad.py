from models.camino import Camino
from models.interseccion import Interseccion


class Ciudad:

    def __init__(self, grid_size):

        self.grid_size = grid_size

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