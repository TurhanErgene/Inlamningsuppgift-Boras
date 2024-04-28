import random


# slumpLista = [random.randint(1, 10) for _ in range(5)]

slumpLista = []
for i in range(5):
    number = random.randint(1, 10)
    slumpLista.append(number)


def minstaTal(lista):
    minstaTal = lista[0]
    for i in lista:
        if i < minstaTal:
            minstaTal = i
    return minstaTal

def störstaTal(lista):
    störstaTal = lista[0]
    for i in lista:
        if i > störstaTal:
            störstaTal = i
    return störstaTal

def medelVärde(lista):
    summa = 0
    for num in lista:
        summa += num
    return summa / len(lista)


print("Slumplista: ", slumpLista)
print("Minsta Tal: ", minstaTal(slumpLista))
print("Största Tal: ", störstaTal(slumpLista))
print("Medelvärde: ", medelVärde(slumpLista))


# print(int(5 // 2))
# print(f' {8:5d}', end = "")


def isprime(num):
    if num==2 or num==3:
        return True
    if num%2==0 or num<2:
        return False
    for n in range(3,int(num**0.5)+1,2):   
        if num%n==0:
            return False   
    return True
print(isprime(13))
print(isprime(18))
print(isprime(17))