#Lab 13 Jafet Hernández Mata

"""
Reto 1 - Determinar la cantidad de dígitos que tiene un número entero positivo distinto de 0.

Entradas: pNum (int)

Salidas: la cantidad de dígitos que tiene pNum. 

Restricciones: pNum = int 
               
               pNum debe ser != de cero
"""

def contarDigitos (pNum):
    if (pNum == 0):
        return "pNum debe ser un  número entero positivo mayor a cero"
    
    if (pNum <= 9):

        return 1 
    
    return 1 + contarDigitos (pNum // 10)

print ("1) La cantidad de dígitos es igual a:", contarDigitos (155))
#print ("\nLa cantidad de dígitos es igual a:", contarDigitos (14558))


"""
Reto 2: Determinar la suma de los dígitos de un número entero positivo

Entradas: num (int)

Salidas: Se obtiene la suma total de los dígitos de la entrada "num".

Restricciones: num debe ser un int
"""

def sumarDigitos (num):
    #Proceso
    if (num <= 9):
        return num
    
    return num % 10 + sumarDigitos (num//10)

#Salida
print ("\n2) Al sumar los dígitos se obtiene:" , sumarDigitos (1036))

"""
Reto 3: Determinar cuántas veces aparece un dígito en un número entero

Entradas: num (int)
          pDigito (int)

Salidas: Devuelve la cantidad de veces que aparece un dígito (pDigito) en el número entero proporcionado en la entrada (num)

Restricciones: num debe ser un int
"""

def numRepetido (num, pDigito):
    #Proceso
    if (num== 0):
        return 0
    
    if (num % 10 == pDigito):
        return 1 + numRepetido (num // 10, pDigito)
    
    return 0 + numRepetido (num // 10, pDigito)

#Salida
print ("\n3) La cantidad total de apariciones es:", numRepetido (1011 , 1))
#print ("La cantidad total es:", numRepetido (4858 , 1))

"""
Reto 4: Determinar la cantidad de vocales (a,e,i,o,u) en una cadena.

Entradas: pCadena (str)

Salidas: Devuelve la cantidad de vocales que aparecen en la cadena de caracteres proporcionada en la entrada "pCadena".

Restricciones: pCadena = str
"""
# Se definió una función auxiliar, que identifica si el elemento de una cadena de carácteres es vocal, devolviendo True de ser el caso y False si no se cumple.

def esVocal(elemento):
    elemento = elemento.upper()
    for letra in elemento:
        if (letra in ["A", "E", "I", "O", "U"]):
            return True
    return False

#print ("El resultado es:", esVocal("e"))
#print ("El resultado es:", esVocal("X"))

# Posteriormente se realizó la función principal para contar la cantidad de vocales que tiene una "pCadena".

def contarVocales (pCadena):
    if (pCadena == ""):
        return 0
    
    if (esVocal(pCadena[0])== True):
        
        return 1 + contarVocales(pCadena[1:])
    
    return contarVocales (pCadena[1:])

print ("\n4) En total hay:", contarVocales("Hola mundo"), "vocales")
#print ("En total hay:", contarVocales(""), "vocales")

"""
Reto 5: Invertir el orden de despliegue de una cadena de caracteres.

Entradas: pCadena (str)

Salidas: Se obtiene de forma invertida la cadena de caracteres proporcionada en la entrada "pCadena" cambiando el orden 
          de los caracteres del último al primero

Restricciones: pCadena = str
"""

def invertirCadena (pCadena):
    #Proceso
    if (pCadena == "" ):
        return ""
    
    return pCadena[-1] + invertirCadena (pCadena[:-1])

print ("\n5) Al invertir la cadena se obtiene:", invertirCadena("hola"))
#print ("Al invertir la cadena se obtiene:", invertirCadena("Jafet"))


"""
Reto 6 : Invertir una lista

Entradas: pLista (lista)

Salidas:  Se obtiene de forma invertida la lista proporcionada en la entrada "pLista" cambiando el orden 
          de los elementos del último al primero

Restricciones: pLista = tipo Lista
"""

def invertirLista (pLista):
    if (pLista == []):
        return []
    
    return [pLista[-1]] + invertirLista(pLista[ :-1 ])

print ("\n6) Al invertir la lista se obtiene:", invertirLista([8,3,6,9]))



"""
Reto 7 - Determinar la suma de los dígitos impares de un número entero positivo

Entradas: pNum (int)

Salidas: Es la suma total de los dígitos impares de la entrada pNum

Restricciones: pNum debe ser un int
               Cuando pNum es = 0, retornar 0


"""
def sumarDigitosImpares(pNum):
   
    #Proceso
    if (pNum == 0):
        return 0

    if ((pNum % 10) % 2 == 1):
        return (pNum % 10) + sumarDigitosImpares(pNum//10)

     
    return sumarDigitosImpares(pNum//10)

print ("\n7) Sumando los números impares se obtiene:", sumarDigitosImpares(23567))



"""
Reto 8 - Invertir un número entero positivo
Entradas: pNum (int)

Salidas: Se obtiene de forma invertida la entrada pNum

Restricciones: pNum debe ser un int
               

"""

#Primero creé una función que cuente la longitud de la entrada
def contarLongitud(variable):
    """
    Esta función toma una variable como entrada y devuelve la longitud de la misma.
    """
    variable = str(variable)

    longitud = 0
    for elemento in variable:
        longitud += 1
    return longitud


# Luego realizé la función principal

def invertirNumero(pNum):
    # Proceso
    if (pNum == 0):
        return 0

    return (pNum % 10) * (10 ** (contarLongitud(pNum) - 1)) + invertirNumero(pNum // 10)


print("\n8) Se obtiene:", invertirNumero(1839))



"""
Reto 9 - Encontrar todos los divisores de un número entero positivo y colocarlos en una lista

Entradas: pNum (int)
          
          divisor=1

Salidas: Se obtiene en una lista todos los divisores de la entrada pNum

Restricciones: pNum debe ser un int
               divisor debe ser un int pero en caso de que no se ponga el parámetro este valdrá 1

"""

def encontrarDivisores (pNum, divisor=1):
    if (divisor > pNum):
        return []
    
    if (pNum % divisor == 0):
        return [divisor] + encontrarDivisores (pNum, divisor+ 1)
    
    else:
        return encontrarDivisores (pNum, divisor + 1)
        

print ("\n9) Los divisores son:", encontrarDivisores (18))
#print ("Los divisores son:", encontrarDivisores (5))

"""
Reto 10 - Factorial

Entradas: pNum (int)

Salidas: Se obtiene el producto de todos los números enteros positivos desde 1 hasta pNum.

Restricciones: pNum = int
"""

def numFactorial (pNum):
    if (pNum == 0):
        return 1
    
    else:
        return pNum * numFactorial(pNum - 1)

print ("\n10) El factorial del número brindado es:", numFactorial (3))

"""
Reto 11 - MCD

Entradas: a (int) y b (int)

Salidas: Se obtiene el máximo común divisor de 2 número enteros brindados en las entradas como "a" y "b"

Restricciones: a = int
               b = int
"""

def MCD (a,b):
    #Proceso
    if (b == 0):
        return a
    
    else:
        return MCD(b, a % b)
    
print ("\n11) El máximo común divisor obtenido es:", MCD ( 12, 4 ))
#print ("El máximo común divisor obtenido es:", MCD ( 18, 6 ))
    

"""
Reto 12 - Fibonacci

Entradas: pNum (int)

Salidas: Se obtiene el resultado de una serie de Fibonacci a partir del "pNum" brindado en la entrada

Restrcciones: pNum = int
"""

def fibonacci (pNum):
    #Proceso
    if (pNum < 2):
        return pNum
    
    return fibonacci(pNum - 1) + fibonacci(pNum - 2)

print ("\n12) El resultado de la serie Fibonacci es:" , fibonacci (7))



prueba = "Bu"
cadena = "HOLA MUNDO"
print (cadena.lower())

print (cadena [:len(prueba)])
   

#Prueba de recursividad de cola

def sumaDigitos (pNum):
    return sumaDigitosAux (pNum, 0)

def sumaDigitosAux (pNum, sumaTotal):
    if (pNum == 0):
        return sumaTotal
    
    else:
        return sumaDigitosAux(pNum//10, pNum%10 + sumaTotal)

print ("\Al crear una función para llamar a la otra se obtiene:", sumaDigitos(145))

#Otra manera de resolverlo

def sumaDigitos2 (pNum, sumaNueva=0):
    if (pNum == 0):
        return sumaNueva
    
    else:
        return sumaDigitos2 (pNum//10, pNum%10 + sumaNueva)

print ("\Al usar parámetros por omisión se obtiene:", sumaDigitos2 (145))

def sumaImparesCola2 (a, b, sumaImpar=0):
    if (a > b):
        return sumaImpar
    
    elif (a % 2 == 1):
        return sumaImparesCola2 (a +1, b, a + sumaImpar)
    
    else:
        return sumaImparesCola2 (a +1, b, sumaImpar)

print ("\nSuma Impares Cola: \nAl usar parámetros por omisión se obtiene:", sumaImparesCola2 (1,7))


