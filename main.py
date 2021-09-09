from juego.objeto import Pocion
import jsonpickle


def print_hi(name):
    a = Pocion('pocion chica', 'es una pocion curativa', 50, 10)

    print(jsonpickle.dumps(a))


if __name__ == '__main__':
    print_hi('PyCharm')
