import random

difficolta=int(input("Seleziona difficoltà: \n 1 - facile \n 2 - medio \n 3 - difficile "))

n_lat=[8, 12, 16]
n_bom=[10, 25, 50]

lato = n_lat[difficolta-1]
bombe = n_bom[difficolta-1]


def stampa(matrice):
    for j in range(len(matrice)):
        for i in range(len(matrice[j])):
            print(matrice[j][i], end=" ")
        print()
    print()


def zeri(campo, r, c, mostra):
    cornice=[]
    posizione=[]

    for i in range(8):
        cornice.append(campo[r+agg_righe[i]][c+agg_colon[i]])
        posizione.append([r+agg_righe[i], c+agg_colon[i]])

    if 0 in cornice:
        continua=True
    else:
        continua=False

    for i in range(len(cornice)):
        mostra[posizione[i][0]-1][posizione[i][1]-1]=cornice[i]
    
    stampa(mostra)

    lista_zeri=[]

    while continua:
        for e in range(len(cornice)):
            x=posizione[e][0]
            y=posizione[e][1]
            if x!=lato+1 and x!=0 and y!=lato+1 and y!=0:
                mostra[x-1][y-1]=cornice[e]
            

            if cornice[e]==0:
                cornice[e]="-"
                lista_zeri.append(posizione[e])
                for i in range(8):
                    if [x+agg_righe[i],y+agg_colon[i]] not in posizione:
                        cornice.append(campo[x+agg_righe[i]][y+agg_colon[i]])
                        posizione.append([x+agg_righe[i], y+agg_colon[i]])
            
        if 0 in cornice:
            continua=True
        else:
            continua=False

            
    for elem in range(len(lista_zeri)):
        mostra[lista_zeri[elem][0]-1][lista_zeri[elem][1]-1]=0

    return mostra


campo = [[0 for _ in range(lato+2)] for _ in range(lato+2)]
for i in range(lato+2):
    for j in range(lato+2):
        if i==0 or j==0 or i==lato+1 or j==lato+1:
            campo[i][j]="x"

start = str(input("coordinate (r c): "))


r = int(start.split()[0])+1
c = int(start.split()[1])+1

print(r,c)

lista_bombe=[]

for i in range(bombe):
    x = random.randint(1, lato)
    y = random.randint(1, lato)
    while [x,y]==[r-1,c-1] or [x,y]==[r-1,c] or [x,y]==[r-1,c+1] or [x,y]==[r,c-1] or [x,y]==[r,c] or [x,y]==[r,c+1] or [x,y]==[r+1,c-1] or [x,y]==[r+1,c] or [x,y]==[r+1,c+1] or [x,y] in lista_bombe:
        x = random.randint(1, lato-1)
        y = random.randint(1, lato-1)
    lista_bombe.append([x,y])
    
    campo[x][y]= 9

agg_righe= [-1,-1,-1, 0, 0, 1, 1, 1]
agg_colon= [-1, 0, 1,-1, 1,-1, 0, 1]

for i in range(1, lato+1):
    for j in range(1, lato+1):
        if campo[i][j]!=9:
            contorno=0
            while contorno<8:
                if campo[i+agg_righe[contorno]][j+agg_colon[contorno]]==9:
                    campo[i][j]+=1
                contorno+=1

mostra = [['-' for _ in range(lato)] for _ in range(lato)]

mostra[r-1][c-1]=campo[r][c]

mostra=zeri(campo, r, c, mostra)

stampa(mostra)

gioca=True

while gioca:
    start = str(input("coordinate (r c): "))
    r = int(start.split()[0])+1
    c = int(start.split()[1])+1

    if campo[r][c]==9:
        gioca=False
        mostra[r-1][c-1]="X"
        stampa(mostra)
        print("HAI PERSO")

    elif campo[r][c]==0:
        mostra=zeri(campo, r, c, mostra)
        stampa(mostra)

    else:
        mostra[r-1][c-1]=campo[r][c]
        stampa(mostra)

    conta= sum(row.count("-") for row in mostra)
    
    if conta==10:
        gioca=False
        print("HAI VINTO")
    
    print("Caselle rimanenti: ", conta-10)

sol = [row[1:lato+1] for row in campo[1:lato+1]]
for i in range(lato):
    for j in range(lato):
        if sol[i][j]==9:
            sol[i][j]="X"

stampa(sol)











