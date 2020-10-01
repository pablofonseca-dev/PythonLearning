toppings = [];

def sandwich_maker(size, *toppings):
    '''
    Simulates a Sandwich Maker \n
    Shows the Sandwich Size and Its Ingredient's
    Parameters: 
    -----------
    size : int
        Pizza Size  
        Options : \n\t\t1. Small, \n\t\t2. Medium, \n\t\t3. Normal, \n\t\t4. Big, \n\t\t5. Super Big
    toppings : str 
        Different toppings for the pizza 
    '''
    if(size < 0 or size > 6): 
        print("Invalid Sandwich Size")
        return False; 
    Sizes = {
        1: 'Small', 
        2: 'Medium', 
        3: 'Normal', 
        4: 'Big',  
        5: 'Super Big'
    }

    str_size = Sizes.get(size, "Undefined")
    print(f"Making a {str_size} sandwich!");
    print("\nToppings Asked:");
    
    counter = 0
    for current_topping in toppings:
        print(f"{counter + 1}- {current_topping}")

sandwich_maker(5, 'Jam', 'Cheese', 'Green Pepper')