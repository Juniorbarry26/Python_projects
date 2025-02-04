import random
accounts = {}

def show_menu():
    print("\n Bank Application")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transfer Money")
    print("5. Check Balance")
    print("6. Exist")

def generate_account_number():
    while True:
        acc_num = int(random.randint(100000, 999999))
        if acc_num not in accounts:
            return acc_num

def create_account():
    full_name = input("Enter your fullname: ")
    pin = input("Set a 4-digit PIN: ")

    if len(pin) != 4 or pin.isdigit():
        print("PIN must be exactly 4-digit")
        return

    initial_deposit = float(input("Please enter your initial deposit: "))

    if initial_deposit < 0:
        print("Deposit must be a positive amount.")
        return
    acc_num = generate_account_number()
    accounts[acc_num] = {"Full Name": full_name, "balance": initial_deposit, "pin": pin}

    print("Account created successfully.")
    print("Here is your account number: ", acc_num)

def deposit():
    acc_num = int(input("Enter your account number: "))

    if acc_num not in accounts:
        print("Account not found.")
        return

    amount = float(input("Enter the amount to deposit: "))

    if amount < 0:
        print("Deposited amount must be greater than zero.")
        return

    accounts[acc_num]["balance"] += amount
    print(f"Deposit successful! New Balance: ${accounts[acc_num]['balance']}")

def withdraw():
    acc_num = int(input("Please enter your account number: "))

    if acc_num not in accounts:
        print("Account not found.")
        return

    pin = input("Please enter your PIN: ")

    if pin != accounts[acc_num]["pin"]:
        print("Incorrect PIN.")
        return

    amount = float(input("Please enter withdrawal amount: "))

    if amount > accounts[acc_num]["balance"]:
        print("Insufficient balance.")
        return

    accounts[acc_num]["balance"] -= amount
    print(f"Withdrawal successful! New Balance: ${accounts[acc_num]['balance']}")


def transfer():
    sender_acc = int(input("Please enter your account number: "))

    if sender_acc not in accounts:
        print("Sender account not found.")
        return

    pin = input("Please enter your PIN: ")

    if pin != accounts[sender_acc]["pin"]:
        print("Invalid PIN:")
        return

    receiver_acc = int(input("Please enter your account number: "))

    if receiver_acc not in accounts:
        print("Sender account not found.")
        return

    pin = input("Enter your PIN: ")

    if pin != accounts[receiver_acc]["pin"]:
        print("Invalid PIN:")
        return

    amount = float(input("Enter recipient account number: "))

    if amount > accounts[sender_acc]["balance"]:
        print("Insufficient balance.")
        return

    accounts[sender_acc]["balance"] -= amount
    accounts[receiver_acc]["balance"] += amount

    print("Amount transferred successfully.")

def check_balance():
    acc_num = int(input("Enter your account number: "))

    if acc_num not in accounts:
        print("Account not found.")
        return

    pin = input("Enter your PIN: ")

    if pin != accounts[acc_num]["pin"]:
        print("Invalid PIN.")
        return

    print(f"Your current balance is: ${accounts[acc_num]['balance']}")

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            create_account()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            transfer()
        elif choice == "5":
            check_balance()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()