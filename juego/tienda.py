from juego.objeto import Pocion, PokeBall


class Tienda:
    def __init__(self):
        self.items = [
            Pocion('Pocion', 5, 10, descripcion="Cura 10 puntos de salud"),
            Pocion('Super Pocion', 15, 20, descripcion="Cura 20 puntos de salud", nombre_url='super-potion'),
            Pocion('Max Pocion', 50, 100, descripcion="Cura todos los puntos de salud", nombre_url='max-potion'),
            PokeBall('Poke Ball', 10, 0.2, descripcion="Pokeball con 20% de probabilidad"),
            PokeBall('Great Ball', 20, 0.4, descripcion="Pokeball con 40% de probabilidad", nombre_url='great-ball'),
            PokeBall('Ultra Ball', 35, 0.95, descripcion="Pokeball con 95% de probabilidad", nombre_url='ultra-ball'),
        ]

    def comprar(self, nombre_objeto, personaje):
        obj = None
        for objeto in self.items:
            if nombre_objeto == objeto.nombre:
                obj = objeto

        if (personaje.dinero - obj.precio)>=0 and personaje.mochila.tiene_espacio():
            personaje.dinero = personaje.dinero - obj.precio
            personaje.mochila.guardar(obj)

        return personaje

    def vender(self, nombre_objeto, personaje):
        obj = personaje.mochila.sacar(nombre_objeto)
        personaje.dinero = personaje.dinero + obj.precio

        return personaje


TIENDA = Tienda()
