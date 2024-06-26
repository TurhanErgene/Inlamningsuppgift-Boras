#####
# Detta program läser in två csv analyserar datan som finns i dem.
# Programmet sorterar datan som finns i dem csv filerna och skapar plot/grafer för dem på hittade datan

# Last edit: 2024-05-17 03:07
######

import csv
import matplotlib.pyplot as plt
import numpy as np


def read_file(file_name):
    # Läs innehållet av en csv fil och returnera en lista av listor där varje sublist representerar en rad.
    data = []
    try:
        with open(file_name, newline="", encoding="utf-8-sig") as file:  # utf-8-sig tar bort BOM
            reader = csv.reader(file, delimiter=";") 

            for row in reader: 
                data.append(row) 
        print(f"Data loaded successfully from {file_name}") 
    except FileNotFoundError: 
        print(f"Error: The file {file_name} was not found.")
    return data


def menu():
    befolkningsdata_2019 = [] 
    befolkningsdata_2022 = []

    while True:
        print("\nMeny\n=====") 
        print("1. Hämta data från fil – uppgift 1")
        print("2. Analysera data - uppgift 2")
        print("3. Analysera data - uppgift 3")
        print("4. Analysera data - uppgift 4")
        print("5. Analysera data - uppgift 5")
        print("6. Avsluta")
        choice = input("Välj menyalternativ (1-6): ") # få meny val från användaren

        if choice == "1": 
            file1 = input("Ange filnamn för befolkningsdata 2019 (eller tryck ENTER för att läsa in båda): ") 
            if file1 == "":
                befolkningsdata_2019 = read_file("befolkningsdata_2019.csv")
                befolkningsdata_2022 = read_file("befolkningsdata_2022.csv")
            else:
                befolkningsdata_2019 = read_file(file1) 
                file2 = input("Ange filnamn för befolkningsdata 2022: ") 
                befolkningsdata_2022 = read_file(file2) 

            if befolkningsdata_2019:
                print("Första två raderna i befolkningsdata_2019:")
                for row in befolkningsdata_2019[1:3]: 
                    print(row)
            if befolkningsdata_2022:
                print("\nFörsta två raderna i befolkningsdata_2022:")
                for row in befolkningsdata_2022[1:3]:
                    print(row)

        elif choice == "2":
            if befolkningsdata_2022:  
                # print("befolkningsdata_2022[1:]: ",str(befolkningsdata_2022[1:]))
                analyzed_data = analysera_data_uppg2(befolkningsdata_2022)
                for data in analyzed_data: 
                    print(data)
            else:
                print("Vänligen ladda befolkningsdata 2022 först (Menyalternativ 1).")

        elif choice == "3":
            if analyzed_data: 
                increase, decrease = analysera_data_uppg3(analyzed_data)
                print_table(increase, decrease) 
            else:
                print("Problem uppstod vid choice 3")
            
        elif choice == "4":
            if befolkningsdata_2022:
                # befolkningsdata_2022.pop(0) # ta bort raden med 'COUNTRY' 
                # print("befolkningsdata_2022:", befolkningsdata_2022[:3])
                analysera_data_uppg4(befolkningsdata_2022[1:]) 
            else:
                print("Problem uppstod vid choice 4")

        elif choice == "5":
            analysera_data_uppg5(befolkningsdata_2019, befolkningsdata_2022)
            
        elif choice == "6":
            print("Avslutar programmet.")
            break
        else:
            print("Ogiltigt val, försök igen.")



################################ Uppgift 2 ################################
# Returnerar det minsta värdet
def min_värde(num_lista):
     min_tal = num_lista[1]
     for rad in num_lista[2:]:
        if rad < min_tal:
            min_tal = rad
     return min_tal
 

def max_värde(num_lista):
    max_tal = num_lista[1]      
    for rad in num_lista[2:]:   
        if rad > max_tal:       
            max_tal = rad
    return max_tal

def analysera_data_uppg2(lista):
    resultat = []
    ar = lista[0]
    for i, row in enumerate(lista[1:], start=1):
        country = row[0]
        year_tvatva = float(row[1]) 
        year_hundra = float(row[18])

        min_tal = min_värde(row)
        min_ar_index = row.index(str(min_värde(row)))  # Find index within the current row
        min_ar = ar[min_ar_index]
        max_tal = max_värde(row)
        max_ar_index = row.index(str(max_värde(row)))  # Find index within the current row
        max_ar = ar[max_ar_index]
        
        
        utveckling_start_slut = round(((year_hundra - year_tvatva) / year_tvatva) * 100, 3)
        
        resultat.append([country, min_tal, min_ar, max_tal, max_ar,utveckling_start_slut])  
    return resultat


################################ Uppgift 3 ################################

def analysera_data_uppg3(lista):
    # data_rows = lista[:]

    # key=lambda x: float(x[5]): sorterar datan enligt 6:e column. Konverterar strings till floats för att numerisk sortering
    # annars det sorterar datan alfabetisk
    data_rows_sorted = sorted(lista, key=lambda x: float(x[5]), reverse=True) 

    top_increases = data_rows_sorted[:5] #lagra den högsta fem
    top_decreases = data_rows_sorted[-5:] #lagra den minsta fem

    return top_increases, top_decreases


# skriva ut topp 5 och botten 5 i en tabellform
def print_table(top_increases,top_decreases):
    print("===================================================================================================")
    print("|          Förväntad befolkningsutveckling för tio länder inom EU under åren 2022 -- 2100          |")
    print("|          Tabellen visar de fem länder med störst respektive minst förväntad befolkningsökning    |")
    print("===================================================================================================")
    print("Estimerad befolkning:\n")
    print("{:<10} {:<25} {:<25} {:<20} {:<25} {:<15}".format(
        "Land", "Lägst befolkningstalet", "År", "Högst befolkningstalet", "År", "Förändring [%]"
    ))
    print("---------------------------------------------------------------------------------------------------")


    # loopa genom angiven lista och skriva ut dem
    print("De fem länder med högsta förväntad befolkningsökning:")
    for i in top_increases:
        print("{:<10} {:<25} {:<25} {:<20} {:<25} {:<15}".format(*i))
    
    # loopa genom angiven lista och skriva ut dem
    print("\nDe fem länder med minsta förväntad befolkningsökning:")
    for i in top_decreases:
        print("{:<10} {:<25} {:<25} {:<20} {:<25} {:<15}".format(*i))


################################ Uppgift 4 ################################

def normerad_data(data):
    # Denna funktion normaliserar befolkningsdata för ett land efter dess befolkning år 2022.
    base_year_value = float(data[1])
    normalized_data = [100]  # Börja med 100 för basåret 2022
    for value in data[2:]:  # Börja från 2023 och framåt
        normalized_value = (float(value) / base_year_value) * 100
        normalized_data.append(normalized_value)
    return normalized_data

def get_top_and_bottom_countries(population_data):
    growth_rates = []
    for data in population_data:
        start_pop = float(data[1])
        end_pop = float(data[-1])
        growth_rate = (end_pop - start_pop) / start_pop * 100
        growth_rates.append((data[0], growth_rate))     # sparar datan intill growth_rates som tuple

    sorted_growth = sorted(growth_rates, key=lambda x: x[1], reverse=True) #Sorterar listan över tuplar baserat på tillväxthastigheten, från högsta till lägsta.
    top_countries = [x[0] for x in sorted_growth[:5]]       # Skapar en lista över namnen på de fem högsta länderna.
    bottom_countries = [x[0] for x in sorted_growth[-5:]]   # Skapar en lista med namnen på de fem minsta länderna.
    return top_countries, bottom_countries


def analysera_data_uppg4(lista):
    years = [2022, 2023, 2025, 2030, 2035, 2040, 2045, 2050, 2055, 2060, 2065, 2070, 2075, 2080, 2085, 2090, 2095, 2100] 
    
    top_countries, bottom_countries = get_top_and_bottom_countries(lista)

    plt.figure(figsize=(14, 7))
    for data in lista:
        if data[0] in top_countries or data[0] in bottom_countries: # Skapa plotten bara om datan finns i respektive landerna
            normalized_data = normerad_data(data)
            plt.plot(years, normalized_data, label=data[0])

    plt.title('Relativ befolkningsutveckling 2022-2100')
    plt.xlabel('År')
    plt.ylabel('Relativ befolkningsförändring (%)')
    plt.axhline(100, color='grey', linestyle='--', linewidth=0.8)  # Normvärdet 100
    plt.grid()
    plt.legend()
    plt.show()


    ################################ Uppgift 5 ################################

def analysera_data_uppg5(lista_1, lista_2):
    list_2019 = []
    list_2022 = []

    # Extrahera data för 2019
    for i, row in enumerate(lista_1[1:], start=1):
        country = row[0]
        year_nitton = float(row[1])
        year_hundra = float(row[18])
        growth_2019 = round(((year_hundra - year_nitton) / year_nitton) * 100, 3)
        list_2019.append((country, growth_2019))

    # Extrahera data för 2022 
    for i, row in enumerate(lista_2[1:], start=1):
        country = row[0]
        year_tvatva = float(row[1])
        year_hundra = float(row[18])
        growth_2022 = round(((year_hundra - year_tvatva) / year_tvatva) * 100, 3)
        list_2022.append((country, growth_2022))

    # Kombinera och sortera enligt befolkningsutveckling
    combined_data = []
    for i in range(len(list_2019)):
        country = list_2019[i][0]  # Hämta namn
        average_growth = (list_2019[i][1] + list_2022[i][1]) / 2 # hitta medelvärdet av de 2 befolkningsutveckling
        combined_data.append((country, list_2019[i][1], list_2022[i][1], average_growth))
        # print("list_2019[i][1]", list_2019[i][1])
        # print("list_2022[i][1]", list_2022[i][1])

    # print("\ncombined_data: ", combined_data)
    combined_data.sort(key=lambda x: x[3], reverse=True)  # Sort by average growth
    # print("\ncombined_data2: ", combined_data)    

    # Dela upp den sorterade datan i separata listor för plottning
    countries = [data[0] for data in combined_data]
    values_2019 = [data[1] for data in combined_data]
    values_2022 = [data[2] for data in combined_data]

    y = np.arange(len(countries))  # y-axis position for each bar
    bar_width = 0.35 

    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.barh.html
    fig, ax = plt.subplots(figsize=(10, 15))
    bars_2019 = ax.barh(y - bar_width/2, values_2019, bar_width, label='2019-2100', color='blue') #
    bars_2022 = ax.barh(y + bar_width/2, values_2022, bar_width, label='2022-2100', color='red')  

    ax.set_yticks(y)
    ax.set_yticklabels(countries)
    ax.set_xlabel('Befolkningsutveckling (%)')
    ax.set_title('Förväntade befolkningsutvecklingar 2100 för olika länder baserat på 2019 och 2022 data')
    ax.invert_yaxis()  # sortera omvänd
    ax.legend()
    plt.grid()

    plt.show()

    # print("\nresultat_2019: ", list_2019)
    # print("\nresultat_2022: ", list_2022)


if __name__ == "__main__":
    menu()