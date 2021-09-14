from flask import Blueprint, request, session
from json import loads

import jsonpickle

from juego.personaje import Personaje
from juego.pokemon import Pokemon

endpoint = Blueprint('personaje', __name__)


@endpoint.route('/personaje', methods=['GET', 'POST', 'DELETE'])
def personaje():
    # try:
    pj = {}
    if request.method == 'POST':
        personaje_data = loads(request.data)
        pj = Personaje(personaje_data['nombre'])
        if hasattr(pj, 'agregar_pokemon'):
            for nombre in personaje_data['pokemons']:
                pj.agregar_pokemon(Pokemon(nombre))

    response = jsonpickle.encode(pj)
    return response


@endpoint.route('/personaje/pokemon/<nombre>', methods=['DELETE'])
def pokemon(nombre):
    
    if request.method == 'DELETE':
        personaje_data = loads(request.data)
        pj = Personaje(personaje_data['nombre'])
        if pj is not None and hasattr(pj, 'remover_pokemon'):
            pj.remover_pokemon(nombre)
        
    response = jsonpickle.encode(pj)
    return response
            
