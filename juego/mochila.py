
class Mochila:
    def __init__(self, capacidad=10):
        self.capacidad = capacidad
        self.bolsillos = dict()

    def guardar(self, objeto):
        if self.cantidad_objetos() < self.capacidad:
            if objeto in self.bolsillos:
                self.bolsillos[objeto] += 1
            else:
                self.bolsillos[objeto] = 1

    def sacar(self, nombre_objeto):
        for objeto in self.bolsillos.keys():
            if objeto.nombre == nombre_objeto and self.bolsillos[objeto]>0:
                self.bolsillos[objeto] -= 1
                return objeto

    def cantidad_objetos(self):
        total = 0
        for cantidad in self.bolsillos.values():
            total += cantidad

        return total



