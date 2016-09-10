import sys
import os
import sqlite3


def main():
    print(welcome_message())

    with sqlite3.connect('polyglot.db') as connection:
        while True:
            command = parse_command(input('Enter command> '))

            if is_command(command, 'help'):
                print(help_command())
            elif is_command(command, 'list'):
                print(list_command(connection))
            elif is_command(command, 'start'):
                print(start_command(connection, command))
            elif is_command(command, 'answer'):
                print(answer_command(connection, command))
            elif is_command(command, 'reset'):
                print(reset_command(connection, command))
            elif is_command(command, 'exit'):
                break
            else:
                print('Invalid command... Please, look at help.')


def welcome_message() -> str:
    return '''
Hello and Welcome!
I am the compiler.
You can ask me to output different source files.
I will provide guides for compiling too.When you are ready, you can provide me with the answer from the code.
And I will reveal a secret to you!
Type help, to get you started.'''


def parse_command(command: str) -> tuple:
    return tuple(command.strip().split(' '))


def is_command(command_tuple: tuple, command_string: str) -> bool:
    return command_tuple[0] == command_string


def help_command() -> str:
    return '''
Here is a list of commands:
list - this will list all available languages
start <number> - this will start you with the language #number
answer <number> <answer> - this will check your answer for language #number
reset <number>* - this will set the answer as not answered.
    * - if no number is provided it will reset all the answers.

Your objective is to get all answers right!
But first, you have to finish the code for the compiler,
since it is not complete!'''


def fetch_languages(cursor) -> list:
    cursor.execute('select id, language, guide, answered from languages;')
    return cursor.fetchall()


def get_language_answered_state(answered: int) -> str:
    return 'NOT DONE' if answered == 0 else 'DONE'


def list_command(connection) -> str:
    cursor = connection.cursor()

    languages = fetch_languages(cursor)
    pattern = '{} [{}] - {}'

    return '\n'.join(
        map(
            lambda x: pattern.format(x[0], x[1], get_language_answered_state(x[3])),
            languages
        )
    )


def create_language_source(language: str, filename: str, source: str) -> None:
    with open(language + '/' + filename, mode='w') as f:
        f.write(source)


def start_command(connection, command: tuple) -> str:
    if len(command) < 2:
        return 'Please provide number parameter. Look at help.'

    cursor = connection.cursor()

    lang_id = int(command[1])

    query_lang = 'select language, guide, answered from languages where id = ?;'
    lang_result = cursor.execute(query_lang, (lang_id, )).fetchone()

    try:
        answer_state = get_language_answered_state(lang_result[2])
    except TypeError:
        return 'Language not found.'

    if answer_state == 'DONE':
        return 'Hey, you have done this. Go get another language!'

    query_sources = 'select file_name, source from sources where lang_id = ?;'
    sources_result = cursor.execute(query_sources, (lang_id, )).fetchone()

    language = lang_result[0]

    if not os.path.isdir(language):
        os.mkdir(language)

    create_language_source(language, sources_result[0], sources_result[1])

    return 'You have made a choice!\n{}'.format(lang_result[1])


def answer_command(connection, command: tuple) -> str:
    if len(command) < 3:
        return 'Please provide number and answer parameters. Look at help.'

    cursor = connection.cursor()

    lang_id = int(command[1])
    user_answer = command[2]

    if len(command) > 3:
        user_answer = ' '.join(command[i] for i in range(2, len(command)))

    query_lang = 'select language, answer from languages where id = ?;'
    lang_result = cursor.execute(query_lang, (lang_id, )).fetchone()

    language, answer = lang_result

    if not os.path.isdir(language):
        return "You haven't started this language yet. Look at help."

    if user_answer == answer:
        cursor.execute('update languages set answered = 1 where id = ?;', (lang_id, ))
        return 'Your answer is valid! Congratulations!'

    return 'Hmm... This seems to be and invalid answer. Try again. :o)'


def reset_command(connection, command) -> str:
    cursor = connection.cursor()

    number = command[1] if len(command) > 1 else 0

    if number != 0:
        cursor.execute('update languages set answered = 0 where id = ?;', (number, ))
        return "Answer #{}'s state is set to 'NOT ANSWERED'.".format(number)
    else:
        cursor.execute('update languages set answered = 0;')
        return "Every answer's state is set to 'NOT ANSWERED'."

if __name__ == '__main__':
    sys.exit(main())
