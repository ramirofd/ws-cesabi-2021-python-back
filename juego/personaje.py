from juego.mochila import Mochila
from juego.pokemon import Pokemon

MAX_POKEMONS = 6
DINERO_INICIAL = 100


class Personaje:

    def __init__(self, nombre, pokemons=None):
        self.nombre = nombre
        self.mochila = Mochila()
        self.dinero = DINERO_INICIAL
        if pokemons is None:
            self.pokemons = list()
        else:
            self.pokemons = pokemons

    def agregar_pokemon(self, pokemon):
        if len(self.pokemons) < MAX_POKEMONS and pokemon not in self.pokemons:
            self.pokemons.append(pokemon)

    def remover_pokemon(self, nombre_pokemon):
        for pokemon in self.pokemons:
            if nombre_pokemon == pokemon.nombre:
                self.pokemons.remove(pokemon)
                return

    def pokemon_sano(self):
        for pokemon in self.pokemons:
            if pokemon.salud > 0:
                return pokemon
