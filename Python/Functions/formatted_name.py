"""
Sometimes parameters are not necessary, for example a middle_name here
"""
def get_formatted_name(first_name, last_name, middle_name = ''):
    """Return a full name, neatly formatted."""
    #Empty strings in python means False, Non-Empty Strings in python means True
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.strip().title();
musician = get_formatted_name('john', 'hooker')

print(musician)
