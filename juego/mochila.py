

class Mochila:
    def __init__(self, capacidad=10):
        self.capacidad = capacidad
        self.objetos = dict()

    def tiene_espacio(self):
        return self.cantidad_objetos() < self.capacidad

    def cantidad_objetos(self):
        total = 0
        for lista in self.objetos.values():
            total += len(lista)
        return total

    def guardar(self, objeto):
        if self.tiene_espacio():
            if objeto.nombre in self.objetos:
                self.objetos[objeto.nombre].append(objeto)
            else:
                self.objetos[objeto.nombre] = [objeto]

    def sacar(self, nombre_objeto):
        if nombre_objeto in self.objetos:
            obj = self.objetos[nombre_objeto].pop(0)
            if len(self.objetos[nombre_objeto]) == 0:
                self.objetos.pop(nombre_objeto)
            return obj





