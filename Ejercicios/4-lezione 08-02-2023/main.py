
# stampare a video y primi 10 numeri
#i=1
#for i in range (11):
 #  print(i)

#task due
def task(a, b):
    soglia = max(a, b) - min(a, b)
    while soglia >= 5:
        print("Difference:", soglia)
        soglia = soglia - min(a, b)

num1 = int(input("Inserisci il primo numero: "))
num2 = int(input("Inserisci il secondo numero: "))

task(num1, num2)




num3 = int(input("Inserisci il numero da inserire nella tavella: "))

while (num3 <11):
    for i in range (10):
       calcolo = num3 * i
       print('tabelina' + ' ' + str(num3) + 'x' + ' ' + str(i)  + ' '+'=' + str(calcolo))
    break