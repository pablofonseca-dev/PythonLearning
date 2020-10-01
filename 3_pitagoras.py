"""
    Calcula la hipotenusa de un triángulo rectángulo.
"""
catetoA = float(input("Ingrese el Cateto A del Triángulo\n"));
catetoB = float(input("Ingrese el Cateto B del Triángulo\n"));

longitudHipotenusa = ((catetoA ** 2) + (catetoB ** 2)) ** 0.5;

#print("La longitud de la hipotenusa es de:", longitudHipotenusa, sep=" ", end="\n");

#o

print("La longitud de la hipotenusa es: " + str(longitudHipotenusa), end="\n");

#str para convertir a string.
#int para convertir a integers.
#float para convertir a punto flotante.


