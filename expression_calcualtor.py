history_file = "history.txt"

def show_history():
    try:
        with open(history_file, "r") as file:
            files = file.readlines()
        if len(files) == 0:
            print("No history found.")
        else:
            for line in reversed(files):
                print(line.strip())
    except FileNotFoundError:
        print("No history file found yet.")

def clear_history():
    open(history_file, "w").close()
    print("History cleared.")

def save_to_history(expression, result):
    with open(history_file, "a") as file:
        file.write(f"{expression} = {result}\n")
    print("Calculation saved to history.") 

def calculate_expression(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid input format. Please use: <number1> <operator> <number2>")
        return None
    
    try:
        num1 = float(parts[0])
        operator = parts[1]
        num2 = float(parts[2])
    except ValueError:
        print("Invalid numbers.")
        return None

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Division by zero error.")
            return None
        else:
            result = num1 / num2
    else:
        print("Invalid operator. Please use one of: +, -, *, /")
        return None

    # Convert result to int if it's whole number
    if result.is_integer():
        result = int(result)
    
    return result

def main():
    while True:
        user_input = input("Enter calculation (+, -, *, /) (or 'history', 'clear', 'exit'): ")
        if user_input == "exit":
            break
        elif user_input == "history":
            show_history()
        elif user_input == "clear":
            clear_history()
        else:
            result = calculate_expression(user_input)
            if result is not None:
                print("Calculation result:", result)
                save_to_history(user_input, result)

main()
