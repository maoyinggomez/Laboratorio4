#MAO YING GOMEZ URIBE SEMESTRE 2 ND SEVILLA POO
#Actividad 1
numeros= [1,2,3,4,5,6,7,8,9,10]
cuadrados=[numero**2 for numero in numeros]
print("__________________________________________________________")
print("Lista de números elevados al cuadrado", cuadrados)
print("__________________________________________________________")

#Acitividad 2
nombre=  "Mao Ying"
edad= 26
mensaje= f"Hola el nombre es {nombre} y tengo {edad} años"
print(mensaje)
print("__________________________________________________________")

#Acitividad 3
edad= 10

if edad >= 18:
    print("Eres mayor de edad")
    print("__________________________________________________________")
else:
    print("Eres menor de edad")
    print("__________________________________________________________")
    
#Acitividad 4
saldo= 100.0
while saldo>100:
    retiro=25.0
    saldo-= retiro
    print(f"Se ha retirado {retiro}, saldo actual : {saldo}")
    print("__________________________________________________________")
    
#Acitiviad 5
persona={
    "Nombre": "MaoYing",
    "Edad": 26,
    "Ciudad": "Sevilla Valle"
}
for clave, valor in persona.items():
    print(f"{clave.capitalize()}:{valor}")
    print("__________________________________________________________")