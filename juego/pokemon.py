from random import randrange

from juego.constants import POKEMON_NAMES, GIF, URL_POKEMON_FRONT_ANIM, URL_POKEMON_BACK_ANIM

MAX_SALUD = 100
MAX_MOVIMIENTOS = 4


class Pokemon:

    def __init__(self, nombre, movimientos=None):
        # pass
        self.nombre = nombre

        self.imagen_frente = URL_POKEMON_FRONT_ANIM + nombre.lower() + GIF
        self.imagen_espalda = URL_POKEMON_BACK_ANIM + nombre.lower() + GIF

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


def get_all_pokemons():
    poke_instances = []
    for nombre_pokemon in POKEMON_NAMES:
        poke_instances.append(Pokemon(nombre_pokemon))
    return poke_instances