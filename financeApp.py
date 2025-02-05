import re
expenses = {}
budgets = {}
user = {}

def show_menu():
    print("\n Welcome to my Expenses Tracker Application")
    print("\tTrack your Money like never before\t")
    print("1. Create an account")
    print("2. View your account")
    print("3. Manage Expense")
    print("4. Manage Budget")
    print("5. Exist")



def create_acc():
    full_name = input("Enter your Full Name: ")

    while True:
        password = input("Enter your Password: ")

        if is_valid_password(password):
            break


    while True:
        email = input("Enter your Email: ")

        if is_valid_email(email):
            if email in user:
                print("❌ This email is already registered. Please use a different email.")
            else:
                break
        else:
            print("❌ Invalid Email. Please try again.")


    user[email] = {"Full Name": full_name, "Password": password}  # Store user data
    print("✅ Account successfully created!")

def is_valid_password(password):
    if (len(password) >= 6 and
        any(char.isupper() for char in password) and
        any(char.islower() for char in password) and
        any(char.isdigit() for char in password) and
        re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)):
        return True  # ✅ Password meets all conditions

    print("❌ Password must contain: \n - At least 6 characters\n - 1 uppercase letter\n - 1 lowercase letter\n - 1 number\n - 1 special character (@, #, etc.)")
    return False

def is_valid_email(email):
    patterns = r"^[a-zA-Z][a-zA-Z0-9_.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(patterns, email)

def view_acc():
    while True:
        email = input("Enter your Email: ")

        if email not in user:
            print("Email not found! Please try again.")
        else:
            print("\n🔹 Account Details:")
            print(f"Full Name: {user[email]['Full Name']}")
            print(f"Email: {email}")
            print(f"Password: {user[email]['Password']}")
        return

def manage_expense():
    print("Managing expenses")

def manage_budget():
    print("Managing budgets")

def main():


    while True:
        show_menu()
        choice = int(input("Choose an option: "))
        if choice == 1:
            create_acc()

        elif choice == 2:
            view_acc()
        elif choice == 3:
            manage_expense()
        elif choice == 4:
            manage_budget()
        elif choice == 5:
            print("Goodbye")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()