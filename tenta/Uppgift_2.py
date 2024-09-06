# Tentamen 2024-05-27 - 28 Uppgift 2 (5p)
print('Uppgift 2\n')
# Skriv kod för din funktion här:

def sortera_ord(lista):
  print(lista)

  # sortera listan
  sorterad = sorted(lista, key=len)
  print(sorterad)

  # concat listan 
  meaning = " ".join(sorterad)
  print(meaning)
  

# Skriv kod för ditt huvudprogram med utskrift här:
Listan = ['Högskolan i Borås', 'Hej', 'åka till', 'jag', 'vill'] 

sortera_ord(Listan)