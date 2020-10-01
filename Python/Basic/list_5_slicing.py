players = ['charles', 'martina', 'michael', 'florence', 'eli']

#Para partir la lista del 0 a el elemento de indice 2 inclusivo
print(players[0: 2])

print(players[1: 4])

#Si se omite el primer indice la lista comenzaria en 0 

print(players[ : 3]) #Va de 0 a 3 inclusivo

#Si se omite el segundo indice de la lista recorrería desde el primer indice dado inclusivo hasta el último indice de la lista inclusivo
print(players[ 2: ]) 

#Para partir una lista desde un último elemento de ella se puede hacer así
print(players[ -4 : ]) #En este caso obtendria el elemento #4 que es martina desde el final contando en 1 hasta eli que es el último elemento inclusivo

#Para recorrer solo una parte de una lista con un ciclo
#Algo asi puede utilizarse para encontrar los mejores jugadores en un videojuego 
for value in players[: 3]: #Recorra la lista de 0 al valor 3
	print(value)
	

#Para copiar una lista sin apuntar a una dirección de memoria igual se puede utilizar esta forma
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are: \n")
print(my_foods)

print("My friend's favorite foods are:\n")
print(friend_foods)


#Para producir una lista que apunte a la misma dirección de memoria de otra se hace esta manera
my_subjects = ['Proyecto de Software II', 'Ingles III']

roger_subjects = my_subjects

roger_subjects.append('Estructuras de Datos I')
roger_subjects.append('Pogramación de Base de Datos')

print(roger_subjects)

#Cuando imprimo mi lista tambien tendra esas materias

print(my_subjects)
