print("Cantidad de bloques de los constructores", end="\n>>>") #5 bloques
cantidadBloques = int(input());

altura = 0;
contador = 0;

#Recorre de 1 a 5
while((cantidadBloques - contador) > 0):
    contador = contador + 1;
    altura = altura + 1;
    cantidadBloques = cantidadBloques - contador;

print("La altura de la pirámide es: " + str(altura), end="\n");

