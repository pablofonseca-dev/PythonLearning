#Se puede usar un While loop para recorrer y eliminar TODAS las instancias de una lista que estan repetidas
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']

while('cat' in pets):
    pets.remove('cat')

while('dog' in pets):
    pets.remove('dog')
print(pets)

