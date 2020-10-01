#Por  buena práctica es recomendable iniciar el diccionario vacío
my_alien = {}

my_alien['name'] = 'Pachaco';
my_alien['color'] = '#00FF00';
my_alien['x_coordinate'] = 0;
my_alien['y_coordinate'] = 25;
my_alien['is_alive'] = True;
my_alien['speed'] = 'medium';

#Para modificar las propiedades de un diccionario
print(my_alien['name'] + 's' + ' color is ' + my_alien['color']);

my_alien['color'] = '#FF0000';

print(my_alien['name'] + 's' + ' color is now ' + my_alien['color']);

x_coordinate_increment = 0;
    #Very slow alien
if(my_alien['speed'] == 'slow'):
    x_coordinate_increment = 1
elif(my_alien['speed'] == 'medium'):
    x_coordinate_increment = 2
else:
    #Very fast alien!
    x_coordinate_increment = 3

my_alien['x_coordinate'] = my_alien['x_coordinate'] + x_coordinate_increment;

#Para eliminar una propiedad del diccionario

person = {}

person['name'] = 'Pablo'
person['lastname'] = 'Fonseca'
person['age'] = 19

print(person)

#Aquí se elimina el nombre
del person['name']

print(person)

#Para imprimir una lista de valores key/value
print(person.items())

#Para recorrer un diccionario
for key, value in person.items():
    print('\nKey: ' + key  + ' ' + 'Value: ' + str(value))

#Otro ejemeplo
favorite_languages = {
    'jen': 'python', 
    'sarah': 'c',  
    'edward': 'ruby', 
    'phil': 'python', 
}

for name, language in favorite_languages.items():
    print('\n' + name.title() + '\'s favorite language is ' + language.title() + '.')

#Para imprimir solo las llaves de un diccionario
#NOTA: Como es el comportamiento por defecto, no hace falta agregar el metodo keys()
#Sin embargo, hace el codigo más entendible . 
for name in favorite_languages.keys():
    print("\n" + name.title() + ' made the poll')

#Un ejemplo un poco más complejo
friends = ['edward', 'sarah']

for name in favorite_languages:
    print(name.title())
    if name in friends:
        print('Hi ' + name.title() + ', I see your favorite language is ' + favorite_languages[name].title() + '!')

#Para averiguar si no hay una llave en un diccionario
if 'alex' not in favorite_languages.keys():
    print('Alex is not in the list!')

#Para recorrer un diccionario en orden se utiliza ordenamiento temporal 
for name in sorted(favorite_languages.keys()):
    print(name.title() + ', thank you for taking the poll.')

#Para recorrer los valores de las llaves de un diccionario
print('The following languages have been mentioned: ')
counter = 0
for language in favorite_languages.values(): 
    counter += 1
    print(str(counter) + '-\t' + language)
"""
Para recorrer los lenguajes de programacion o otro tipo de llave o valor, nos daremos cuenta que muchas veces
lo que imprimimos se repite innecesariamente, por ejemplo, si listamos dos veces el nombre de un lenguaje de 
programación este aparecerá dos veces.
"""
#La solucion a ello es convertir la lista en un Set

unique_fav_languages = set(favorite_languages.values())
print('The following languages have been mentioned but they are in a Set structure: ')
counter = 0
for language in unique_fav_languages: 
    counter += 1
    print(str(counter) + '-\t' + language)