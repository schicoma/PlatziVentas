import sys
import csv
import os

#CLIENTS_FILE = ':.clients.csv'
CLIENTS_FILE = "E:\\platzi\\python\\2019\\platzi_ventas\\.clients.csv"
CLIENTS_SCHEMA = ['name', 'company', 'email', 'position']
clients = []


def _initialize_clients_from_storage():
    # with open(CLIENTS_FILE, mode='r') as f:
    #     reader = csv.DictReader(f, CLIENTS_SCHEMA)
    #     for row in reader:
    #         clients.append(row)
    #     f.close()
    f = open(CLIENTS_FILE, mode="r")
    reader = csv.DictReader(f, fieldnames=CLIENTS_SCHEMA)

    for row in reader:
        clients.append(row)
    
    f.close()


def _save_clients_to_storage():
    tmp_file_name = '{}.tmp'.format(CLIENTS_FILE)

    with open(tmp_file_name, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames=CLIENTS_SCHEMA)
        writer.writerows(clients)

        f.close()

    os.remove(CLIENTS_FILE)
    os.rename(tmp_file_name, CLIENTS_FILE)


def create_client(client):
    # tomar la variable global para utilizarla dentro de a función
    #global clients
    if client not in clients:
        clients.append(client)
    else:
        print('Client already is in the client\'s list')


def list_clients():
    #global clients
    for idx, client in enumerate(clients):
        #print('{}: {}'.format(idx, client['name']))
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid=idx,
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position'],
        ))


def update_client(client_name, updated_client):
    #global clients

    for idx, client in enumerate(clients):
        if client_name == client['name']:
            clients[idx] = updated_client
            return True

    print('Client is not in client\'s list')
    return False


def delete_client(client_name):
    #global clients

    for idx, client in enumerate(clients):
        if client_name == client['name']:
            clients.pop(idx)
            return True

    print('Client is not in client\'s list')
    return False


def search_client(client_name):
    #global clients

    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return True


def _print_welcome():
    print("WELCOME TO PLATZI VENTAS")
    print("*" * 30)
    print("What would you like to do today?")
    print("[L]ist clients")
    print("[C]reate client")
    print("[U]pdate client")
    print("[D]elete client")
    print("[S]earch client")


def _get_client_name():
    client_name = None

    while not client_name or len(client_name.strip()) == 0:
        client_name = input("What is the client name? ")

        if client_name == 'exit':
            client_name = None
            break

    if not client_name:
        sys.exit()

    return client_name


def _get_client_field(field):
    client_field = None

    while not client_field or len(client_field.strip()) == 0:
        client_field = input("What is the client {}? ".format(field))

        # if client_field == 'exit':
        #     client_field = None
        #     break

    if not client_field:
        sys.exit()

    return client_field


def _get_client_user():
    return {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position')
    }


if __name__ == '__main__':
    # pass -> placeholder para determinar una función vacía
    _initialize_clients_from_storage()
    _print_welcome()

    command = input()
    command = command.upper()

    if command == "L":
        list_clients()
    elif command == "C":
        client = _get_client_user()

        create_client(client)
        # list_clients()
    elif command == 'U':
        client_name = _get_client_field('name')

        print('>>> Type the new client ')
        updated_client = _get_client_user()

        result = update_client(client_name, updated_client)

        if result:
            pass
            # list_clients()
    elif command == 'D':
        client_name = _get_client_name()
        result = delete_client(client_name)

        if result:
            pass
            # list_clients()
    elif command == 'S':
        client_name = _get_client_field('name')
        found = search_client(client_name)

        if found:
            print('The client is in the client\'s list')
        else:
            print('The client {} is not in our client\'s list'.format(client_name))

    else:
        print("Invalid command")

    _save_clients_to_storage()
