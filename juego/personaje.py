from juego.mochila import Mochila

MAX_POKEMONS = 6
DINERO_INICIAL = 100


class Personaje:

    def __init__(self, nombre):
        self.nombre = nombre
        self.dinero = DINERO_INICIAL
        self.pokemons = list()
        self.mochila = Mochila()

    def agregar_pokemon(self, pokemon):
        if len(self.pokemons) < MAX_POKEMONS and pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
