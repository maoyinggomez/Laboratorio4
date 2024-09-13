#MAO YING GOMEZ URIBE SEMESTRE 2 ND SEVILLA POO

#Acitividad 1
def fibonacci(n,memo={}):
    if n in  memo:
        return memo[n]
    if n<=1:
        return n
    memo[n]=fibonacci(n-1,memo)+fibonacci(n-2,memo)
    return memo[n]
resultado=fibonacci(150)
print("__________________________________________________________")
print("Fibonacci de 150 es:", resultado)
print("__________________________________________________________")
#Actividad 2
from decimal import Decimal,getcontext
getcontext().prec=38
numero1=Decimal('1.123456789123456789')
numero2=Decimal('2.987654321987654321')
resultado= numero1*numero2
print(f"El resultado precisio es: {resultado}")
print("__________________________________________________________")
#Acitividad 3
import re

cadena = "ESTE ES un CODIGO DE USO ejemplo de CADENAS y expresiones  MAYUSCULAS y minusculas o bien, REGULARES"
patron = r'\b[A-Z]{2,}\b'
palabrasMayusculas = re.findall(patron, cadena)
print("Palabras en mayusculas:", palabrasMayusculas)
print("__________________________________________________________")
#Acitividad 4
a= True
b= False
c= True

resultado=(a and b) or (a and c) ^ b

print("Resultado de la operacion logica compleja:", resultado)
print("__________________________________________________________")

#Actividad 5

def sumar_o_default(a, b):

    return (a or 0) + (b or 0)
print(sumar_o_default(5, None)) 
print(sumar_o_default(None, None))  
print(sumar_o_default(10, 20))  
print("__________________________________________________________")
