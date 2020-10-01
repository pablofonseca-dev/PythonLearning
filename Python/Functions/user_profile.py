
"""
ES: ** significa que python debe crear un diccionaro vacío y que cualquier key/value pair que reciba
debe ingresarlo en ese diccionario 
"""
def build_profile(first_name, last_name, **user_additional_info):
    """
    Build a dictionary containing everything we know about a user. 
    """
    profile = {};
    profile['first_name'] = first_name
    profile['last_name'] = last_name
    for key, value in user_additional_info.items():
        profile[key] = value
    return profile

user = build_profile(first_name="Pablo", last_name="Fonseca", location='princeton', field="Computer Science")
print(user)
