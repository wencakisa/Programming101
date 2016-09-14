import sys
import os
import json
from collections import defaultdict


def main():
    if len(sys.argv) < 2:
        print('Usage: {} <input_filename.json>'.format(os.path.relpath(sys.argv[0])))
        return 1

    input_filename = sys.argv[1]
    input_data = load_input_data(input_filename)

    people = input_data['people']
    language_skills = get_language_skills(people)

    for language, people in language_skills.items():
        print('{} - {}'.format(language, max(people, key=lambda l: l[1])[0]))


def load_input_data(input_filename: str):
    with open(input_filename, mode='r', encoding='utf-8') as f:
        return json.load(f)


def get_language_skills(people: dict) -> dict:
    result = defaultdict(list)

    for person in people:
        first_name = person['first_name']
        last_name = person['last_name']
        full_name = first_name + ' ' + last_name

        skills = person['skills']

        for skill in skills:
            language = skill['name']
            level = skill['level']

            result[language].append((full_name, level))

    return result

if __name__ == '__main__':
    sys.exit(main())
