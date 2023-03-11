# Defininiendo variables
variable1 = 6
variable2 = 7
variable3 = 3

vari_division1 = 15
vari_division2 = 5

#Enteros (int)
#multiplicacion de numeros enteros
multiplicacion = variable1 * variable2 * variable3
#Divison  con numeros enteros
division_entera = int(vari_division1 // vari_division2) 
resultado_suma = multiplicacion + division_entera
print("El resultado de la multiplicación es:", multiplicacion)
print("El resultado de la división entera es:", division_entera)
print("El resultado de la suma es:", resultado_suma)

# Definir variables de tipo flotante (Float)
vari_exponecial1 = 3
vari_exponecial2 = 7

vari_modul1 = 5
vari_modul2 = 9

exponencial = vari_exponecial1 ** vari_exponecial2
#Operando modulo
modulo = vari_modul1 % vari_modul2
resultado_flotante = exponencial - modulo
division = resultado_suma / resultado_flotante
print("El resultado del exponencial es:", exponencial)
print("El resultado del módulo es:", modulo)
print("El resultado de la resta es:", resultado_flotante)
print("El resultado de la división es:", division)

# Definir variables de tipo complejo (Complex)
complejo1 = 2 + 4j
complejo2 = 5 + 7j
complejo3 = 10 + 5j
complejo4 = 1 + 3j

# Definir variables de tipo carácter (String)
fruta1 = "Pera"
fruta2 = "Mandarina"
fruta3 = "Uva"
fruta4 = "Fresa"
fruta5 = "Naranja"
fruta6 = "Kiwi"

# Definir variable de tipo booleano (Bool)
nombre_fruta = input("Ingrese el nombre de una fruta: ")
if nombre_fruta == fruta1:
    print(fruta1 + " es la fruta favorita de Abigail.")
elif nombre_fruta == fruta2:
    print(fruta2 + " es la fruta favorita de Luis.")
elif nombre_fruta == fruta3:
    print(fruta3 + " es la fruta favorita de Wendy.")
elif nombre_fruta == fruta4:
    print(fruta4 + " es la fruta favorita de Alexander.")
elif nombre_fruta == fruta5:
    print(fruta5 + " es la fruta favorita de Eduardo.")
elif nombre_fruta == fruta6:
    print(fruta6 + " es la fruta favorita de Rodrigo.")

    
# Mensaje de finalización del programa
print("Hemos finalizado la tarea de fundamentos de programación.")
