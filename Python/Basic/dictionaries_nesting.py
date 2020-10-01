#Para crear diccionarios en una lista
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens_collection = [alien_0, alien_1, alien_2]

for alien in aliens_collection: 
    print(alien)

#Para generar aliens en una lista
aliens = []

for alien in range(30):
    generated_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(generated_alien)

#Una vez agregados se imprimen los primero 5 
for alien in aliens[0 : 5]: 
    print(alien)
print('...')

#Se muestran cuantos aliens han sido generados
print('Total number of aliens: ' + str(len(aliens)))

#Para crear una lista en un diccionario
pizza = {
    'crust': 'thick', 
    'toppins': ['mushrooms', 'extra cheese']
}

#Para imprimir el contenido de esa pizza de arriba
print('You ordered a ' + pizza['crust'] + '-crust pizza ' + 'with the following toppins:')

for topping in pizza['toppins']:
    print('\t' + topping)

#Un ejemplo con dos ciclos un poco mas complejo
favorite_languages = {
    'jen': ['python', 'ruby'], 
    'sarah': ['c'], 
    'edward': ['ruby', 'go'], 
    'phil': ['python', 'haskell'], 
}

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "\'s favorite languages are:")
    for language in languages: 
        print("\t" + language.title())

#Para mezclar diccionarios dentro de un diccionario
#Se puede hacer, pero no es recomendable porque el codigo se puede complicar muy rapido y mucho
users = {
    'aeinstein': {
        'first': 'albert', 
        'last': 'einstein', 
        'location': 'princeton'
    },
    'mcurie': {
        'first': 'marie', 
        'last': 'curie', 
        'location': 'paris'
    },
}

#Para imprimir los datos de una manera ordenada
for username, user_info in users.items():
    print('\nUsername: ' + username)
    full_name = user_info['first'].title() + ' ' + user_info['last'].title()
    location = user_info['location']

    print('\nFull Name: ' + full_name);
    print('\nLocation ' + location.title())