"""
The asterisk parameter name *toppings tells python to make an empty tuple called toppings
Optional parameters always are at the end of the parameters. 
"""
def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) + '-inch pizza with the following toppings:')
    print(toppings)
    for topping in toppings: 
        print("- " + str(topping))

#make_pizza(12, ['pepperoni'], ['mushrooms', 'green peppers', 'extra cheese'])