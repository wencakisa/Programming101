import sys
from datetime import datetime
from collections import defaultdict
import json


class Meal:
    def __init__(self, name: str, amount: int):
        self.name = name
        self.amount = amount
        self.date = datetime.now().date().strftime('%d.%m.%Y')
        self.calories = Calories()


class FoodDiary:
    def __init__(self):
        self._diary = defaultdict(list)

    def add(self, meal: Meal) -> None:
        """write what are you eating now"""
        self._diary[meal.date].append({
            'name': meal.name,
            'amount': meal.amount
        })

    def list_diary(self, date: str) -> str:
        """lists all the meals that you ate that day"""
        try:
            date = datetime.strptime(date, '%d.%m.%Y').strftime('%d.%m.%Y')
        except ValueError:
            print('Date should be in format <dd.mm.yyyy>')
            return 1

        if date in self._diary:
            return '\n'.join(meal['name'] for meal in self._diary[date])

        return 'No meals for this day.'


class Calories:
    def __init__(self):
        self.calories_filename = 'calories.json'
        self.calories_data = self._load_calories_data()

    def _load_calories_data(self) -> dict:
        with open(self.calories_filename, mode='r', encoding='utf-8') as f:
            return json.load(f)

    def has_meal(self, meal: Meal):
        return meal.name in self.calories_data

    def add_meal(self, meal: Meal, calories: int):
        self.calories_data[meal.name] = calories

    def get_calories(self, meal: Meal):
        return self.calories_data[meal.name]

    def extend_calories_file(self):
        with open(self.calories_filename, mode='w', encoding='utf-8') as f:
            json.dump(self.calories_data, f, indent=4)


class CLI:
    def __init__(self, diary: FoodDiary, calories: Calories):
        self._diary = diary
        self._calories = calories
        self._welcome_message = '\n'.join([
            'Hello and Welcome!',
            'Choose an option.',
            '1. meal - {}.'.format(self._diary.add.__doc__),
            '2. list <dd.mm.yyyy> - {},'.format(self._diary.list_diary.__doc__)
        ])

    def start_interface(self):
        print(self._welcome_message)

        while True:
            command = input('Enter command> ')

            if command == 'exit':
                self._calories.extend_calories_file()
                print('Goodbye!')
                break

            command = command.split(' ')

            if len(command) != 2:
                print('Please provide parameters.')
                continue

            command_name, param = command

            if command_name == 'meal':
                amount_eaten = int(input('How much have you eaten (in grams) ?> '))
                meal = Meal(name=param, amount=amount_eaten)

                if not self._calories.has_meal(meal):
                    print("I don't have {} in the calories database".format(meal.name))
                    calories = int(input('How much calories per 100g> '))
                    self._calories.add_meal(meal, calories)

                calories = self._calories.get_calories(meal)
                print('OK, this is a total of {:.2f} calories for this meal.'.format(meal.amount / calories))
                self._diary.add(meal)
            elif command_name == 'list':
                print(self._diary.list_diary(date=param))
            else:
                print('{} is an invalid command.'.format(command))


def main():
    food_diary = FoodDiary()
    calories = Calories()

    client = CLI(food_diary, calories)
    client.start_interface()

if __name__ == '__main__':
    sys.exit(main())
