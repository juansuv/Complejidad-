# Pedimos al usuario que ingrese los números
num1 = 20
num2 = 6
# Seleccionamos el menor entre num1 y num2
menor = min(num1,num2)
# Realizamos un ciclo for para iterar entre
# 1 y el menor de los dos numeros
for i in range(1,menor):
    # Comprobamos la division exacta de num1 y num2 entre todos
    # todos los valores que toma i en el ciclo
    if (num1%i==0 and num2%i==0):
        # La división puede ser exacta para varios valores de i,
        # sin embargo sólo será mcd el último de estos valores
        mcd = i
        # Calculamos el Mínimo Común Múltiplo
        mcm = (num1*num2)/mcd
# Mostramos el resultado en pantalla
print("El M.C.M. entre "+str(num1)+" y "+str(num2)+" es: "+str(mcm))

#o(n)