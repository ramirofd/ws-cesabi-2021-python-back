from juego.constants import PNG, URL_ITEM
from juego.pokemon import MAX_SALUD


class Pocion:
    def __init__(self, nombre, cura, nombre_url='potion', descripcion='', precio=5):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.cura = cura
        self.url = URL_ITEM + nombre_url + PNG

    def aplicar_efecto(self, pokemon):
        nueva_salud = pokemon.salud + self.cura
        pokemon.salud = nueva_salud if nueva_salud <= MAX_SALUD else MAX_SALUD
