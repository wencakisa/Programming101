import re
import json


class Panda:
    def __init__(self, name: str, email: str, gender: str):
        self.__name = name
        self.__email = email
        self.__gender = gender

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError('Name must be a string.')

        self.__name = name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        if re.search(r'[^@]+@[^@]+\.[^@]+', email) is None:
            raise ValueError('Please provide a valid email.')

        self.__email = email

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender: str):
        if not gender == 'male' or not gender == 'female':
            raise ValueError('Invalid gender: {}'.format(gender))

        self.__gender = gender

    def is_male(self):
        return self.__gender == 'male'

    def is_female(self):
        return self.__gender == 'female'

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash(self.__name)

    def __str__(self):
        return self.__name

    def __repr__(self):
        return self.__str__()


class PandaSocialNetwork:
    class PandaException(Exception):
        def __init__(self, message: str=''):
            super().__init__(message)

    class PandaAlreadyThereException(PandaException):
        def __init__(self):
            super().__init__(message='Panda is already there.')

    class PandasAlreadyFriends(PandaException):
        def __init__(self):
            super().__init__(message='Pandas are already friends.')

    def __init__(self):
        self.__pandas = {}
        # key: Panda instance
        # value: list of pandas (friends)

    def add_panda(self, panda: Panda):
        if panda in self.__pandas:
            raise self.PandaAlreadyThereException()

        self.__pandas[panda] = []

    def has_panda(self, panda: Panda) -> bool:
        return panda in self.__pandas

    def make_friends(self, panda1: Panda, panda2: Panda):
        if panda1 not in self.__pandas:
            self.__pandas[panda1] = []
        if panda2 not in self.__pandas:
            self.__pandas[panda2] = []

        if self.are_friends(panda1, panda2):
            raise self.PandasAlreadyFriends()

        self.__pandas[panda1].append(panda2)
        self.__pandas[panda2].append(panda1)

    def are_friends(self, panda1, panda2):
        return panda1 in self.__pandas[panda2] or panda2 in self.__pandas[panda1]

    def friends_of(self, panda):
        return self.__pandas[panda] if panda in self.__pandas else False

    def connection_level(self, panda1, panda2):
        if self.are_friends(panda1, panda2):
            return 1

        if not self.has_panda(panda1) or not self.has_panda(panda2):
            return False

        pass

    def are_connected(self, panda1, panda2):
        pass

    def how_many_gender_in_network(self, level, panda, gender):
        pass

    def save(self, file_name: str):
        with open(file_name, mode='w') as f:
            json.dump(
                {
                    str(panda): list(map(str, friends))
                    for panda, friends in self.__pandas.items()
                },
                f,
                indent=4
            )

    @staticmethod
    def load(file_name: str):
        with open(file_name, mode='r') as f:
            return json.load(f)
