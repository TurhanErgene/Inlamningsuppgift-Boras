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

# def medelVärde(lista):
#     summa = sum([i for i in lista])
#     antal = len(lista)
#     return summa / antal

def medelVärde(lista):
    summa = 0
    for num in lista:
        summa += num
    return summa / len(lista)


print("Slumplista: ", slumpLista)
print("Minsta Tal: ", minstaTal(slumpLista))
print("Största Tal: ", störstaTal(slumpLista))
print("Medelvärde: ", medelVärde(slumpLista))






    
# tal = 3.1415

# print(f'Talet avrundat blev: {tal:.3}')

# print(f'Talet avrundat blev: {tal:<10.2f}')

# print(f'Talet avrundat blev: {tal:.2f}')

# print(f'Talet avrundat blev: {tal:10.2f}')
  
# dätå = 5 // 2

# print(dätå)