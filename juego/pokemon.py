from juego.constants import POKEMON_NAMES, GIF, URL_POKEMON_FRONT_ANIM, URL_POKEMON_BACK_ANIM

MAX_SALUD = 100
MAX_MOVIMIENTOS = 4


class Pokemon:

    def __init__(self, nombre):
        self.nombre = nombre

        self.imagen_frente = URL_POKEMON_FRONT_ANIM + nombre.lower() + GIF
        self.imagen_espalda = URL_POKEMON_BACK_ANIM + nombre.lower() + GIF

        self.salud = MAX_SALUD


def get_all_pokemons():
    poke_instances = []
    for nombre_pokemon in POKEMON_NAMES:
        poke_instances.append(Pokemon(nombre_pokemon))
    return poke_instances