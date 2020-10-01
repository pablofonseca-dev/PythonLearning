
"""
    When you use default values, any parameter with a default value needs to be listed
    after all the parameters that don’t have default values. This allows Python to continue 
    interpreting positional arguments correctly.
"""
def describe_pet(pets_name, animal_type = 'dog'):
    """
    Display information about a pet.
    """
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}\'s name is {pets_name.title()}.")

describe_pet(pets_name="Newton")

