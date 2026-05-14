import random

from ui.colors import Colores


class Auto:

    def __init__(self, inicio, destino):

        self.inicio = inicio
        self.destino = destino

        self.x = inicio.x
        self.y = inicio.y

        self.color_original = (
            random.randint(80, 255),
            random.randint(80, 255),
            random.randint(80, 255)
        )

        self.color = self.color_original

        self.ruta = []

        self.route_index = 0

        self.speed = 0.03

        self.interseccion_actual = inicio

        self.terminado = False

    def update(self):

        if not self.ruta:
            return

        if self.route_index >= len(self.ruta):
            self.terminado = True
            self.color = Colores.VERDE
            return

        objetivo = self.ruta[self.route_index]

        # =========================
        # DIRECCION DEL TRAMO
        # =========================

        dx_nodo = objetivo.x - self.interseccion_actual.x
        dy_nodo = objetivo.y - self.interseccion_actual.y

        direccion_movimiento = (
            "HORIZONTAL" if dx_nodo != 0 else "VERTICAL"
        )

        # =========================
        # SEMAFORO (del nodo actual)
        # =========================

        semaforo = self.interseccion_actual.semaforo

        if semaforo is not None:
            if (
                semaforo.direccion == direccion_movimiento
                and semaforo.estado == "ROJO"
            ):
                return

        # =========================
        # MOVIMIENTO
        # =========================

        dx = objetivo.x - self.x
        dy = objetivo.y - self.y

        distancia = (dx ** 2 + dy ** 2) ** 0.5

        # 🔥 LLEGADA AL NODO (AQUÍ SE RESERVA)
        if distancia < self.speed:

            # liberar anterior
            self.interseccion_actual.liberar()

            # actualizar nodo
            self.interseccion_actual = objetivo

            # ocupar nuevo nodo
            objetivo.intentar_ocupar(self)

            self.x = objetivo.x
            self.y = objetivo.y

            self.route_index += 1

        else:
            # movimiento continuo sin bloquear nodos
            self.x += (dx / distancia) * self.speed
            self.y += (dy / distancia) * self.speed
    
   
