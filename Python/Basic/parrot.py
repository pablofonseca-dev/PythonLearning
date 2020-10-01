prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program.\n>>> "
message = ""

flag = True
keyword = "Quit"
while flag == True:
    message = input(prompt)
    validate = message
    if validate.lstrip().title() != keyword:
        print(message)
    else:
        flag = False
