#LISTA
lista = [1, 23, 31, 40, 56, 16]

for x in lista:
    print(x)

for x in lista:
    print(x*2)

pares = []

for x in lista:
    if x % 2 == 0:
        pares.insert(0,x)
    pares.append(x)


def main():
    print(lista)
    print(pares)

main()

lista2 = [ 'oi',2,2,5,'top','python',45]

for x in lista2:
    if type(x) == str:
        print(x)




# if __name__ == '__main__':
#     main()

#IDEXANDO
my_list = [0, 10, 20, 30, 40, 50, 60, 70]
print(my_list[len(my_list) - 1])

for i in range(0,4):
    print(my_list[i])

for i in range(0,len(my_list)-1):
    print(my_list[i])


#Diccionario 
lista = ['a','a','b','a','c','d','e','b','b','c']


dicc = {}


for item in lista:
    keys = dicc.keys()
    if item in keys:
        dicc[item] += 1
    else:
        dicc[item] = 1
    
print(dicc)



def producto_scalar(pt1,pt2):
    len_pt1 = len(pt1)
    len_pt2 = len(pt2)    
    sum = 0
    if len_pt1 == len_pt2:
        for i in range(0,len_pt1):
            sum += (pt1[i]*pt2[i])
    return sum
print(producto_scalar([1,2,3],[0,4,7]))

# MATRICES

import numpy as np

lista1D = np.array([7,2,9,10])

lista2D = np.array([[5.2,9.1],
                    [3.0,0.1],
                    [4.5,0.3]])

lista3D = np.array([[[1,2,1,9],
                     [4,9,3,6],
                     [7,7,0,9]],
                    [[2,0,0,0],
                     [3,0,0,0],
                     [4,5,2,8]]
                     ])


print(lista1D)
print(lista2D)
print(lista3D)

print(len(lista1D))
print(len(lista2D),len(lista2D[0]))
print(len(lista3D),len(lista3D[0]),len(lista3D[0][0]))

print(len(lista1D))
print(len(lista2D)*len(lista2D[0]))
print(len(lista3D)*len(lista3D[0])*len(lista3D[0][0]))
    