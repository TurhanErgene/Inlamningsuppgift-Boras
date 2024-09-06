# Tentamen 2024-05-27 - 28 Uppgift 3 (4p)
print('Uppgift 3\n')
# Hitta felen och rätta koden. Glöm inte skriva kommentar vid varje rättning.

def sortera_funtion(lista):
    for index in range(0, len(lista)):
        minsta = index
        for i in range(index, len(lista)):
            if lista[minsta] > lista[i]:
                minsta = i  # Använd korrekt index för minsta elementet eftersom vi kontrollerar om lista[minsta] är större än lista[i] om är det så bör vi bestämma/initiate den nya minsta
                
        lista[index], lista[minsta] = lista[minsta], lista[index]  # Korrigerade värdet att byta med rätt index
    return lista


lista = [5, 65, -4, 111, 78, 348, 97, -14, 47]

print(f'Den ursprungliga listan är: ')
print(f'{lista} ')
print('-'*30)
print(f'Den sorterade listan är: ')
print(f'{sortera_funtion(lista)}')