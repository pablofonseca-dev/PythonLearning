#Para inicializar un arreglo o stack
healthy = ['kale chips', 'pizza', "Frozen Custard"]

backpack = ['pizza', 'frozen custard', 'apple crisp', 'kale chips']
#Para agregar un elemento al stack se utiliza el método append()
healthy.append("Apple Crips")

#Para saber la longitud de un stack LIFO se utiliza la función len()
length = len(healthy)

#Para saber si un elemento esta dentro del Stack
healthyFound = ("Frozen Custard" in healthy)

print(healthy)
print('La lista tiene', length, 'elementos')


#Imprime cada mensaje dependiendo de si se encontró la lista o no.
if(healthyFound):
    print('La pizza se encuentra en el Stack')
else:
    print('La pizza no fue encontrada :(')

#Para eliminar un elemento del stack
backpack.remove('pizza')

if "kale chips" not in healthy:
    backpack.remove('kale chips');


print(backpack);




