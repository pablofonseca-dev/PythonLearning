dimensions = (200, 500);

print(dimensions[0]) 
print(dimensions[1])

#Las tuplas son iguales a las listas, la diferencia es que sus elementos no pueden cambiar, son inmutables

#dimensions[0] = 1000; Entonces esto daria error

newDimensions = (dimensions[0], 300);

print(newDimensions);

#Para MODIFICAR una Tupla se hace lo siguiente

names = ('Mario', 'Laura');

print("Original Names")
for value in names: 
	print('\t' + value)
	
#Aqui ocurre la modificacion, en realidad es una re inicializacion de la variable 
names = ('Bernald', 'John');

print("Modified Names")
for value in names: 
	print('\t' + value)
	
	
