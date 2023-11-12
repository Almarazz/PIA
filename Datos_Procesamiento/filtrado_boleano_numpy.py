import numpy as np 

arreglo_uni = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

filtro = arreglo_uni < 5
print(filtro)

resultado = arreglo_uni [filtro]
print()
print(resultado)

matriz_ejemplo = np.random.randint(1,300,   size=(2,5))
print(matriz_ejemplo)
print()

filtro = matriz_ejemplo > 100
print(filtro)
print()

resultado = matriz_ejemplo[filtro]
print(resultado) 


datos = np.random.randint(1,200, size=(18,))
print('Los datos son: ')
print(datos)

minimo = datos.min()
maximo = datos.max()

print(f'\nLos datos tienen un rango de {maximo - minimo}, abarcando desde el {minimo} hasta el {maximo}')

minimo = np.amin(datos)
maximo = np.amax(datos)

print(f'\nLos datos tienen un rango de {maximo - minimo} abrcando desde el {minimo} hasta el {maximo}')

primer_cuartil = np.percentile(datos, 25)
mediana = np.median(datos)
tercer_cuartil = np.percentile(datos, 75)


print(f'\nLa mediana de los datos es igual a {mediana}')
print(f'El primer cuartil es igual a {primer_cuartil} mientras que el tercer cuartil es igual a {tercer_cuartil}')
print(f'Con rango intercuartil {primer_cuartil} a {tercer_cuartil} o {tercer_cuartil - primer_cuartil}')



media = datos.mean()
desviacion_estandar = datos.std()
varianza = datos.var()

print(f'\Los datos poseen una media aritmetica de {media: .4f}, con una varianza de {varianza: .4f} y una desviacion estandar de {desviacion_estandar: .4f}')


media = np.mean(datos)
desviacion_estandar = np.std(datos)
varianza = np.var(datos)

print(f'\Los datos poseen una media aritmetica de {media: .4f}, con una varianza de {varianza: .4f} y una desviacion estandar de {desviacion_estandar: .4f}')
