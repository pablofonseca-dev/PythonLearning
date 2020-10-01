print("Ingrese el primer número", end=":\n>>>");
numeroA = int(input());

print("Ingrese el segundo número", end=":\n>>>");
numeroB = int(input());

mayor = None;
if numeroA > numeroB:
    mayor = numeroA;
else:
    mayor = numeroB;

print("El mayor de los dos números es " + str(int(mayor)));



