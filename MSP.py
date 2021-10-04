import random

SUBJECTS = ['Administrator', 'User1', 'User2', 'User3', 'User4']
OBJECTS = ['Document.docx', 'cat.png', 'Pursuit(JAWNS Version).mp3']
LEVELS_OBJECTS = [1, 2, 3, 4]
LEVELS_SUBJECTS = [1, 2, 3, 4]


def Enter():
    """ENTRY MENU"""
    print('AUTORIZATION')
    print('1.Sing in')
    print('0.Out')
    enter = int(input('Enter: '))
    return enter


def ui():
    """UI"""
    print('Login: ')


def get_key(dict, value):
    """GET THE KEY WITH A KNOWN VALUE FROM LIST"""
    for key, val in dict.items():
        if val == value:
            return key


def func_SUBJECT(list1, list2):
    """SHUFFLING ELEMENTS & CREATING KEY/VALUE PAIRS FOR SUBJECT"""
    dictionary = {}
    list1 = sorted(list1, key=lambda list1: random.random())
    list2 = sorted(list2, key=lambda list1: random.random())
    dictionary = dict(zip(list1, list2))
    for item in range(len(SUBJECTS)):
        if (SUBJECTS[item] in dictionary.values()) == False:
            dictionary[SUBJECTS[item]] = random.choice(LEVELS_SUBJECTS)
    dictionary['Administrator'] = 0
    return dictionary


def func_OBJECT(list1, list2):
    """SHUFFLING ELEMENTS & CREATING KEY/VALUE PAIRS FOR OBJECT"""
    dictionary = {}
    list1 = sorted(list1, key=lambda list1: random.random())
    list2 = sorted(list2, key=lambda list1: random.random())
    dictionary = dict(zip(list1, list2))
    return dictionary


SUBJECTS_DICT = func_SUBJECT(SUBJECTS, LEVELS_SUBJECTS)
OBJECTS_DICT = func_OBJECT(OBJECTS, LEVELS_OBJECTS)


def CheckAccessOnReadAndWrite(login, dictionary_subject, dictionary_object):
    """CHECKING THE FILE ACCESS LEVEL"""
    if login == 'Administrator' and dictionary_subject[login] == 0:
        print('SELECT FILE:\n')
        for key in dictionary_object.keys():
            print(key)
        filename = str(input('Select file: '))

    elif dictionary_subject[login] == 4:
        print('SELECT FILE:')
        for item in list(dictionary_object.values()):
            if item <= 4 and item in dictionary_object.values():
                print(get_key(dictionary_object, item))
        filename = str(input('Select file: '))

    elif dictionary_subject[login] == 3:
        print('SELECT FILE:')
        for item in list(dictionary_object.values()):
            if item <= 3 and item in dictionary_object.values():
                print(get_key(dictionary_object, item))
        filename = str(input('Select file: '))

    elif dictionary_subject[login] == 2:
        print('SELECT FILE:')
        for item in list(dictionary_object.values()):
            if item <= 2 and item in dictionary_object.values():
                print(get_key(dictionary_object, item))
        filename = str(input('Select file: '))

    elif dictionary_subject[login] == 1:
        print('SELECT FILE:')
        for item in list(dictionary_object.values()):
            if item <= 1 and item in dictionary_object.values():
                print(get_key(dictionary_object, item))
        filename = str(input('Select file: '))


def CheckAccsessOnChange(login, dictionary_subject, dictionary_object):
    classification = int(input('Enter classification: '))
    SUBJECTS_DICT['Administrator'] = classification
    print(f'Administrator classification is: {classification}')


def PrintLevelAccess(dictionary_subject, dictionary_object):
    """PRINT LEVEL ACCESS"""
    print("OBJECTS:")
    for key, value in dictionary_object.items():
        print(f'{key} : {value}')
    print('--------------------------------------------')
    for key, value in dictionary_subject.items():
        print(f'{key} : {value}')


def main():
    enter = Enter()
    if enter == 0:
        return
    else:
        while True:
            ui()
            PrintLevelAccess(SUBJECTS_DICT, OBJECTS_DICT)
            login = str(input('Login: '))
            if (login in SUBJECTS_DICT.keys()) and (SUBJECTS_DICT[login] == 0):
                command = str(input('Command: '))
                if command == 'read':
                    CheckAccessOnReadAndWrite(
                        login, SUBJECTS_DICT, OBJECTS_DICT)
                    print(
                        '-------------------------------------------Read success!-------------------------------------------')
                elif command == 'write':
                    CheckAccessOnReadAndWrite(
                        login, SUBJECTS_DICT, OBJECTS_DICT)
                    print(
                        '-------------------------------------------Write success!-------------------------------------------')
                elif command == 'change':
                    CheckAccsessOnChange(login, SUBJECTS_DICT, OBJECTS_DICT)
                    pass

            if (login in SUBJECTS_DICT.keys()) and (SUBJECTS_DICT[login] == 3):
                command = str(input('Command: '))
                if command == 'read':
                    CheckAccessOnReadAndWrite(
                        login, SUBJECTS_DICT, OBJECTS_DICT)
                    print(
                        '-------------------------------------------Read success!-------------------------------------------')
                elif command == 'write':
                    CheckAccessOnReadAndWrite(
                        login, SUBJECTS_DICT, OBJECTS_DICT)
                    print(
                        '-------------------------------------------Write success!-------------------------------------------')

            if (login in SUBJECTS_DICT.keys()) and (SUBJECTS_DICT[login] == 4):
                command = str(input('Command: '))
                if command == 'read':
                    CheckAccessOnReadAndWrite(
                        login, SUBJECTS_DICT, OBJECTS_DICT)
                    print(
                        '-------------------------------------------Read success!-------------------------------------------')
                elif command == 'write':
                    CheckAccessOnReadAndWrite(
                        login, SUBJECTS_DICT, OBJECTS_DICT)
                    print(
                        '-------------------------------------------Write success!-------------------------------------------')

            if (login in SUBJECTS_DICT.keys()) and (SUBJECTS_DICT[login] == 1):
                command = str(input('Command: '))
                if command == 'read':
                    CheckAccessOnReadAndWrite(
                        login, SUBJECTS_DICT, OBJECTS_DICT)
                    print(
                        '-------------------------------------------Read success!-------------------------------------------')
                elif command == 'write':
                    CheckAccessOnReadAndWrite(
                        login, SUBJECTS_DICT, OBJECTS_DICT)
                    print(
                        '-------------------------------------------Write success!-------------------------------------------')

            if (login in SUBJECTS_DICT.keys()) and (SUBJECTS_DICT[login] == 2):
                command = str(input('Command: '))
                if command == 'read':
                    CheckAccessOnReadAndWrite(
                        login, SUBJECTS_DICT, OBJECTS_DICT)
                    print(
                        '-------------------------------------------Read success!-------------------------------------------')
                elif command == 'write':
                    CheckAccessOnReadAndWrite(
                        login, SUBJECTS_DICT, OBJECTS_DICT)
                    print(
                        '-------------------------------------------Write success!-------------------------------------------')
            if (login not in SUBJECTS_DICT.keys()):
                print('AUTORAZATION FAILED')
                break


if __name__ == '__main__':
    main()
