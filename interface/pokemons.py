from flask import Blueprint

import jsonpickle


endpoint = Blueprint('pokemon', __name__)


@endpoint.route('/pokemon', methods=['GET'])
def all_pokemons():
    instances = []
    max = None
    try:
        from juego.pokemon import get_all_pokemons
        from juego.personaje import MAX_POKEMONS
        instances = get_all_pokemons()
        max = MAX_POKEMONS

    finally:
        response = {
            'all_pokemons': instances, 
            'max_pokemons': max
        }
        return jsonpickle.encode(response)
