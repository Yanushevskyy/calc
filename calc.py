from prettytable import PrettyTable

def user_name_input():
    while True:
        user_name = input("Please type your name: ")
        if validate_string(user_name):
            return user_name.capitalize()
        else:
            continue
 
def validate_string(string):
    if string.strip() == "":
        print("😢 I'm just waiting for your name...😢")
        return False
    elif any(char.isdigit() for char in string):
        print("😾 Please type letters only 😾")
        return False
    else:
        return True
 
def start_calc(user_name):
    print(f"Ok, {user_name}, let's start!")
 
def number_validation(prompt):
    while True:    
        num = input(prompt)
        if num.isdigit():
            return int(num)
        elif num == '':
            print("😢 I'm just waiting for your number 😢")
        else:
            print("😏 Please type digits only 😏")
 
def user_number_input(prompt):
    return number_validation(prompt)
 
def choose_operations():
    print(
        "\nAvailable operations:\n[ + ] for [Addition] \n[ - ] for [Subtraction] \n[ * ] for [Multiplication] \n[ / ] for [Division] \n[ ** ] for [Exponentiation]")
    while True:
        user_operation_input = input("Choose operation: ")
        if operation_validation(user_operation_input):
            return user_operation_input
        else:
            print("⚠️ Choose a correct operation ⚠️")
 
def operation_validation(oper):
    valid_operations = ['+', '-', '*', '/', '**']
    return oper in valid_operations
 
def calculation(first_number, second_number, user_operation):
    if user_operation == "+":
        return first_number + second_number
    elif user_operation == "-":
        return first_number - second_number
    elif user_operation == "*":
        return first_number * second_number
    elif user_operation == "**":
        return first_number ** second_number
    elif user_operation == "/":
        if second_number == 0:
            print("⚠️ Cannot divide by zero ⚠️")
            return None
        return first_number / second_number

 
def calculator():
    requests = []  # Initialize requests list
    results = []   # Initialize results list
 
    user_name = user_name_input()
    start_calc(user_name)
 
    while True:
        user_input = input("Press \"Enter\" to continue or \"q\" to exit: ")
        if user_input.lower() == "":
            first = user_number_input("Please type your first number: ")
            second = user_number_input("Please type your second number: ")
            operation = choose_operations()
            result = calculation(first, second, operation)
            if result is not None:
                requests.append((first, operation, second))  # Store request
                results.append(result)                       # Store result
                table = {requests[i]: results[i] for i in range(len(requests))}
                print(table)
                final_table = PrettyTable()
                final_table.field_names = ["Request", "Result"]
                for request, result in zip(requests, results):
                    final_table.add_row([request,result])
                print(final_table)
        elif user_input.lower() == "q":
            print("Exiting....")
            break
        else:
            print("What actually do you want to do?")
 
calculator()