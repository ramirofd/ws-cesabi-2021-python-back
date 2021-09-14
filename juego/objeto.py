from juego.constants import PNG, URL_ITEM


class Objeto:
    def __init__(self, nombre, precio, descripcion, nombre_url):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.url = URL_ITEM + nombre_url + PNG


class Pocion(Objeto):
    def __init__(self, nombre, precio, cura, descripcion='', nombre_url='potion'):
        super(Pocion, self).__init__(nombre, precio, descripcion, nombre_url)
        self.cura = cura


class PokeBall(Objeto):
    def __init__(self, nombre, precio, prob_atrapar, descripcion='', nombre_url='poke-ball'):
        super(PokeBall, self).__init__(nombre, precio, descripcion, nombre_url)
        self.prob_atrapar = prob_atrapar