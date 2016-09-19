import sys

from pandalism import Panda, PandaSocialNetwork


def main():
    network = PandaSocialNetwork()

    wencakisa = Panda("Vencislav", "wencakisa@pandamail.com", "male")
    marko = Panda("Martin", "matir8@pandamail.com", "male")
    tony = Panda("Tony", "tony@pandamail.com", "male")
    july = Panda("Juliyan", "julymaruli@pandamail.com", "male")
    stefoto = Panda("Stephan", "carmaniac@pandamail.com", "male")

    network.add_panda(wencakisa)
    network.add_panda(marko)
    network.add_panda(tony)
    network.add_panda(july)
    network.add_panda(stefoto)

    network.make_friends(wencakisa, marko)
    network.make_friends(marko, tony)
    network.make_friends(tony, july)
    network.make_friends(july, stefoto)

    print(network.connection_level(wencakisa, stefoto))

    network.save('sisko.json')


if __name__ == '__main__':
    sys.exit(main())
