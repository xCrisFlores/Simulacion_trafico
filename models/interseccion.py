class Interseccion:

    def __init__(self, id, x, y):

        self.id = id

        self.x = x
        self.y = y

        self.vecinos = []

    def __hash__(self):

        return hash(self.id)

    def __eq__(self, other):

        if not isinstance(other, Interseccion):
            return False

        return self.id == other.id