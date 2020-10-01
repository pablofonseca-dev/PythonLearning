# name = input('Please enter your name: ')

# print("Hello, " + name + "!")

#Cuando necesitamos crear un prompt más completo para el usuario podemos crearlo en una variable
# y luego pasarlo a la funcion input
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name?\n"
prompt += ">>> "

user_name = input(prompt)

print('Hello, ' + user_name + '!')