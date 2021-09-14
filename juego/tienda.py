from juego.objeto import Pocion


class Tienda:
    def __init__(self):
        self.items = [
            Pocion('Pocion', 10, descripcion="Cura 10 puntos de salud"),
            Pocion('Super Pocion', 20, nombre_url='super-potion', descripcion="Cura 20 puntos de salud", precio=15),
            Pocion('Max Pocion', 100, nombre_url='max-potion', descripcion="Cura todos los puntos de salud", precio=50),
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
