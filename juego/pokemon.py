from random import randrange

MAX_SALUD = 100
MAX_MOVIMIENTOS = 4


class Pokemon:

    def __init__(self, nombre, imagen_frente=None, imagen_espalda=None, movimientos=None):
        self.nombre = nombre

        self.imagen_frente = imagen_frente
        self.imagen_espalda = imagen_espalda

        self.salud = MAX_SALUD

        if movimientos is None:
            self.movimientos = list()
        else:
            if len(movimientos) > MAX_MOVIMIENTOS:
                self.movimientos = movimientos[:MAX_MOVIMIENTOS]
            else:
                self.movimientos = movimientos

    def enseniar_movimiento(self, movimiento):
        if len(self.movimientos) < MAX_MOVIMIENTOS:
            self.movimientos.append(movimiento)

    def olvidar_movimiento(self, nombre_movimiento):
        for movimiento in self.movimientos:
            if movimiento.nombre == nombre_movimiento:
                self.movimientos.remove(movimiento)

    def buscar_movimiento(self, nombre_movimiento):
        for movimiento in self.movimientos:
            if movimiento.nombre == nombre_movimiento:
                return movimiento

    def movimiento_aleatorio(self):
        selector_movimiento = randrange(len(self.movimientos))
        return self.movimientos[selector_movimiento]

