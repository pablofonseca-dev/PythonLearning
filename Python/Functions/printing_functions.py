def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing. 
    """
    #unprinted_designs_copy = unprinted_designs[:] this was my solution, but there is one better
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing {current_design.title()}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """
    Show all the models that were printed.
    """
    print("\nThe following models have been printed.")
    counter = 0
    for current_model in completed_models:
        print(f"{counter + 1}-{current_model.title()}")
        counter += 1