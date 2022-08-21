# Bank app V1

from Authentication import must_login, logout
from Comands import *
from Clients import *
from Accounts import *

IS_USER_LOGED_IN = False

print('''
    Welcome to the Titulescu Bank!
    If you don't know how to use the application please use the "help" command.
''')
while True:
    user_command = input('Please specify your command: ').lower()
    if user_command == EXIT_COMMAND:
        break
    elif user_command == HELP_COMMAND:
        print('''
        This application can do a multitude of things based on the command that was imputed.
        Commands available :
            - add_client Starts process for adding new client
            - read_balance Shows client's account balance
            - logout Disconnect user
            - login Login user
            - modify_balance Add cash in clients balance
            - transfer_money Transfer money between accounts
            - bank_statement Show's client transactions
            - exit To exist the application
        ''')
    elif user_command == LOGIN_COMMAND:
        IS_USER_LOGED_IN = must_login(IS_USER_LOGED_IN)
    if not IS_USER_LOGED_IN:
        print("You are not logged in, please use -login command to do so!")
        continue
    elif user_command == LOGOUT_COMMAND:
        IS_USER_LOGED_IN = logout(IS_USER_LOGED_IN)

    if user_command == ADD_CLIENT_COMMAND:
        start_create_client_procedure()
    elif user_command == READ_CLIENT_BALANCE:
        client_id = retrieve_client_id()
        if client_id:
            read_account_balance(client_id)
        else:
            print('User does not exist in the system.')
    elif user_command == MODIFY_BALANCE:
        client_id = retrieve_client_id()
        new_account_balance = float(input("Specify new balance: "))
        update_balance(client_id=client_id, ammount=new_account_balance, fully_update=True)

    elif user_command == TRANSFER_MONEY:
        transfer_money()

    elif user_command == BANK_STATEMENT:
        client_info = retrieve_client_information()
        if not client_info:
            print("No client found!")
            continue
        client_account_balance, client_account_currency = read_account_balance(client_id=client_info['client_id'])
        statement_file = open(f"Extras-{client_info['client_name']}.txt", 'w')
        statement_file.write(f'''
                        Banca Titulescu

        Name: {client_info['client_name']}
        City: {client_info['client_city']}
        Phone: {client_info['client_phone']}

        Account: {client_account_balance} {client_account_currency}

        Transfer History:

''')
        statement_file.close()

        file = open('money_transfer_history.txt', 'r')
        file_lines = file.readlines()
        client_id = client_info['client_id']

        statement_file = open(f"Extras-{client_info['client_name']}.txt", 'a')
        for transfer_line in file_lines:
            transfer_data = transfer_line.strip('\n').split(',')
            sender_id = transfer_data[0]
            receiver_id = transfer_data[1]
            sender_amount = transfer_data[2]
            sender_currency = transfer_data[3]
            receiver_amount = transfer_data[4]
            receiver_currency = transfer_data[5]
            time_transfer = transfer_data[6]

            if sender_id == client_id:
                history_line = f'Money sent {sender_amount} {sender_currency} {time_transfer}\n'
                statement_file.write(history_line)
            elif receiver_id == client_id:
                history_line = f'Money received {receiver_amount} {receiver_currency} {time_transfer}\n'
                statement_file.write(history_line)

        statement_file.close()
        file.close()
