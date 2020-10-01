anio = int(input("Introduzca un año:"));
if (anio < 1582):
    print('No dentro del período del calendario gregoriano')
elif (anio / 4) != int(anio / 4):
    print('Año común')
elif (anio / 100) != int(anio / 100):
    print('Año bisiesto')
elif (anio / 400) != int(anio / 400):
    print('Año común')
else:
    print('Año bisiesto')

