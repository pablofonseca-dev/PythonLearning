print("Escribe un correo electrónico", end="\n");
email = input();

before = '';
for letter in email:
    if(letter == '@'):
        break;
    before += letter
print(before);