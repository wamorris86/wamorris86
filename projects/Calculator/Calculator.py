import os

# Clears screen after each operation, keeps it clean
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Saves calculaion history to file called history.txt
def save_history(record, filename="history.txt"):
    with open(filename, "a") as f:
        f.write(record + "\n")

# Loads history for user to view
def load_history(filename="history.txt"):
    try:
        with open(filename, "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

# Clears history at the command of the user
def clear_history(filename="history.txt"):
    open(filename, "w").close()
    print("\n ---- History Cleared! ---- \n")

# --- Main Calculator --- 

def do_calculation(history):
    # Performs the calculation
    while True:
        try:
            num1 = float(input("First value here: "))       # Takes first value as input
            print("\nChoose an operation\n")
            print("1. Add (+)")
            print("2. Subtract (-)")
            print("3. Multiply (*)")
            print("4. Divide (/)")
            operation = input("Operation here (1-4 or +, -, *, /): ")       # Takes operation as input
            num2 = float(input("Second value here: "))          # Takes second value as input
        except ValueError:
            print("Invalid input")
            continue

        if operation == '1' or operation == '+':
            result = num1 + num2
            op_symbol = '+'
        elif operation == '2' or operation == '-':
            result = num1 - num2
            op_symbol = '-'
        elif operation == "3" or operation == '*':
            result = num1 * num2
            op_symbol = '*'
        elif operation == '4' or operation == '/':
            if num2 == 0:
                print("Cannot divide by zero\n")
                continue
            result = num1 / num2
            op_symbol = '/'
        else:
            print("Invalid operation\n")
            continue

        record = (f"{num1} {op_symbol} {num2} = {result}")
        print(record)

        history.append(record)
        save_history(record)

        again = input("Would you like to calculate more? (y/n): ")
        if again.lower() != 'y':
            break

    

def calcmenu(history):
# Calculator main menu
    while True:
        clear_screen()
        print(" ---- Calc (slang for calculator) ----\n")
        print("1. Use the calculator")
        print("2. View calculator history")
        print("3. Clear calculator history")
        print("4. Exit\n")

        MenuChoice = input("Choice: ")
        # Use the calculator
        if MenuChoice == '1':
            clear_screen()
            do_calculation(history)
        # View calculator history (after making sure history isnt blank)
        elif MenuChoice == '2':
            clear_screen()
            if len(history) == 0:
                print("No history yet\n")
            else:
                print(" ---- Calculator History ---- \n")
                for calc in history:
                    print(calc)
                print()
            input("Press enter to return to the main menu")
        # Clear history
        elif MenuChoice == '3':
            clear_screen()
            clear_history()
            history.clear()
            input("Press enter to return to main menu")
        # Exit the calculator
        elif MenuChoice == '4':
            print("Thanks for using this Calc (slang for calculator)! Goodbye!")
            break

        else:
            print("Invalid operation.")
            input("Press enter to try again")

history = load_history()
calcmenu(history)