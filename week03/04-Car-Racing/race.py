import json
import sys
from random import uniform


class Car:
    def __init__(self, car: str, model: str, max_speed: float):
        if max_speed <= 0:
            raise ValueError('Max speed can not be negative.')

        self.car = str(car)
        self.model = str(model)
        self.max_speed = float(max_speed)

    def __str__(self):
        return '{} {} (max speed: {}km/h)'.format(self.car, self.model, self.max_speed)

    def __repr__(self):
        return self.__str__()


class Driver:
    def __init__(self, name: str, car: Car):
        self.name = name
        self.car = car

    def __str__(self):
        return '{} drives {}'.format(self.name, self.car)

    def __repr__(self):
        return self.__str__()


class Race:
    def __init__(self, drivers: list, crash_chance: float):
        if crash_chance < 0 or crash_chance > 1:
            raise ValueError('Crash chance must be in the range 0 - 1.')

        self.drivers = drivers
        self.crash_chance = round(float(crash_chance), 2)
        self._results = sorted(self.drivers, key=lambda d: d.car.max_speed, reverse=True)

    def print_results(self):
        results_points = dict(zip(reversed(self._results[:3]), [8, 6, 4]))

        for person, points in results_points.items():
            print('{} - {}'.format(person.name, points))

    def __str__(self):
        return 'Drivers in this race: {}, crash chance is {} out of 1'.format(
            ', '.join([driver.name for driver in self.drivers]),
            self.crash_chance
        )

    def __repr__(self):
        return self.__str__()


class Championship:
    def __init__(self, name: str, races_count: int):
        if races_count <= 0:
            raise ValueError('Races count can not be negative.')

        self.name = name
        self.races_count = int(races_count)
        self.drivers = self.load_drivers()
        self.races = []

        for i in range(1, races_count + 1):
            print('\nRace #{}'.format(i))
            print('###### START ######')

            race = Race(self.drivers, uniform(0, 1))
            race.print_results()
            self.races.append(race)

    @staticmethod
    def load_drivers():
        drivers = []

        with open('cars.json', mode='r', encoding='utf-8') as f:
            people = json.load(f)['people']

            for person in people:
                car = Car(person['car'], person['model'], person['max_speed'])

                driver = Driver(person['name'], car)
                drivers.append(driver)

        return drivers

    def top3(self):
        print('Total championship standings: ')
        for race in self.races:
            print(race)

    def __str__(self):
        return 'Championship {} consists of {} races'.format(self.name, self.races_count)


def main():
    if len(sys.argv) < 2:
        print('\n'.join([
            'Hello PyRacer!',
            'Please, call command with the proper argument: ',
            '$ python3 race.py start <name> <races_count> -> This will start a new championship with the given name, races count and drivers from cars.json',
            '$ python3 race.py standings -> This will print the standings for each championship that has ever taken place.'
        ]))

        return 1

    command = sys.argv[1]

    if command == 'start':
        name, races_count = sys.argv[2:]
        races_count = int(races_count)

        print('Starting a new championship called {} with {} races.'.format(name, races_count))
        print('Running {} races...'.format(races_count))

        championship = Championship(name, races_count)
        print(championship.top3())
        # TODO: Do the randomizing things.

    elif command == 'standings':
        pass
    else:
        print('{} is an invalid command.'.format(sys.argv[1]))
        return 1


if __name__ == '__main__':
    main()
