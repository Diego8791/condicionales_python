#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1
 
Descripcion:
Programa creado para que practiquen los conocimietos adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

def ej1():
    # Ejercicios de práctica con números

    '''
    Realice un programa que solicite por consola 2 números
    Calcule la diferencia entre ellos e informe por pantalla
    si el resultado es positivo, negativo o cero.
    '''
    numero_1 = float(input("Ingrese el primer número: "))
    numero_2 = float(input("Ingrese el segundo número: "))

    resta = numero_1 - numero_2

    if resta > 0:
      print("El resultado es positivo")
    elif resta < 0:
      print("El resultado es negativo")
    else:
      print("El resultado es 0")

def ej2():
# Ejercicios de práctica con números

    '''
    Realice un programa que solicite el ingreso de tres números
    enteros, y luego en cada caso informe si el número es par
    o impar.
    Para cada caso imprimir el resultado en pantalla.
    '''
    numero_1 = int(input("Ingrese el primer número entero: "))
    numero_2 = int(input("Ingrese el segundo número entero: "))
    numero_3 = int(input("Ingrese el tercer número entero: "))

    if (numero_1 % 2) == 0:
        print(f"{numero_1} es par")
    else:
        print(f"{numero_1} es impar")

    if (numero_2 % 2) == 0:
        print(f"{numero_2} es par")
    else:
        print(f"{numero_2} es impar")
    
    if (numero_3 % 2) == 0:
        print(f"{numero_3} es par")
    else:
        print(f"{numero_3} es impar")

def ej3():
    # Ejercicios de práctica con números

    '''
    Realice una calculadora, se ingresará por línea de comando dos números
    Luego se ingresará como tercera entrada al programa el símbolo de la operación
    que se desea ejecutar
    - Suma (+)
    - Resta (-)
    - Multiplicación (*)
    - División (/)
    - Exponente/Potencia (**)

    Se debe efectuar el cálculo correcto según la operación ingresada por consola
    Imprimir en pantalla la operación realizada y el resultado
    
    '''
    numero_1 = float(input("Ingrese el primer número: "))
    numero_2 = float(input("Ingrese el segundo número: "))
    print(" - Suma (+)")
    print(" - Resta (-)")
    print(" - Multiplicación (*)")
    print(" - División (/)")
    print("- Exponente/Potencia (**)")
    simbolo = input("Ingrese la operación a realizar: ")

    if simbolo == '+':
        print(f"La suma de {numero_1} y {numero_2} es {numero_1 + numero_2}")
    elif simbolo == '-':
        print(f"La resta de {numero_1} y {numero_2} es {numero_1 - numero_2}")
    elif simbolo == '*':
        print(f"La multiplicación de {numero_1} y {numero_2} es {numero_1 * numero_2}")
    elif simbolo == '/':
        print(f"La división de {numero_1} y {numero_2} es {numero_1 / numero_2}")
    elif simbolo == '**':
        print(f"La potencia de base {numero_1} y exponente {numero_2} es {numero_1 ** numero_2}")
    else:
        print("Esta calculadora no realiza la operación pedida. ¡Lo siento!")

def ej4():
    # Ejercicios de práctica con cadenas
    
    '''
    Realice un programa que solicite por consola 3 palabras cualesquiera
    Luego el programa debe consultar al usuario como quiere ordenar las palabras
    1 - Ordenar por orden alfabético (usando el operador ">")
    2 - Ordenar por cantidad de letras (longitud de la palabra)

    Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
    e imprimir en pantalla de la mayor a la menor

    Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
    e imprimir en pantalla de la mayor a la menor

    '''
    palabra_1 = input("Ingrese la primer palabra: ")
    palabra_2 = input("Ingrese la segunda palabra: ")
    palabra_3 = input("Ingrese la tercer palabra: ")
    orden_palabras = " "    # inicio variable para ordenamiento
    opcion = 0
    
    # Comparo las palabras introducidas para saber que operaciones de
    # ordenamiento se puden realizar. Si hay al menos dos palabras repetidas 
    # no se podrá hacer ordenamiento alguno, y si hay palabras diferentes 
    # pero con igual cantidad de letras no se podrá hacer ordenamiento por
    # cantidad de letras.
    if (palabra_1 == palabra_2) or (palabra_1 == palabra_3) or (palabra_2 == palabra_3):
        print("¡ATENCIÓN!... Ha introducido palabras iguales")
        print("No puede hacerse ordenamiento. El programa ha terminado")
    else:
        if (len(palabra_1) == len(palabra_2)) or (len(palabra_1) == len(palabra_3)) or (len(palabra_2) == len(palabra_3)):
            print("¡ATENCIÓN!...palabras con igual cantidad de letras")
            print("solo se podrá hacer ordenamiento alfabético")
            opcion = 1
        else:
            print("-" * 50)
            print("Ingrese 1 para orden alfabético")
            print("Ingrese 2 para ordenar por cantidad de letras")
            print("-" * 50)
            opcion = int(input("Ingrese su opción: "))
    # Ejecución de ordenamiento por órden alfabético de mayor a menor
    if opcion == 1:
        if (palabra_1 > palabra_2) and (palabra_1 > palabra_3):
            orden_palabras += palabra_1 + " "
            if palabra_2 > palabra_3:
                orden_palabras += palabra_2 + " "
                orden_palabras += palabra_3
            else:
                orden_palabras += palabra_3 + " "
                orden_palabras += palabra_2
        if (palabra_2 > palabra_1) and (palabra_2 > palabra_3):
            orden_palabras += palabra_2 + " "
            if palabra_1 > palabra_3:
                orden_palabras += palabra_1 + " "
                orden_palabras += palabra_3
            else:
                orden_palabras += palabra_3 + " "
                orden_palabras += palabra_1
        if (palabra_3 > palabra_1) and (palabra_3 > palabra_2):
            orden_palabras += palabra_3 + " "
            if palabra_1 > palabra_2:
                orden_palabras += palabra_1 + " "
                orden_palabras += palabra_2
            else:
                orden_palabras += palabra_2 + " "
                orden_palabras += palabra_1
    
    # Ejecución de ordenamiento de mayor a menor por cantidad de letras.
    if opcion == 2:
        if (len(palabra_1) > len(palabra_2)) and (len(palabra_1) > len(palabra_3)):
            orden_palabras += palabra_1 + " "
            if len(palabra_2) > len(palabra_3):
                orden_palabras += palabra_2 + " "
                orden_palabras += palabra_3
            else:
                orden_palabras += palabra_3 + " "
                orden_palabras += palabra_2
        if (len(palabra_2) > len(palabra_1)) and (len(palabra_2) > len(palabra_3)):
            orden_palabras += palabra_2 + " "
            if len(palabra_1) > len(palabra_3):
                orden_palabras += palabra_1 + " "
                orden_palabras += palabra_3
            else:
                orden_palabras += palabra_3 + " "
                orden_palabras += palabra_1
        if (len(palabra_3) > len(palabra_1)) and (len(palabra_3) > len(palabra_2)):
            orden_palabras += palabra_3 + " "
            if len(palabra_1) > len(palabra_2):
                orden_palabras += palabra_1 + " "
                orden_palabras += palabra_2
            else:
                orden_palabras += palabra_2 + " "
                orden_palabras += palabra_1
    print(orden_palabras)

def ej5():
    # Ejercicios de práctica con números
       
    '''
    Realice un programa que solicite ingresar tres valores de temperatura
    De las temperaturas ingresadas por consola determinar:
    1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
    2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
    3 - ¿Cuál es el promedio de las temperaturas ingresadas?

    En cada caso imprimir en pantalla el resultado  

    '''
    temp_1 = int(input("Ingrese el primer valor de temperatura: "))
    temp_2 = int(input("Ingrese el segundo valor de temperatura: "))
    temp_3 = int(input("Ingrese el tercer valor de temperatura: "))

    if (temp_1 == temp_2) or (temp_1 == temp_3) or (temp_2 == temp_3):
        print("¡ATENCION!... Ha introducido valores repetidos")
        print("Programa terminado")
    else:
        if temp_1 > temp_2 and temp_1 > temp_3:
            print(f"{temp_1} es la mayor temperatura ingresada")
        elif temp_2 > temp_1 and temp_2 > temp_3:
            print(f"{temp_2} es la mayor temperatura ingresada")
        else:
            print(f"{temp_3} es la mayor temperatura ingresada")
        
        if temp_1 < temp_2 and temp_1 < temp_3:
            print(f"{temp_1} es la menor temperatura ingresada")
        elif temp_2 < temp_1 and temp_2 < temp_3:
            print(f"{temp_2} es la menor temperatura ingresada")
        else:
            print(f"{temp_3} es la menor temperatura ingresada")

        promedio = (temp_1 + temp_2 + temp_3) / 3
        print("El promedio de temperaturas es",round(promedio, 2))

if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    ej5()
