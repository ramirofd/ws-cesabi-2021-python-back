from flask import Blueprint

import jsonpickle

endpoint = Blueprint('pokemon', __name__)


@endpoint.route('/pokemon', methods=['GET'])
def all_pokemons():
    instances = []
    max = None
    try:
        from juego.personaje import MAX_POKEMONS
        max = MAX_POKEMONS

        from juego.pokemon import get_all_pokemons
        instances = get_all_pokemons()


    finally:
        response = {
            'all_pokemons': instances,
            'max_pokemons': max
        }
        return jsonpickle.encode(response)
