

#To modify a list you should
list = ['A', 'B', 'D', 'D', 'E'];


list[2] = 'C';

print(list);


#Adding an element to a list of items
fruits = ['Orange', 'Watermelon', 'Apple'];

# ES: Cada uno de los elementos se agregan al final de la pila. 
fruits.append('Mango');
fruits.append(2);
fruits.append(True);

'''
	Es: Para agregar elementos a la izquierda o también conocido como shift, se utiliza el método insert
		aunque en realidad siempre hay que especificar el index de primero, por lo que puede servir para 
		posicionar un elemento en cualquier índice.
'''
fruits.insert(0, 'Pen');

#Removing an item to use the del statement 
# ES: Lo malo de del es que no se puede almacenar el elemento removido de esa lista en una variable. 
del fruits[0] # Pen removed 
del fruits[-1] # True removed
del fruits[-1] # Number 2 removed 

print(fruits);

#Removing an item using the pop method 
#ES: El método POP se utiliza para poder manipular y gestionar el elemento removido de una lista, y poder hacer operaciones con él. 
motorcycles = ["Honda", "Yamaha", "Susuki"]

print(motorcycles);

removed_motorcycle = motorcycles.pop(); #Susuki

print(motorcycles);

print("The removed motorcycle is " + removed_motorcycle);


#Para eliminar un elemento con pop mediante su índice

names = ['Pablo', 'John', 'Josh', 'Delta', 'Omega']

print(names);

removed_item = names.pop(2); #Josh

print(names);

'''
	Es: Para eliminar un elemento sin saber su índice se utiliza el método remove, 
	el método borra la primera ocurrencia de izquierda a derecha, para eliminar otra ocurrencia
	se debería usar un ciclo
'''
bicycle_to_remove = 'Delta';
removed_item = names.remove(bicycle_to_remove); 

print("Se borró " + bicycle_to_remove);

