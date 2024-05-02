import csv
import matplotlib.pyplot as plt


def read_file(file_name):
    # Läs innehållet av en csv fil och returnera en lista av listor där varje sublist representerar en rad.
    data = []
    try:
        with open(file_name, newline="", encoding="utf-8-sig") as file:  # utf-8-sig tar bort BOM
            reader = csv.reader(file, delimiter=";") # använda ";" som delare för datan  i filen
            next(reader)  # hoppa över rubrikraden i csv filen.
            for row in reader: # gå genom datan som finns i reader
                data.append(row) # spara datan intill data
        print(f"Data loaded successfully from {file_name}") #skriva ut lyckad meddelande
    except FileNotFoundError: # om filen finns inte skriv error kod
        print(f"Error: The file {file_name} was not found.")
    return data # returnera data när funktionen får kallas


def menu():
    ### Huvudmeny för att navigera mellan uppgifter. 
    befolkningsdata_2019 = [] # initiliera en tom array
    befolkningsdata_2022 = []

    while True:
        print("\nMeny\n=====") #skriva ut menyn
        print("1. Hämta data från fil – uppgift 1")
        print("2. Analysera data - uppgift 2")
        print("3. Analysera data - uppgift 3")
        print("4. Analysera data - uppgift 4")
        print("5. Analysera data - uppgift 5")
        print("6. Avsluta")
        choice = input("Välj menyalternativ (1-6): ") # få meny val från användaren

        if choice == "1": 
            file1 = input("Ange filnamn för befolkningsdata 2019 (eller tryck ENTER för att läsa in båda): ") #få namn från användaren för data set befolkningsdata_2019.csv
            if file1 == "":
                befolkningsdata_2019 = read_file("befolkningsdata_2019.csv")
                befolkningsdata_2022 = read_file("befolkningsdata_2022.csv")
            else:
                befolkningsdata_2019 = read_file(file1)  # spara läst datan inom befolkningsdata_2019
                file2 = input("Ange filnamn för befolkningsdata 2022: ") #få namn från användaren för data set befolkningsdata_2022.csv
                befolkningsdata_2022 = read_file(file2)  # spara läst datan inom befolkningsdata_2022

            # Om nåt data finns skriv ut de två första raderna från varje lista som kontroll
            if befolkningsdata_2019:
                print("Första två raderna i befolkningsdata_2019:")
                for row in befolkningsdata_2019[:2]: 
                    print(row)
            if befolkningsdata_2022:
                print("\nFörsta två raderna i befolkningsdata_2022:")
                for row in befolkningsdata_2022[:2]:
                    print(row)

        #  Om befolkningsdata_2022 har laddats skicka den till respektive funktion 
        elif choice == "2":
            if befolkningsdata_2022:  # Kontrollera att data har laddats
                analyzed_data = analysera_data_uppg2(befolkningsdata_2022)
                print("Analysresultat:")
                for data in analyzed_data: # skriva ut returnerad data
                    print(data)
            else:
                print("Vänligen ladda befolkningsdata 2022 först (Menyalternativ 1).")

        elif choice == "3":
            if analyzed_data: # kontrollera om datan har laddats från tidigare funktion
                increase, decrease = analysera_data_uppg3(analyzed_data) # spara datan som returnerad från funktion intill increase och decrease
                print_table(increase, decrease) #kalla funktionen för att printa ut datan
            else:
                print("Problem uppstod vid choice 3")
            
        elif choice == "4":
            if befolkningsdata_2022:
                top_increases, top_decreases = analysera_data_uppg3(befolkningsdata_2022) 
                analysera_data_uppg4(befolkningsdata_2022, top_increases, top_decreases) # skicka in data till analysera_data_uppg4()
            else:
                print("Problem uppstod vid choice 4")

        elif choice == "5":
            # Ska läggas senare
            pass
        elif choice == "6":
            print("Avslutar programmet.")
            break
        else:
            print("Ogiltigt val, försök igen.")



################################ Uppgift 2 ################################
# Returnerar det minsta värdet
def min_värde(num_list):
    min_val = num_list[0]
    for num in num_list:
        if num < min_val:
            min_val = num
    return min_val

# Returnerar det största värdet 
def max_värde(num_list):
    max_val = num_list[0] 
    for num in num_list: 
        if num > max_val:
            max_val = num
    return max_val

def analysera_data_uppg2(lista):
    result_list = []
    for row in lista:
        country = row[0]
        year_tvatva = int(row[1]) #spara år 2022
        year_hundra = int(row[18]) #spara år 2100
       
        population_years = list(map(int, row[1:]))  # Omvandla befolkningstal till heltal och spara inom en lista
        lowest_population = min_värde(population_years) # hitta minsta värde
        highest_population = max_värde(population_years) # hitta hösta värde
        lowest_year = 2022 + population_years.index(lowest_population) # hitta året som befolkningen är lägst
        highest_year = 2022 + population_years.index(highest_population) # hitta året som befolkningen är högst
        population_change = (year_hundra - year_tvatva) / year_hundra * 100 # beräkna procentförändring av befolkningsstorleken
        result_list.append([country, lowest_population, lowest_year, highest_population, highest_year, population_change]) # spara alla data inom result_list
    return result_list



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

def normalize_population_data(data, base_year_index): # base_year_index kan tas bort om den ersättas med 0 men det är lättare att läsa så här
    base_value = float(data[base_year_index].replace(' ', '')) # extrahera basvärdet, hämtar befolkningsantalet för basåret och omvandlar den till float samt tar bort mellanslag
    return [((float(value.replace(' ', '')) / base_value) * 100) if value.strip() else None for value in data] # omvandlar varje befolkningsantalet till float, tar bort mellanslag och beräknar procenten för basåret. Om ett värde är tomt returneras None


# Grafen inte innehåller de högst och lägst landerna efter befolkningsförändringsprocent, utan bara de med högsta och lägsta befolkningen.
def analysera_data_uppg4(lista, top_countries_increase, top_countries_decrease):
    years = [2022, 2023, 2025, 2030, 2035, 2040, 2045, 2050, 2055, 2060, 2065, 2070, 2075, 2080, 2085, 2090, 2095, 2100] # gav året manuellt, kanske ska optimeras senare

    plt.figure(figsize=(12, 8)) # skapar en tabell i matplot

    for country_data in top_countries_increase + top_countries_decrease:
        country_name = country_data[0] 
        normalized_data = normalize_population_data(country_data[1:], 0)  # förlättar datan så blir det enklare att jobba med, exkluderar country namn
        plt.plot(years, normalized_data, label=country_name) #skapar grafen för normalizerade datan och skriver varje linje med landers namn

    plt.title('Förväntad befolkningsutveckling inom EU för tidsperioden 2022 - 2100') # sätter titeln och etiketterna för axlarna
    plt.xlabel('År')
    plt.ylabel('Relativ befolkningsförändring från 2022 (%)')

    plt.axhline(100, color='grey', linewidth=0.8, linestyle='--')  # Horizontal line at the 100% level
    plt.grid(True) # ritar grid
    plt.legend() # skapar tabelln för landernas namn
    plt.show() # visar grafen


# kallar menyn så här så att det är lättare att börja att kodera från var som helst.
if __name__ == "__main__":
    menu()