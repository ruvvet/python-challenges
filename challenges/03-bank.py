print("Welcome to Chase bank.")
print("Have a nice day!")


def deposit(bal):
    amt = int(input('amt to deposit: $'))
    return f'Your current balance: ${bal+amt}'


def withdraw(bal):
    amt = int(input('amt to withdraw: $'))
    return f'Your current balance: ${bal-amt}'


def bank():
    balance = 4000
    action = input('Display Balance, Withdraw, Deposit?: (B/W/D)').upper()
    if action == 'B':
        return f'Your current balance: ${balance}'
    elif action == 'W':
        return withdraw(balance)
    elif action == 'D':
        return deposit(balance)


print(bank())
