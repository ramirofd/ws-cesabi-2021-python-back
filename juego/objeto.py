from pokemon import MAX_SALUD


class Pocion:
    def __init__(self, nombre, descripcion, precio, cura):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.cura = cura

    def aplicar_efecto(self, pokemon):
        nueva_salud = pokemon.salud + self.cura
        pokemon.salud = nueva_salud if nueva_salud <= MAX_SALUD else MAX_SALUD
