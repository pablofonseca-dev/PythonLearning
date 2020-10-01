
# Para ordenar una lista en orden alfabetico 
cars = ['bmw', 'audi', 'toyota', 'subaru'];

cars.sort();

print(cars);

# Para ordenar una lista al reves EN ORDEN ALFABETICO

cars.sort(reverse=True)

print(cars);

# Para ordenar una lista TEMPORALMENTE
names = ['Ricardo', 'Hanna', 'Amelia', 'John', 'Josh'];

print('\nHere is the original list: ');
print(names);

print('\nHere is the temp sorted list: ');
print(sorted(names));

print('\nHere is the original list again');
print(names);

# NOTA: sorted() también acepta el argumento sorted(reverse=True) para revertir la lista temporalmente. 

#Para ordenar una lista al reves SIN ORDEN ALFABETICO, literalmente dandole vuelta
names.reverse(); 

print('\nHere is the list in reverse order');
print(names);

#Para saber la longitud de una lista 
print(len(names))
