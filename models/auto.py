import random


class Auto:

    def __init__(self, inicio, destino):

        self.inicio = inicio
        self.destino = destino

        self.x = inicio.x
        self.y = inicio.y

        self.color = (
            random.randint(80, 255),
            random.randint(80, 255),
            random.randint(80, 255)
        )

        self.ruta = []

        self.route_index = 0

        self.speed = 0.03

    def update(self):

        if not self.ruta:
            return

        if self.route_index >= len(self.ruta):
            return

        objetivo = self.ruta[self.route_index]

        dx = objetivo.x - self.x
        dy = objetivo.y - self.y

        distancia = (dx ** 2 + dy ** 2) ** 0.5

        if distancia < self.speed:

            self.x = objetivo.x
            self.y = objetivo.y

            self.route_index += 1

        else:

            self.x += (dx / distancia) * self.speed
            self.y += (dy / distancia) * self.speed