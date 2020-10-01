pizza = {
    'toppings': []
}

prompt = "Enter a pizza toppin:\n(Enter 'quit' to exit)\n>>> "

keyword = "quit"

active = True

while(active):
    pizza_toppin = input(prompt)
    selection = pizza_toppin
    if(not(selection.lower().lstrip() == keyword)):
        pizza['toppings'].append(pizza_toppin.title())
    else:
        active = False

if(len(pizza['toppings']) < 1):
    print("You didn't add a topping to your pizza")
else:
    print("These are your selected toppings:")
    counter = 0
    for topping in pizza['toppings'] :
        print("\t" + str(counter + 1) + "-" + " " + topping)
        counter += 1
    