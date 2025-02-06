import re

expenses = {}
budgets = {}
user = {}
expense_id = 1  # unique id
budget_id = 1  # unique id


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

    print(
        "❌ Password must contain: \n - At least 6 characters\n - 1 uppercase letter\n - 1 lowercase letter\n - 1 number\n - 1 special character (@, #, etc.)")
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
    while True:
        print("\n📊 **Expense Tracker Menu**")
        print("1️⃣ Add Expense")
        print("2️⃣ View Expenses")
        print("3️⃣ Edit Expense")
        print("4️⃣ Delete Expense")
        print("5️⃣ Exit")

        choice = int(input("\nEnter your choice (1-5): "))

        if choice == 1:
            add_expense()
        elif choice == 2:
            view_expenses()
        elif choice == 3:
            edit_expense()
        elif choice == 4:
            delete_expenses()
        elif choice == 5:
            print("\n👋 Exiting... Goodbye!\n")
            break
        else:
            print("❌ Invalid Choice. Please try again.")


# CREATE: Add a new expense
def add_expense():
    global expense_id
    date = input("📆 Enter Date (YYYY-MM-DD): ")
    category = input("📌 Enter Category (e.g., Food, Transport, Bills): ")
    amount = float(input("💰 Enter Amount: "))
    payment_method = input("💳 Enter Payment Method (Cash, Card, etc.): ")
    description = input("📝 Enter Description: ")

    expenses[expense_id] = {
        "date": date,
        "category": category,
        "amount": amount,
        "payment_method": payment_method,
        "description": description
    }
    print(f"\n✅ Expense Added Successfully! (ID: {expense_id})\n")
    expense_id += 1  # Increment ID for next expense


# READ: View all expenses
def view_expenses():
    if not expenses:
        print("\n📭 No expenses recorded yet!\n")
        return

    print("\n📜 Your Expenses:\n")
    for id, expense in expenses.items():
        print(
            f"{id}. 📆 {expense['date']} | 📌 {expense['category']} | 💰 {expense['amount']} | 💳 {expense['payment_method']} | 📝 {expense['description']}")
    print()


# UPDATE: Edit an existing expense
def edit_expense():
    view_expenses()
    exp_id = int(input("\nEnter the Expense ID to Edit: "))

    if exp_id in expenses:
        print("\n📝 Current Expense Details:")
        print(f"1. Date: {expenses[exp_id]['date']}")
        print(f"2. Category: {expenses[exp_id]['category']}")
        print(f"3. Amount: {expenses[exp_id]['amount']}")
        print(f"4. Payment Method: {expenses[exp_id]['payment_method']}")
        print(f"5. Description: {expenses[exp_id]['description']}")

        # Get new values (or keep existing)
        expenses[exp_id]['date'] = input("Enter New Date (YYYY-MM-DD) or Press Enter to Keep: ") or expenses[exp_id][
            'date']
        expenses[exp_id]['category'] = input("Enter New Category or Press Enter to Keep: ") or expenses[exp_id][
            'category']
        new_amount = input("Enter New Amount or Press Enter to Keep: ")
        expenses[exp_id]['amount'] = float(new_amount) if new_amount else expenses[exp_id]['amount']
        expenses[exp_id]['payment_method'] = input("Enter New Payment Method or Press Enter to Keep: ") or \
                                             expenses[exp_id]['payment_method']
        expenses[exp_id]['description'] = input("Enter New Description or Press Enter to Keep: ") or expenses[exp_id][
            'description']

        print("\n✅ Expense Updated Successfully!\n")
    else:
        print("❌ Invalid Expense ID. Try Again.")


# DELETE: Remove an expense
def delete_expenses():
    view_expenses()
    exp_id = int(input("\nEnter the Expense ID to Delete: "))

    if exp_id in expenses:
        print("\n🗑️ Expense to be Deleted:")
        print(f"📆 Date: {expenses[exp_id]['date']}")
        print(f"📌 Category: {expenses[exp_id]['category']}")
        print(f"💰 Amount: {expenses[exp_id]['amount']}")
        print(f"💳 Payment Method: {expenses[exp_id]['payment_method']}")
        print(f"📝 Description: {expenses[exp_id]['description']}")

        confirm = input("\nAre you sure you want to delete this expense? (yes/no): ").lower()
        if confirm == "yes":
            del expenses[exp_id]
            print("\n✅ Expense Deleted Successfully!\n")
        else:
            print("\n❌ Deletion Cancelled.")
    else:
        print("❌ Invalid Expense ID. Try Again.")


def manage_budget():
    while True:
        print("\n📊**Budget Tracker Menu**")
        print("1️⃣ Add Budget")
        print("2️⃣ View Budgets")
        print("3️⃣ Edit Budget")
        print("4️⃣ Delete Budget")
        print("5️⃣ Exit")

        choice = int(input("\nEnter your choice (1-5): "))

        if choice == 1:
            add_budget()
        elif choice == 2:
            view_budget()
        elif choice == 3:
            edit_budget()
        elif choice == 4:
            delete_budget()
        elif choice == 5:
            print("\n👋 Exiting... Goodbye!\n1")
        else:
            print("Invalid choice. Please Try again.")


def add_budget():
    global budget_id
    date = input("📆 Enter Date (YYYY-MM-DD): ")
    category = input("📌 Enter Category (e.g., Food, Transport, Bills): ")
    amount = float(input("💰 Enter Amount: "))
    description = input("📝 Enter Description: ")

    budgets[budget_id] = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }
    print(f"\n✅ Budget Added Successfully! (ID: {budget_id})\n")
    budget_id += 1


def view_budget():

    if not budgets:
        print("\n📭 No expenses recorded yet!\n")
        return

    print("\n📜 Your Expenses:\n")
    for id,  budget in budgets.items():
        print(
            f"{id}. 📆 {budget['date']} | 📌 {budget['category']} | 💰 {budget['amount']}  | 📝 {budget['description']}"
        )
        print()



def edit_budget():
    view_budget()
    bud_id = int(input("Enter the Budget ID: "))

    if bud_id in budgets:
        print("📝\nCurrent Budget Details")
        print(f"1. 📆 Date: {budgets[bud_id]['date']}")
        print(f"2. 📌 Category: {budgets[bud_id]['category']}")
        print(f"3. 💰 Amount: {budgets[bud_id]['amount']}")
        print(f"4. 📝 Description: : {budgets[bud_id]['description']}")

        budgets[bud_id]['date'] = input("Enter New Date (YYYY-MM-DD) or Press Enter to Keep: ") or budgets[bud_id][
            'date']
        budgets[bud_id]['category'] = input("Enter New Date (YYYY-MM-DD) or Press Enter to Keep: ") or budgets[bud_id][
            'category']
        new_amount = input("Enter New Amount or Press Enter to Keep: ")
        budgets[bud_id]['amount'] = float(new_amount) if new_amount else budgets[bud_id]['amount']
        budgets[bud_id]['description'] = input("Enter New Date (YYYY-MM-DD) or Press Enter to Keep: ") or \
                                         budgets[bud_id]['description']

        print("\n✅ Expense Updated Successfully!\n")
    else:
        print("❌ Invalid Expense ID. Try Again.")


def delete_budget():
    view_budget()

    budg_id = int(input("Enter the budget ID to delete budget: "))

    if budg_id in budgets:
        print("🗑️\nBudget to be deleted")
        print(f"1. 📆 Date: {budgets[budg_id]['date']}")
        print(f"2. 📌 Category: {budgets[budg_id]['category']}")
        print(f"3. 💰 Amount: {budgets[budg_id]['amount']}")
        print(f"4. 📝 Description: : {budgets[budg_id]['description']}")

        confirm = input("Are you sure you want to delete this budget (yes/no): ").lower()
        if confirm == "yes":
            print("\n✅ Budget Deleted Successfully!\n")
        else:
            print("\n❌ Deletion Cancelled.")
    else:
        print("❌ Invalid Expense ID. Try Again.")


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
