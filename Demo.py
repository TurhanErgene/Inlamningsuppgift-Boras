import csv


def read_file(file_name):
    # Läs innehållet av en csv fil och returnera en lista av listor där varje sublist representerar en rad.
    data = []
    try:
        with open(file_name, newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=";")
            for row in reader:
                data.append(row)
        print(f"Data loaded successfully from {file_name}")
    except FileNotFoundError:
        print(f"Error: The file {file_name} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return data


def menu():
    """Huvudmeny för att navigera mellan uppgifter."""
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
            file1 = input(
                "Ange filnamn för befolkningsdata 2019 (eller tryck ENTER för att läsa in båda): "
            )
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
                print("Första två raderna i befolkningsdata_2022:")
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
            # Lägg till funktion för uppgift 3 här
            pass
        elif choice == "4":
            # Lägg till funktion för uppgift 4 här
            pass
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
################################################################




################################ Uppgift 3 ################################



################################################################


if __name__ == "__main__":
    menu()
