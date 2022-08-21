from Clients import retrieve_client_id
import datetime

def get_all_account():
    accounts_file = open('accounts.txt', 'r')
    all_accounts = accounts_file.readlines()
    accounts_file.close()
    return all_accounts


def read_account_balance(client_id):
    all_acounts = get_all_account()
    for account in all_acounts:
        account = account.strip('\n')
        account_data = account.split(',')
        if client_id == account_data[0]:
            print(f'Your account has {account_data[1]}{account_data[2]}')
            return float(account_data[1]), account_data[2]


def update_balance(client_id, ammount, fully_update=False):
    accounts = get_all_account()
    for index, account in enumerate(accounts):
        account_data = account.split(',')
        if client_id == account_data[0]:
            if fully_update:
                new_account_balance = ammount
            else:
                new_account_balance = float(account_data[1]) + ammount
            accounts[index] = f'{account_data[0]},{new_account_balance},{account_data[2]}'
    file = open('accounts.txt', 'w')
    file.writelines(accounts)
    file.close()


def transfer_money():
    sender_client_id = retrieve_client_id()
    sender_account_balance, sender_account_currency = read_account_balance(sender_client_id)
    receiver_client_id = retrieve_client_id()
    receiver_account_balance, receiver_account_currency = read_account_balance(receiver_client_id)
    transfer_amount = float(input('Please enter the amount you want to send: '))
    if transfer_amount > sender_account_balance:
        print("Not enough money!")
    elif transfer_amount <= 0:
        print("You can not transfer negative or zero amounts")
    elif not receiver_client_id or not sender_client_id:
        print('Nonexistent beneficiary/sender, we cannot transfer money!')
    else:
        transfer_date =  datetime.datetime.now()
        transfer_date_made = transfer_date.strftime("%Y-%B-%d %H:%M")
        update_balance(sender_client_id, -transfer_amount)
        update_balance(receiver_client_id, transfer_amount)
        file = open('money_transfer_history.txt', 'a')
        file.write(
            f'{sender_client_id},{receiver_client_id},{-transfer_amount},{sender_account_currency},{transfer_amount},{receiver_account_currency},{transfer_date_made}\n')
        file.close()