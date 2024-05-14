import textwrap

def menu():
    menu = """\n
    =========Welcome=========
    [1]\tDeposit
    [2]\tWithdraw
    [3]\tShow Statement
    [4]\tNew User
    [5]\tList Accounts
    [6]\tNew Account
    [7]\tQuit
    ==>"""
    return input(textwrap.dedent(menu))

#função para depositar -- deposit function
def deposit_money(balance, extract):
    value = float(input("Enter the amount you want to deposit: "))
    if value > 0:
        balance += value
        print(f"Successful deposit, you now have {balance:.2f} in your account. Thanks for using our bank!")
    else:
        print("Invalid value")
    return balance, extract
# função extrato -- withdraw function
def to_withdraw(balance, statement, limit, number_statement, limit_statement):
    value = float(input("Enter the amount you want to withdraw: "))
    if value > 0 and value <= balance and number_statement < limit_statement:
        balance -= value
        statement += f"Withdraw: \t\tR$ {value:.2f}\n"
        number_statement += 1
        print("\n=== Withdrawal successful! ===")
    else:
        print("\n--- Withdrawal failed, invalid amount or exceeded limit ---")
    return balance, statement
# mostrando saldo -- showing statement
def show_statement(statement):
    print("\n====== Statement ======")
    print(statement if statement else "No transactions made.")
# criando um novo usuário -- creating user
def create_user(users):
    id = input("Enter your ID (numbers only): ")
    if any(user["id"] == id for user in users):
        print("This user already exists")
        return
    name = input("Enter your name: ")
    birthday = input("Enter your birthday (dd-mm-yyyy): ")
    address = input("Enter your address (city - neighborhood - state): ")

    users.append({"name": name, "birthday": birthday, "id": id, "address": address })
    print("User created!")
# filtrando -- filter
def filter_user(id, users):
    return next((user for user in users if user["id"] == id), None)
# criando uma nova conta -- creating a new account
def create_account(agency, id_account, users):
    id = input("Enter the user's ID: ")
    user = filter_user(id, users)
    if user:
        print("\n======== Account created ========")
        return {"agency": agency, "id_account": id_account, "user": user}
    else:
        print("\n=== User not found ===")
# função para mostrar as contas já criadas -- function to show the created accounts
def show_account(accounts):
    for account in accounts:
        line = f"""\
            Agency:\t{account['agency']}
            Account:\t{account['id_account']}
            Holder:\t{account['user']['name']}
            """
        print("=" * 100)
        print(textwrap.dedent(line))
# chamando as funções pelo if else -- calling functions by if else
def main():
    LIMIT_CASH = 3
    AGENCY = "0001"

    balance = 0
    limit = 500
    statement = ""
    number_statement = 0
    limit_statement = 3
    users = []
    accounts = []

    while True:
        option = menu()

        if option == "1":
            balance, statement = deposit_money(balance, statement)

        elif option == "2":
            balance, statement = to_withdraw(balance, statement, limit, number_statement, limit_statement)

        elif option == "3":
            show_statement(statement)

        elif option == "4":
            create_user(users)

        elif option == "5":
            show_account(accounts)

        elif option == "6":
            id_account = len(accounts) + 1
            account = create_account(AGENCY, id_account, users)
            if account:
                accounts.append(account)

        elif option == "7":
            break

        else:
            print("Invalid option. Please select a valid option.")

if __name__ == "__main__":
    main()
