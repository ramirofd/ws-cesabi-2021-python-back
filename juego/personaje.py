from mochila import Mochila

MAX_POKEMONS = 3


class Personaje:

    def __init__(self, nombre, pokemons=None):
        self.nombre = nombre
        self.mochila = Mochila()
        if pokemons is None:
            self.pokemons = list()
        else:
            self.pokemons = pokemons

    def agregar_pokemon(self, pokemon):
        if len(self.pokemons) < MAX_POKEMONS and pokemon not in self.pokemons:
            self.pokemons.append(pokemon)

    def remover_pokemon(self, pokemon):
        if pokemon in self.pokemons:
            self.pokemons.remove(pokemon)

    def pokemon_sano(self):
        for pokemon in self.pokemons:
            if pokemon.salud > 0:
                return pokemon
