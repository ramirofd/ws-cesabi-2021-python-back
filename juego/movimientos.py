from juego.constants import TipoMovimiento
from juego.pokemon import MAX_SALUD


class Movimiento:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def aplicar_efecto(self, pokemon):
        pass


class MovimientoAtaque(Movimiento):
    def __init__(self, nombre, danio):
        super(MovimientoAtaque, self).__init__(nombre, TipoMovimiento.ATAQUE)
        self.danio = danio

    def aplicar_efecto(self, pokemon):
        pokemon.salud = pokemon.salud - self.danio
        if pokemon.salud < 0:
            pokemon.salud = 0


class MovimientoCuracion(Movimiento):
    def __init__(self, nombre, cura):
        super(MovimientoCuracion, self).__init__(nombre, TipoMovimiento.CURACION)
        self.cura = cura

    def aplicar_efecto(self, pokemon):
        pokemon.salud = pokemon.salud + self.cura
        if pokemon.salud > MAX_SALUD:
            pokemon.salud = MAX_SALUD
