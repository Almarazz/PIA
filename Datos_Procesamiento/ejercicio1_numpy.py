import numpy as np

lista_de_listas = [[2,0],[3,0],[3,1],[5,0],[5,1],[5,2]]
print(lista_de_listas)
print()
a = np.array([[2,0],[3,0],[3,1],[5,0],[5,1],[5,2]])
print('El contenido del array numpy es: ')
print(a)

print(f'Y es un objeto de tipo {type(a)}')

a[:,0] = 15
print( a)
print()
a[:,1] = 30
print(a)

arreglo2 = np.zeros(shape =(2,4), dtype= int)
print(arreglo2)
print(f'\nLas dimensiones del arreglo son {arreglo2.shape}')


arreglo_aleatorio = np.random.randint(1,11, size=10)
print(arreglo_aleatorio)

matriz_aleatorio = np.random.randint(1,11, size=(2,4))
print(matriz_aleatorio)

dos_en_dos = np.arange(10,25,2)
print(dos_en_dos)
print(f'\nLas dimensiones de la estructura resultante son: {dos_en_dos.shape}')

lista= [10, 'abc', 20]
print(lista)
print(*[type(elemento) for elemento in lista], sep='\n')

arreglo1 = np.array([10, 'abc', 20])
print(arreglo1)
print(*[type(elemento) for elemento in arreglo1], sep ='\n')

lista = [10, 15, 20, 25]
print(lista)
print(f'\n{lista * 2 } ')

arreglo = np.array([10,15,20,25])
print(arreglo)
print()
print(arreglo *2)

matrizA = np.random.randint(1, 300, size=(5,10))
matrizB = np.random.randint(1, 300, size=(5,10))

print(f'matriz A\n{matrizA}')
print('\nX\n')
print(f'matriz B\n{matrizB}')
print('\n=\n')
print(matrizA * matrizB)


