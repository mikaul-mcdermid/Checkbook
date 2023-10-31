import os

# Function to read the balance from the file
def read_balance():
    if os.path.exists('balance.txt'):
        with open('balance.txt', 'r') as f:
            return float(f.readline())
    else:
        return 0

# Function to write the balance to the file
def write_balance(balance):
    with open('balance.txt', 'w') as f:
        f.write(str(balance))

# Function to display the current balance
def view_balance(balance):
    print(f'Your current balance is: ${balance:.2f}')

# Function to handle deposits
def deposit(balance):
    try:
        deposit_amount = float(input('Enter the deposit amount: '))
        if deposit_amount > 0:
            balance += deposit_amount
            print(f'You have deposited ${deposit_amount:.2f}. Your new balance is ${balance:.2f}')
        else:
            print('Invalid input, please enter a valid deposit amount.')
    except ValueError:
        print('Invalid input. Please enter a valid number for the deposit amount.')
    return balance

# Function to handle withdrawals
def withdraw(balance):
    try:
        withdrawal_amount = float(input('Enter the amount you wish to withdraw: '))
        if withdrawal_amount <= balance:
            balance -= withdrawal_amount
            print(f'You have successfully withdrawn ${withdrawal_amount:.2f}. Your new balance is: ${balance:.2f}')
        else:
            # Check if the user wants to proceed with an overdraft
            response = input(f'Warning: Insufficient funds. Your current balance is ${balance:.2f}, and you are trying to withdraw ${withdrawal_amount:.2f}.\nDo you want to proceed with an overdraft? (y/n): ')
            if response.lower() == 'y':
                balance -= withdrawal_amount
                # Deduct an overdraft fee of $25
                balance -= 25
                print(f'You have overdrafted your account with ${withdrawal_amount:.2f}. An overdraft fee of $25 has been applied. Your new balance is: ${balance:.2f}')
            else:
                print('Withdrawal canceled.')
    except ValueError:
        print('Invalid input. Please enter a valid number for the withdrawal amount.')
    return balance


def main():
    balance = read_balance()
    
    while True:
        greeting = input('~~~~~Welcome to Generic Bank Inc! Please select from the following options:~~~~~\n1-View Your Balance\n2-Deposits\n3-Withdrawals\n4-Quit\n')
        
        if greeting in [1, '1', '1.0', 'one', 'view balance', 'balance']:
            view_balance(balance)
        elif greeting in [2, '2', '2.0', 'two', 'deposit', 'deposits']:
            balance = deposit(balance)
        elif greeting in [3, '3', '3.0', 'three', 'withdraw', 'withdrawals']:
            balance = withdraw(balance)
        elif greeting in [4, '4', '4.0', 'four', 'quit', 'exit', 'end']:
            write_balance(balance)
            print('~~~~Thank you for choosing Generic Banking Inc.~~~\n Bring us more money next time... OR ELSE\n Goodbye ^v^')
            break
        else:
            print('Invalid input, please select an option from the menu.')

if __name__ == "__main__":
    main()