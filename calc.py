results = []
def user_name_input():
    while True:
        name_msg = "Please type your name: "
        user_name = input(name_msg)
        contains_digits = any(char.isdigit() for char in user_name)
        if user_name == "":
            print("😢 I'm just waiting for your name...😢")
        elif contains_digits:
            print("😾 Please type letters only 😾")
        else:
            capitalized_user_name = user_name.capitalize()
            user_name = capitalized_user_name
            break
    return user_name

def start_calc():
    print(f"Ok, {user_name_input()}, let's start!")


def user_validation(num):
    while True:    
        if num == "":
            print("😢 I'm just waiting for your number 😢")
        elif num.isdigit():
            print(f"👌 Ok, let's try with {num} and...")
            num = int(num)
            return num
        else:
            print("😏 Please type digits only 😏")
           

def user_first_number_input():
        user_first_number = input("Please type your first number: ")
        validated_first = user_validation(user_first_number)
        return validated_first
        
def user_second_number_input():
        user_second_number = input("Please type your second number: ")
        validated_second = user_validation(user_second_number)
        return validated_second      

def choose_operations():
    print("\nAvailable operations: ")
    print("\n[ + ] for [Addition] \n[ - ] for [Subtraction] \n[ * ] for [Multiplication] \n[ / ] for [Division]\n")
    user_operation_input = input("Choose operation:")
    return user_operation_input

def calculation():
    user_operation = choose_operations()
    calc_first_number = user_first_number_input()
    calc_second_number = user_second_number_input()
    while True:
        
        if user_operation =="+":
            
            add = calc_first_number + calc_second_number
            print(f"{calc_first_number} {user_operation} {calc_second_number} = [{add}]")
            return add
        elif user_operation =="-":
            
            sub = calc_first_number - calc_second_number
            print(f"{calc_first_number} {user_operation} {calc_second_number} = [{sub}]")
            return sub
        elif user_operation =="*":
           
            mul = calc_first_number * calc_second_number
            print(f"{calc_first_number} {user_operation} {calc_second_number} = [{mul}]")
            return mul
        elif user_operation =="/":
            
            div = calc_first_number / calc_second_number
            print(f"{calc_first_number} {user_operation} {calc_second_number} = [{div}]")
            return div
        else:
            print("⚠️ Choose correct operation ⚠️")
            break

def calculator():
    while True:
        user_input = input("Press \"Enter\" to continue or \"q\" to exit")
        if user_input == "":
            calculation()
        elif user_input == "q":
            print("Exiting....")
            break
        else:
            print("What actually do you want to do?")

# create a list / dict
        
# comment !!!

start_calc()
calculator()








