nombre = "Juan"
nombre =  45 #se cambia la variable, segun como la aignemos

print(type(nombre))

dato1 = 10
dato2 = 20
print(str(dato1)+str(dato2))

#Anidar
registro = True
edad = 20
print(type(registro)) #Inprimir el tipo de dato
print(type(edad))

if edad >= 18 and registro == True:
    print("tiene permiso")
else:
    print("no tiene permiso")
    if edad < 18:
        print("no tiene permiso por ser menor de edad")