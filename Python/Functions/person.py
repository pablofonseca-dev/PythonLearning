
def generate_person(first_name, middle_name='', last_name='', first_tel_number=0):
    """
    Return a dictionary of information about a person. 
    """
    generated_person = {}
    generated_person['first_name'] = first_name
    if middle_name:
        generated_person['middle_name'] = middle_name
    if last_name:
        generated_person['last_name'] = last_name
    if first_tel_number != 0:
        generated_person['first_tel_number'] = first_tel_number
    return generated_person

musician = generate_person("Pablo", last_name="Fonseca", first_tel_number=87620495);

print(musician);