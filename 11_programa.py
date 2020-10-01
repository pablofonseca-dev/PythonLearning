eggs = 4;

for eggs in range(2, 20):
    print("Valor de eggs " + str(eggs), end="\n");
else:
    print("El valor de eggs global es de " + str(eggs));

foo = 45;

for foo in range(20, 2):
    print("Valor de foo es " + str(foo), end="\n");
else:
    print("Como nunca se ejecuto el ciclo, el valor de foo es de " + str(foo), end="\n");