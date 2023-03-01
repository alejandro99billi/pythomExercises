matrice = [[0 for j in range(4)] for i in range(6)]

for i in range(6):
    for j in range(4):
        matrice[i][j] = (i + j) % 4


for riga in matrice:
    print(riga)

for i in range(6):
    for j in range(4):
        print(j,end='')
    print()