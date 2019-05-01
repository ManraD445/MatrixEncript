#Trato de poder insertar una cadena de x cantidad y
#que el script funcione.
import random,math #importa libreria math & random
print ("introduce un texto:\n"+
    "Input Text:\n")
M=input()
print("\n")
tamano= len(M)
tamano2=tamano
tamano = math.sqrt(tamano)

#print (tamano)
tEntero=int(tamano)
tEntero1=int(tamano)
residuo = tamano%tEntero

#print("«««------------»»»\n",residuo,"\n««««---------»»»»")


limtResiduo=.5
tamanoy=tEntero
tamanox=tEntero+1
indice=0
key=[]
key2=[]
if residuo == .00:
    Matrix = [[0 for x in range(tEntero1)] for y in range(tEntero1)]
    Cipher = [[0 for x in range(tEntero1)] for y in range(tEntero1)]
    aux=0
    for i in range (tEntero1):
        key.append(i)
else:
    if residuo < limtResiduo:
        Matrix = [[0 for x in range(tamanox)] for y in range(tamanoy)]
        Cipher = [[0 for x in range(tamanox)] for y in range(tamanoy)]
        aux=1
        for i in range (tamanox):
            key.append(i)
        for i in range (tamanoy):
            key2.append(i)
    else:
        Matrix = [[0 for x in range(tamanox)] for y in range(tamanox)]
        Cipher = [[0 for x in range(tamanox)] for y in range(tamanox)]
        aux=2
        for i in range (tamanox):
            key.append(i)
if aux ==0:
    for i in range(tEntero1):
        for j in range(tEntero1):
            Matrix[i][j]=M[indice]
            indice = indice+1
    print(Matrix)
    random.shuffle(key)
    print(key)
    c = ""
    for i in key:
        for j in range(tEntero1):
            c = c + Matrix[i][j]
    indice = 0
    for i in range(tEntero1):
        for j in range(tEntero1):
            Cipher[i][j]=c[indice]
            if i == key:
                Matrix[i][j]="%"
            if indice < tamano2-1:
                indice = indice+1
    c=""
    for i in range(tEntero1):
        for j in key:
            c = c + Cipher[i][j]
if aux == 1:
    coñomiki=0
    for i in range(tamanoy):
        for j in range(tamanox):
            Matrix[i][j]=M[indice]
            if coñomiki >= tamano2:
                Matrix[i][j]=" "
            if indice < tamano2-1:
                indice = indice+1
            coñomiki=coñomiki+1
    print(Matrix)
    random.shuffle(key)
    print(key)
    c = ""
    for i in key2:
        for j in range(tamanox):
            c = c + Matrix[i][j]
    indice = 0
    for i in range(tamanoy):
        for j in range(tamanox):
            Cipher[i][j]=c[indice]
            indice = indice+1
    c=""
    for i in range(tEntero1):
        for j in key:
            c = c + Cipher[i][j]
if aux == 2:
    coñomiki=0
    for i in range(tamanox):
        for j in range(tamanox):
            Matrix[i][j]=M[indice]
            if coñomiki >= tamano2:
                Matrix[i][j]=" "
            if indice < tamano2-1:
                indice = indice+1
            coñomiki=coñomiki+1
    print(Matrix)
    random.shuffle(key)
    print(key)
    c = ""
    for i in key:
        for j in range(tamanox):
            c = c + Matrix[i][j]
    indice = 0
    for i in range(tamanox):
        for j in range(tamanox):
            Cipher[i][j]=c[indice]

            if indice < tamano2-1:
                indice = indice+1
    c=""
    for i in range(tamanox):
        for j in key:
            c = c + Cipher[i][j]

c = c.replace(" ", "_")
print(c) #Se imprime la cadena ya cifrada

