import threading

from models.semaforo import Semaforo


class Interseccion:

    def __init__(
        self,
        id,
        x,
        y
    ):

        self.id = id
        self.x = x
        self.y = y

        self.vecinos = []

        self.lock = threading.Lock()

        self.ocupada = False
        self.auto_actual = None
        self.cola_autos = []
        self.semaforo = None
        self.orientacion = None

    def agregar_semaforo(
        self,
        direccion,
        verde,
        amarillo,
        rojo
    ):

        self.orientacion = direccion

        self.semaforo = Semaforo(
            direccion,
            verde,
            amarillo,
            rojo
        )

        self.semaforo.start()

    def intentar_ocupar(
        self,
        auto
    ):

        with self.lock:

            if self.ocupada:
                return False

            self.ocupada = True

            self.auto_actual = auto

            return True

    def liberar(self):

        with self.lock:

            self.ocupada = False

            self.auto_actual = None

    def __hash__(self):

        return hash(self.id)

    def __eq__(self, other):

        if not isinstance(
            other,
            Interseccion
        ):
            return False

        return self.id == other.id