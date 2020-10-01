magicians_names = ['Paul', 'Sam', 'William', 'Dereck', 'Sophia', 'Daniela']

def show_magicians(magicians_names):
    """
    Show magicians names
    """
    for current_magician in magicians_names: 
        print(current_magician.title())

def make_great(magicians_names):
    """
    Modifies the list of magicians by adding the phrase: Great to each magician's name. 
    """
    for index in range(0, len(magicians_names)):
        magicians_names[index] = "Great " + magicians_names[index]
    return magicians_names
    
great_magicians = make_great(magicians_names[:])
show_magicians(magicians_names)
show_magicians(great_magicians)