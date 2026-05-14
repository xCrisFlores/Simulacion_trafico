import threading
import time


class Semaforo(threading.Thread):

    def __init__(
        self,
        direccion,
        verde,
        amarillo,
        rojo
    ):

        super().__init__(daemon=True)
        self.direccion = direccion  
        self.estado = "VERDE"
        self.verde = verde
        self.amarillo = amarillo
        self.rojo = rojo

    def run(self):

        while True:

            self.estado = "VERDE"
            time.sleep(self.verde)

            self.estado = "AMARILLO"
            time.sleep(self.amarillo)

            self.estado = "ROJO"
            time.sleep(self.rojo)