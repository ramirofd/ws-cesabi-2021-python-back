from juego.constants import TipoMovimiento
from juego.pokemon import MAX_SALUD


class Movimiento:
    def __init__(self, nombre, tipo):
        pass

    def aplicar_efecto(self, pokemon):
        pass


class MovimientoAtaque(Movimiento):
    def __init__(self, nombre, danio):
        pass

    def aplicar_efecto(self, pokemon):
        pass


class MovimientoCuracion(Movimiento):
    def __init__(self, nombre, cura):
        pass

    def aplicar_efecto(self, pokemon):
        pass
