from flask import Flask, session
from interface.personaje import endpoint as personaje_endpoint
from interface.pokemons import endpoint as pokemon_endpoint
from interface.tienda import endpoint as tienda_endpoint
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = 'TEST_KEY'

CORS(app)

app.register_blueprint(personaje_endpoint)
app.register_blueprint(pokemon_endpoint)
app.register_blueprint(tienda_endpoint)


@app.route("/")
def home():
    return 'ok'


if __name__ == "__main__":
    app.run(host='localhost', debug=True, port=5000)
