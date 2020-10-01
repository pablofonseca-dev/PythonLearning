ingresoCiudadano = float(input("Ingrese el ingreso anual: "));
impuesto = None;
if(ingresoCiudadano <= 85528.):
    impuesto = ((((ingresoCiudadano * 18) / 100) - 556) - 0.02);

else:
    impuesto = 14.839 + 0.02 + (((ingresoCiudadano - 85528) * 32) / 100);

if(impuesto < 0):
    impuesto = 0.0;
impuesto = round(impuesto, 0);

print("El impuesto es: ", impuesto, "pesos")
