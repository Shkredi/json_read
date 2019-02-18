import json


def file_open():
    """
    Read data with JSON-file. Return name of file and data
    """
    file = None
    data = None
    while file is None or data is None:
        print('\nPlease type file path:', end='\t')
        file_name = input()
        # file_name = 'user_friends.json'

        try:
            file = open(file_name, 'r', encoding='UTF8')
            try:
                data = json.load(file)
            except json.decoder.JSONDecodeError:
                print('This is not JSON-file')

        except FileNotFoundError:
            print('No such file or directory:', file_name)

    return file_name, data


def print_list(data):
    """
    Print parameters for list
    """
    print('LIST:', len(data))
    obj = data[0]
    if type(obj) == dict:
        print('KEYS:', len(obj.keys()))
    else:
        for index in range(len(data)):
            print_dict(f' {index}\t{data[index]}')


def print_dict(data):
    """
    Print parameters for dictionary
    """
    print('KEYS:')
    for key in data.keys():
        print('\t' + key)


def print_current(path, data):
    """
    Print parametrs for current directory
    """
    print(f'\n{make_path(path)}/')
    if type(data) == dict:
        print_dict(data)
        return list(data.keys())

    elif type(data) == list:
        print_list(data)
        return list(range(len(data)))

    else:
        print(data)
        return []


def make_path(path_lst):
    """
    list -> str
    create string path
    """
    path = path_lst[0]
    for index in range(1, len(path_lst)):
        direct = path_lst[index]
        if type(direct) == int:
            path += '/' + str(direct)

        elif type(direct) == str:
            path += "/'" + direct + "'"

    return path


def main_loop():
    """
    run main loop
    """
    HELP = "\nType needed key to get information from dictionary\nAlso you can use next commands: exit, back (It's obvious what it does)\nPress Enter\n"

    file_name, data = file_open()

    print(HELP)
    input()

    path, current = [file_name], data
    command = ''
    while command != 'exit':
        print('\n'+'-'*50)
        current_keys = print_current(path, current)
        print()

        command = input(make_path(path)+'>\t')
        if command.isdigit():
            command = int(command)

        if command in current_keys:
            path.append(command)

            current = current[command]

        elif command == 'back':
            if len(path) > 1:
                path = path[:-1]
                if len(path) == 1:
                    current = data
                else:
                    current = eval(f'data[{"][".join(make_path(path).split("/")[1:])}]')

        elif command == 'exit':
            print('Thank you! Good day!')

        else:
            print('Not such command or key')


main_loop()

