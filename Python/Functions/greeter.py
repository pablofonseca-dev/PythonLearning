def formatted_name(first_name, last_name):
    return first_name.title() + ' ' + last_name.title()

def validate_flag(flag, val):
    if(val == flag):
        return True;
    return False; 

def greet_user(): 
    flag = 'q'
    while True: 
        intro_message = "Please tell me your name\n(enter 'q' at any time to quit)"
        print(intro_message)

        first_name = input("First Name\n>>>")

        if(validate_flag(flag, first_name)):
            break;

        last_name = input("Last Name\n>>>")

        if(validate_flag(flag, last_name)):
            break;

        full_name = formatted_name(first_name, last_name);

        print(f"Hello! {full_name}")

greet_user()