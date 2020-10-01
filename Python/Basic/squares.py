list_of_nums = [];

for i in range(1, 10 + 1):
	list_of_nums.insert(i - 1, i ** 2);

print(list_of_nums);

#List comprenhension 
squares = [value ** 2 for value in range(1, 10 + 1)]

print(squares);
