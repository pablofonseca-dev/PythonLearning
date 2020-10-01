numeroSecreto = 777

print(
"""
+==================================+
| Bienvenido a mi juego, muggle!   |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

numeroUsuario = int(input());

while(numeroUsuario != numeroSecreto):
    print("¡Ja, ja! ¡Estás atrapado en mi ciclo!");
    print("¿Cuál es el número secreto?");
    numeroUsuario = int(input());
print("¡Bien hecho, muggle! Eres libre ahora");
