from flask import Blueprint, request, session
from json import loads

import jsonpickle

from juego.personaje import Personaje
from juego.pokemon import Pokemon

endpoint = Blueprint('personaje', __name__)


@endpoint.route('/personaje', methods=['GET', 'POST', 'DELETE'])
def personaje():
    pj = {}
    try:
        if request.method == 'POST':
            personaje_data = loads(request.data)
            pj = Personaje(personaje_data['nombre'])
            if hasattr(pj, 'agregar_pokemon'):
                for nombre in personaje_data['pokemons']:
                    pj.agregar_pokemon(Pokemon(nombre))
    finally:
        return jsonpickle.encode(pj)
            
