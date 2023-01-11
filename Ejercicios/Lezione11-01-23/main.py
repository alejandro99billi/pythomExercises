#print("hola mundo :)")
age = 17
license = 18
if age >= 18 and license == True:
    print("Sei maggiorente") #ojo a la indetassione
    #per il
    #blocco
    #di comenti se deve usare uno '#' per cada riga
##elif
else :
    print("sei minorente")
##scrivere un programa che se x==6 il programa risteuisce x vale 5

x = 6

if x == 5 :
    print("x vale 5")
elif x==6 :           #NON si usa if anidati si usa elif
    print("x vale 6")
else :
    print("x diverso da 5 e 6")
counter = 0
while (counter<=5):
    print(counter)
    counter += 1
