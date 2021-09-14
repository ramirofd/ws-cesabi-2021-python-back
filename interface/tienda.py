from flask import Blueprint, request

import jsonpickle


endpoint = Blueprint('tienda', __name__)


@endpoint.route('/tienda', methods=['GET'])
def tienda():
    items = []
    try:
        from juego.tienda import TIENDA
        items = TIENDA.items
    finally:
        print(items)
        return jsonpickle.encode(items)


@endpoint.route('/tienda/comprar', methods=['POST'])
def comprar():
    data = jsonpickle.decode(request.data)
    pj = data['personaje']
    nombre_objeto = data['objeto']
    try:
        from juego.tienda import TIENDA
        pj = TIENDA.comprar(nombre_objeto, pj)
    finally:
        return jsonpickle.encode(pj)


@endpoint.route('/tienda/vender', methods=['POST'])
def vender():
    data = jsonpickle.decode(request.data)
    pj = data['personaje']
    nombre_objeto = data['objeto']
    try:
        from juego.tienda import TIENDA
        pj = TIENDA.vender(nombre_objeto, pj)
    finally:
        return jsonpickle.encode(pj)


