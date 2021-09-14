from enum import Enum, auto


class TipoMovimiento(Enum):
    ATAQUE = auto()
    CURACION = auto()


PNG = ".png"
GIF = ".gif"
URL_POKEMON_FRONT_NORMAL = "https://img.pokemondb.net/sprites/black-white/normal/"
URL_POKEMON_BACK_NORMAL = "https://img.pokemondb.net/sprites/black-white/back-normal/"
URL_POKEMON_FRONT_ANIM = "https://img.pokemondb.net/sprites/black-white/anim/normal/"
URL_POKEMON_BACK_ANIM = "https://img.pokemondb.net/sprites/black-white/anim/back-normal/"
URL_ITEM = "https://img.pokemondb.net/sprites/items/"

POKEMON_NAMES = ["Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard",
    "Squirtle", "Wartortle","Blastoise","Caterpie","Metapod","Butterfree","Weedle",
    "Kakuna","Beedrill","Pidgey","Pidgeotto","Pidgeot","Rattata","Raticate",
    "Spearow","Fearow","Ekans","Arbok","Pikachu","Raichu","Sandshrew","Sandslash",
    "Nidoran-F","Nidorina","Nidoqueen","Nidoran-M","Nidorino","Nidoking","Clefairy",
    "Clefable","Vulpix","Ninetales","Jigglypuff","Wigglytuff","Zubat","Golbat",
    "Oddish","Gloom","Vileplume","Paras","Parasect","Venonat","Venomoth","Diglett",
    "Dugtrio","Meowth","Persian","Psyduck","Golduck","Mankey","Primeape","Growlithe",
    "Arcanine","Poliwag","Poliwhirl","Poliwrath","Abra","Kadabra","Alakazam","Machop",
    "Machoke","Machamp","Bellsprout","Weepinbell","Victreebel","Tentacool","Tentacruel",
    "Geodude","Graveler","Golem","Ponyta","Rapidash","Slowpoke","Slowbro","Magnemite",
    "Magneton","Farfetchd","Doduo","Dodrio","Seel","Dewgong","Grimer","Muk","Shellder",
    "Cloyster","Gastly","Haunter","Gengar","Onix","Drowzee","Hypno","Krabby","Kingler",
    "Voltorb","Electrode","Exeggcute","Exeggutor","Cubone","Marowak","Hitmonlee","Hitmonchan",
    "Lickitung","Koffing","Weezing","Rhyhorn","Rhydon","Chansey","Tangela","Kangaskhan",
    "Horsea","Seadra","Goldeen","Seaking","Staryu","Starmie","Mr-Mime","Scyther","Jynx",
    "Electabuzz","Magmar","Pinsir","Tauros","Magikarp","Gyarados","Lapras","Ditto","Eevee",
    "Vaporeon","Jolteon","Flareon","Porygon","Omanyte","Omastar","Kabuto","Kabutops",
    "Aerodactyl","Snorlax","Articuno","Zapdos","Moltres","Dratini","Dragonair","Dragonite",
    "Mewtwo","Mew"]
