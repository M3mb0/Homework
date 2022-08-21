import  uuid

def start_create_client_procedure():
    print("Add new client")
    file = open('clients.txt', 'a')
    client_id = uuid.uuid4()
    client_name = input('Client name: ')
    client_phone = input('Client phone: ')
    client_town = input('Client town: ')
    file.write(f'{client_id},{client_name},{client_phone},{client_town} \n')
    file.close()

    file = open('accounts.txt', 'a')
    file.write(f'{client_id},{0},RON\n')
    file.close()


def retrieve_client_id():
    client_data = retrieve_client_information()
    if client_data:
        return client_data['client_id']
    return None


def retrieve_client_information():
    print("Specify clinet's information")
    client_name = input("Client name: ")
    client_phone = input("Client phone: ")
    file = open('clients.txt', 'r')
    client_info = None
    for line in file:
        client_data = line.split(',')
        client_data_name = client_data[1]
        client_data_phone = client_data[2]
        if client_name == client_data_name and client_phone == client_data_phone:
            client_info = dict()
            client_info['client_name'] = client_data_name
            client_info['client_phone'] = client_data_phone
            client_info['client_city'] = client_data[3]
            client_info['client_id'] = client_data[0]
            file.close()
            return client_info
    file.close()
    return client_info