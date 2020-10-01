print("Escribe un número", end="\n");
number = input();
formattedNumber = '';
for i in number:
    if(i == '0'):
        formattedNumber += 'x';
        continue;
    formattedNumber += i;
print(formattedNumber);