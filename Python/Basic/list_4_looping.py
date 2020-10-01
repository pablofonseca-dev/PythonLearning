magicians = ['alice', 'david', 'carolina']

for magician in magicians:
	print(magician.title() + ", that was a great trick!")
	print('I cant\' wait to see your next trick, ' + magician.title() + '.\n');
print('Thank you, everyone. That was a great magic show!\n');
	#print('This is going to have an error'); #Unexpected Indent

#Para hacer una lista con la funcion range() se puede hacer así
list_of_numbers = list(range(1, 10 + 1));
print(list_of_numbers)

#Using range() function to make a list

list_of_numbers = [];

for value in range(0, 5 +1):
	print(value);
	list_of_numbers.insert(value, value);

print(list_of_numbers);

#Para hacer una lista de números enteros y pares 
list_of_numbers = list(range(2, 20 +1, 2)); #Va de 2 a 20 inclusivo pero solo agrega números pares. 

print(list_of_numbers);
