# Skriv en inledande kommentar som talar om vad programmet gör. 

#Detta program läser in två filer om förväntade befolkning, samt gör olika beräkningar på detta.

# Placera dina modulimpoter här:

import csv
import sys
import matplotlib.pyplot as plt

# Deluppgift 1: Funktioner från deluppgift 1 i ordning.
# Skriv din kod här:

def read_file(file_name):       ## Du kan lägga koden efter den här raden intill en try-except sats så blir det ett renare kod
    with open(file_name, 'r') as file:     # Du kan lägga - encoding='utf-8' - som tredje argument här för att ta bort [['ï»¿COUNTRY' " från resultatet 
        data = []
        csv_reader = csv.reader(file, delimiter=";")
        
        for row in csv_reader:
            data.append(row) 
        return data
    

def min_value(num_lista):
     min_tal = num_lista[1]
     for rad in num_lista[2:]:
        if rad < min_tal:
            min_tal = rad
     return min_tal
 

def max_value(num_lista):
    max_tal = num_lista[1]      # Kunde göra samma sak med "max_tal = num_lista[0]""
    for rad in num_lista[2:]:   # då skulle inte behövas att starta från 2. 
        if rad > max_tal:       
            max_tal = rad
    return max_tal


# Deluppgift 2: Funktioner från deluppgift 2 i ordning.
# Skriv din kod här:

"""Bra!"""
def analysera_data_uppg2(lista, ar):
    resultat = []
    for row_index, row in enumerate(lista[1:], start=1):
        land = row[0]
        min_tal = min_value(row)
        min_ar_index = row.index(str(min_value(row)))  # Find index within the current row
        min_ar = ar[min_ar_index]
        max_tal = max_value(row)
        max_ar_index = row.index(str(max_value(row)))  # Find index within the current row
        max_ar = ar[max_ar_index]
        
        tal_start = float(row[1].replace(' ', ''))  # Remove spaces and convert to float
        tal_slut = float(row[18].replace(' ', ''))  # Remove spaces and convert to float
        
        utveckling_start_slut = round(((tal_slut - tal_start) / tal_start) * 100,2)
        
        resultat.append([land, min_tal, min_ar, max_tal, max_ar,utveckling_start_slut])  # Append min_ar instead of min_value
    return resultat

# Deluppgift 3: Funktioner från deluppgift 3 i ordning.
# Skriv din kod här:
"""Fungerar Bra!"""
def analysera_data_uppg3(lista):
    # Sortera listan baserat på den sista kolumnen (förväntad befolkningsökning)
    sorterad_lista = sorted(lista, key=lambda x: x[-1], reverse=True)
    
    # Dela upp listan i de fem länderna med störst ökning och de fem länderna med mest minskning
    top_fem_okning = sorterad_lista[:5]
    top_fem_minskning = sorterad_lista[-5:]
    
    return top_fem_okning , top_fem_minskning

# Deluppgift 4: Funktioner från deluppgift 4 i ordning.
# Skriv din kod här:
"""Fattade inte riktig men kan se lite var det rikter sig"""
def analysera_data_uppg4(lista):
    # Hämta topp 5 länder med störst ökning och minskning från uppgift 3
    top_fem_okning, topp_fem_minskning = analysera_data_uppg3(lista)
    
    alla_topplander = befolkningsdata_2022
    normerad_data = []
    lander = []
    

    for a in topp_fem_minskning:    # saknas kommantär!
        for a2 in a:
              lander.append(a2[0])  # Verkar som du försöker spara landernas namn 
    
         
    for rad in befolkningsdata_2022:# saknas kommantär!
     if rad[0] in lander:
            normerad_data.append(rad)   
            
    bas_ar = normerad_data[1][0]    
    print(normerad_data)
  
        
    #(befolkning_2100 – befolkning_2022)/befolkning_2022 * 100.



# Deluppgift 5: Funktioner från deluppgift 5 i ordning.
# Skriv din kod här:


# Huvudprogram med Meny från deluppgift 0. Använd menyrubriker enl. uppgiftsbeskrivningen.
# Skriv din kod här:

while True:
    print("  Meny \n\n  ==== \n \n 1. Hämta data från fil - uppgift 1 \n 2. Analysera data - uppgift 2 \n 3. Analysera data - uppgift 3 \n 4. Analysera data - uppgift 4 \n 5. Analysera data - uppgift 5 \n 6. Avsluta")
    choice = int(input("Välj ett alternativ(1-6):"))
 
    if choice == 1:
        while True:
            filnamn_2019 = input("Ange filnamn (2019) för data från 2019 (eller tryck Enter för automatisk läsa in data för år 2019 och 2022): ")
            if filnamn_2019 == "":
                filnamn_2019 = "befolkningsdata_2019.csv"
                filnamn_2022 = "befolkningsdata_2022.csv"
                break  #Break out of the inner loop if Enter is pressed

            elif filnamn_2019 == "2019":
                 filnamn_2019 = "befolkningsdata_2019.csv"
                 
            filnamn_2022 = input("Ange filnamn (2022) för data från 2022")
            if filnamn_2022 == "2022":
               
                filnamn_2022 = "befolkningsdata_2022.csv"
                break


            
        # Read data from the files
        try:
            befolkningsdata_2019 = read_file(filnamn_2019)
            befolkningsdata_2022 = read_file(filnamn_2022)
            print("\nFörsta raden i befolkningsdata_2019.csv:")
            print(befolkningsdata_2019[:2])      # du borde ha skrivit första två rader så: [:2]
            print("\nFörsta raden i befolkningsdata_2022.csv:")
            print(befolkningsdata_2022[:2])      # du borde ha skrivit första två rader så: [:2]
        except FileNotFoundError as e:
            print(f"Fel: Filen {e.filename} hittades inte.")
            continue
    elif choice == 2:
        
        resultat = analysera_data_uppg2(befolkningsdata_2022, befolkningsdata_2022[0]) # du kunde ge år så här: befolkningsdata_2022[0]
        for rad in resultat:
             print(rad)
             
    elif choice == 3:
        #använder först uppg2 metoden i uppg3 metoden för att få top 5
        resultat = analysera_data_uppg3(analysera_data_uppg2(befolkningsdata_2022, befolkningsdata_2022[0])) # du kunde ge år så här: befolkningsdata_2022[0]
    
        for rad in resultat:
            print(rad)
            
    elif choice == 4:
        resultat = analysera_data_uppg4(analysera_data_uppg3(analysera_data_uppg2(befolkningsdata_2022, befolkningsdata_2022[0]))) # du kunde ge år så här: befolkningsdata_2022[0]
        
        #for rad in resultat:
          #  print(rad)
            
    elif choice == 6:
     sys.exit()    # kan ersättas med break så du behöver inte importera "sys" 
    
