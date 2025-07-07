"""
Hecho por: [Tu Nombre]
Este programa genera una contraseña segura basada en una o varias palabras clave.
Combina las palabras clave con caracteres aleatorios para fortalecer la seguridad.
"""

import random
import string

def generar_contraseña(palabras_clave, longitud=12):
    # Unir palabras clave en una sola cadena
    base = ''.join(palabras_clave)

    # Caracteres que se pueden añadir
    caracteres_extra = string.ascii_letters + string.digits + string.punctuation

    # Si la base es menor que la longitud deseada, rellenar con caracteres aleatorios
    while len(base) < longitud:
        base += random.choice(caracteres_extra)

    # Mezclar caracteres para mayor seguridad
    base_lista = list(base)
    random.shuffle(base_lista)

    # Cortar a la longitud deseada
    contraseña = ''.join(base_lista[:longitud])
    return contraseña

def main():
    print("----- Generador de Contraseñas Seguras -----")
    entrada = input("Ingresa una o varias palabras clave separadas por espacio: ")
    palabras = entrada.strip().split()

    try:
        longitud = int(input("Longitud de la contraseña (mínimo 12): "))
    except ValueError:
        print("Valor inválido, se usará longitud por defecto: 12")
        longitud = 12

    if longitud < 12:
        print("Longitud mínima es 12, se ajustará automáticamente.")
        longitud = 12

    contraseña = generar_contraseña(palabras, longitud)
    print(f"\nTu contraseña sugerida es: {contraseña}")

if __name__ == "__main__":
    main()
