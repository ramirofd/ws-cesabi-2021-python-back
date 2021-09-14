from juego.constants import TipoMovimiento


class Batalla:
    def __init__(self, jugador, enemigo):
        self.jugador = jugador
        self.enemigo = enemigo
        self.poke_jugador = jugador.pokemons[0]
        self.poke_enemigo = enemigo.pokemons[0]
        self.ganador = None

    def avanzar(self, nombre_movimiento=None, nombre_pocion=None):
        self.turno_jugador(nombre_movimiento, nombre_pocion)
        self.comprobar_ganador()
        self.turno_enemigo()
        self.comprobar_ganador()

    def turno_jugador(self, nombre_movimiento, nombre_pocion):
        if self.ganador is None:
            if nombre_movimiento is not None:
                movimiento = self.poke_jugador.buscar_movimiento(nombre_movimiento)
                if movimiento.tipo == TipoMovimiento.ATAQUE:
                    movimiento.aplicar_efecto(self.poke_enemigo)
                else:
                    movimiento.aplicar_efecto(self.poke_jugador)
            elif nombre_pocion is not None:
                pocion = self.jugador.mochila.sacar(nombre_pocion)
                pocion.aplicar_efecto(self.poke_jugador)

    def turno_enemigo(self):
        movimiento = self.poke_enemigo.movimiento_aleatorio()
        if movimiento.tipo == TipoMovimiento.ATAQUE:
            movimiento.aplicar_efecto(self.poke_jugador)
        else:
            movimiento.aplicar_efecto(self.poke_enemigo)

    def comprobar_ganador(self):

        if self.ganador is None and self.jugador.pokemon_sano() is None:
            self.ganador = self.enemigo
        else:
            self.poke_jugador = self.jugador.pokemon_sano()

        if self.ganador is None and self.enemigo.pokemon_sano() is None:
            self.ganador = self.jugador
        else:
            self.poke_enemigo = self.enemigo.pokemon_sano()



