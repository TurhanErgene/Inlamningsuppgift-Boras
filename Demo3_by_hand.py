import csv
import matplotlib.pyplot as plt


def read_file(file_name):
    # Läs innehållet av en csv fil och returnera en lista av listor där varje sublist representerar en rad.
    data = []
    try:
        with open(file_name, newline="", encoding="utf-8-sig") as file:  # utf-8-sig removes the BOM
            reader = csv.reader(file, delimiter=";")
            next(reader, None)  # Skip the header row
            for row in reader:
                data.append(row)
        print(f"Data loaded successfully from {file_name}")
    except FileNotFoundError:
        print(f"Error: The file {file_name} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return data


def menu():
    ### Huvudmeny för att navigera mellan uppgifter. 
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
        choice = input("Välj menyalternativ (1-6): ")

        if choice == "1":
            file1 = input("Ange filnamn för befolkningsdata 2019 (eller tryck ENTER för att läsa in båda): ")
            if file1 == "":
                befolkningsdata_2019 = read_file("befolkningsdata_2019.csv")
                befolkningsdata_2022 = read_file("befolkningsdata_2022.csv")
            else:
                befolkningsdata_2019 = read_file(file1)  
                file2 = input("Ange filnamn för befolkningsdata 2022: ")
                befolkningsdata_2022 = read_file(file2)  

            # Skriv ut de två första raderna från varje lista som kontroll
            if befolkningsdata_2019:
                print("Första två raderna i befolkningsdata_2019:")
                for row in befolkningsdata_2019[:2]:
                    print(row)
            if befolkningsdata_2022:
                print("\nFörsta två raderna i befolkningsdata_2022:")
                for row in befolkningsdata_2022[:2]:
                    print(row)

        elif choice == "2":
            if befolkningsdata_2022:  # Kontrollera att data har laddats
                analyzed_data = analysera_data_uppg2(befolkningsdata_2022)
                print("Analysresultat:")
                for data in analyzed_data:
                    print(data)
            else:
                print("Vänligen ladda befolkningsdata 2022 först (Menyalternativ 1).")

        elif choice == "3":
            if analyzed_data:
                ökande_lander, fallande_lander = analysera_data_uppg3(analyzed_data)
                print_table(ökande_lander, fallande_lander)
            else:
                print("Problem uppstod vid choice 3")
            
        elif choice == "4":
            if analyzed_data:
                top_increases, top_decreases = analysera_data_uppg3(befolkningsdata_2022)
                analysera_data_uppg4(befolkningsdata_2022, top_increases, top_decreases)
            else:
                print("Problem uppstod vid choice 4")

        elif choice == "5":
            # Lägg till funktion för uppgift 5 här
            pass
        elif choice == "6":
            print("Avslutar programmet.")
            break
        else:
            print("Ogiltigt val, försök igen.")



################################ Uppgift 2 ################################
def min_värde(num_list):
    # Returnerar det minsta värdet
    min_val = num_list[0]
    for num in num_list:
        if num < min_val:
            min_val = num
    return min_val

def max_värde(num_list):
    # Returnerar det största värdet
    max_val = num_list[0]
    for num in num_list:
        if num > max_val:
            max_val = num
    return max_val

def analysera_data_uppg2(lista):
    result_list = []
    for row in lista:
        country = row[0]
        population_years = list(map(int, row[1:]))  # Omvandla befolkningstal till heltal och spara inom en lista
        lowest_population = min_värde(population_years)
        highest_population = max_värde(population_years)
        lowest_year = 2022 + population_years.index(lowest_population)
        highest_year = 2022 + population_years.index(highest_population)
        population_change = (population_years[-1] - population_years[0]) / population_years[0] * 100
        result_list.append([country, lowest_population, lowest_year, highest_population, highest_year, population_change])
    return result_list



################################ Uppgift 3 ################################

def analysera_data_uppg3(lista):
    data_rows = lista[:]  # Exclude header row

    # Sort data rows based on the absolute value of the change percentage, ensuring numerical sorting
    # Reverse True to have largest changes (both increases and decreases) at the top
    data_rows_sorted = sorted(data_rows, key=lambda x: abs(float(x[5])), reverse=True)

    # Filter and get the top 5 increases (positive changes)
    top_increases = [row for row in data_rows_sorted if float(row[5]) > 0][:5]

    # Filter and get the top 5 decreases (negative changes)
    top_decreases = [row for row in data_rows_sorted if float(row[5]) < 0][:5]


    return top_increases, top_decreases


def print_table(top_increases, top_decreases):

    print("===================================================================================================")
    print("|          Förväntad befolkningsutveckling för tio länder inom EU under åren 2022 -- 2100          |")
    print("|          Tabellen visar de fem länder med störst respektive minst förväntad befolkningsökning    |")
    print("===================================================================================================")
    print("Estimerad befolkning:\n")


    print("{:<10} {:<25} {:<25} {:<20} {:<25} {:<15}".format(
        "Land", "Lägst befolkningstalet", "År", "Högst befolkningstalet", "År", "Förändring [%]"
    ))
    print("---------------------------------------------------------------------------------------------------")

    print("De fem länder med högsta förväntad befolkningsökning:")
    for i in top_increases:
        print("{:<10} {:<25} {:<25} {:<20} {:<25} {:<15}".format(*i))
    

    print("\nDe fem länder med minsta förväntad befolkningsökning:")
    for i in top_decreases:
        print("{:<10} {:<25} {:<25} {:<20} {:<25} {:<15}".format(*i))


################################ Uppgift 4 ################################

def normalisera_data(lista):
    result_list = []
    for row in lista:
        country = row[0]
        population_years = list(map(int, row[1:]))  # Omvandla befolkningstal till heltal och spara inom en lista
    
        result_list.append([country, population_years])
        
    return result_list
 
  
def analysera_data_uppg4(lista, top_countries_increase, top_countries_decrease):
    
    
    print(normalisera_data(lista))

    # print("\n\ntop_countries_increase")
    # print(top_countries_increase)

    # print("\n\ntop_countries_decrease")
    # print(top_countries_decrease)

if __name__ == "__main__":
    menu()