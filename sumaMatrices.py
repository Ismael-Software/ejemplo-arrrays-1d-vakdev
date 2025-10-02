n = int(input("¿Cuántos números deseas ingresar? "))

numeros = []      
suma = 0          
mayor = None      

for i in range(n):
    num = float(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)

    suma += num

    if mayor is None or num > mayor:
        mayor = num

print("Resultados:")
print("Números ingresados:", numeros)
print("Suma de los números:", suma)
print("Número mayor:", mayor)
