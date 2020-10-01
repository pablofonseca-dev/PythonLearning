print("Escribe un número positivo diferente de 0");
c0 = int(input());
pasos = 0;
if(c0 < 0 or c0 == 0):
    print("El valor " + str(c0) + " no sigue las normas establecidas", end="\n")
else:
    while(c0 != 1):
        if((c0 % 2) == 0):
            c0 = c0 / 2;
        else:
            c0 = ((3 * c0) + 1)
        print(int(c0), end="\n");
        pasos = pasos + 1;
    print("Pasos: " + str(pasos));