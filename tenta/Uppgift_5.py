# Tentamen 2024-05-27 - 28 Uppgift 5 (20p)
print("Uppgift 5\n")
# Modulimporter
# Skriv kod för modulimporter och egendefinerade funktioner som används i flera deluppgifter här.
import csv

# Deluppgift 5a
# Skriv kod för funktioner från deluppgift 5a här.

def read_file(file_name):
    # Läs innehållet av en csv fil och returnera en lista av listor där varje sublist representerar en rad.
    data = []
    try:
        with open(
            file_name, newline="", encoding="utf-8-sig"
        ) as file:  # utf-8-sig tar bort BOM
            reader = csv.reader(file, delimiter=";")

            for row in reader:
                data.append(row)
        print(f"Data loaded successfully from {file_name}")
    except FileNotFoundError:
        print(f"Error: The file {file_name} was not found.")
    return data


WHR1Data = read_file("WHR2023.csv")
WHR2Data = read_file("WHR2005-2022.csv")

print(WHR1Data[:3])
print(WHR2Data[:3])


# Deluppgift 5b
# Skriv kod för funktioner från deluppgift 5b här.
import matplotlib.pyplot as plt


def analysera_kol(lista, kol):
    country = lista[0]
    data = lista[1:]

    # Sortera data efter kolumnens index (kol)
    data_rows_sorted = sorted(data, key=lambda x: float(x[kol]), reverse=True)

    # hämta de 8 högsta och minsta
    top_8 = data_rows_sorted[:8]
    bottom_8 = data_rows_sorted[-8:]

    # Printa ut högsta 8 countries
    print(f"\nDe 8 högsta värdena i kolumn {kol} ({country[kol]})")
    print(f"|{'Country name':<31}|{country[kol]:<29}|")
    print(f"+{'-'*31}+{'-'*29}+")
    for row in top_8:
        print(f"|{row[0]:<31}|{row[kol]:<29}|")
        print(f"+{'-'*31}+{'-'*29}+")

    # Printa ut minsta 8 countries
    print(f"\nDe 8 lägsta värdena i kolumn {kol} ({country[kol]})")
    print(f"|{'Country name':<31}|{country[kol]:<29}|")
    print(f"+{'-'*31}+{'-'*29}+")
    for row in bottom_8:
        print(f"|{row[0]:<31}|{row[kol]:<29}|")
        print(f"+{'-'*31}+{'-'*29}+")

    colors = [
        "#1b9e77",
        "#A890F0",
        "#fc8d62",
        "#8da0cb",
        "#a6d854",
        "#ffd92f",
        "#1f78b4",
        "#b2df8a",
        "#fb9a99",
        "#33a02c",
        "#e31a1c",
    ]

    countries = [row[0] for row in top_8 + bottom_8]
    values = [float(row[kol]) for row in top_8 + bottom_8]
    # Plotting
    plt.figure(figsize=(10, 8))
    plt.bar(countries, values, color=colors)
    plt.xlabel("Country")
    plt.ylabel(country[kol])
    plt.title(f"{country[kol]}")
    plt.xticks(rotation=90)
    plt.grid(True)
    plt.show()


antal_kol = int(
    input("Ange vilken kolumn (1-7) i listan WHR1Data som ska analyseras: ")
)
analysera_kol(WHR1Data, antal_kol)


# Deluppgift 5c
# Skriv kod för funktioner från deluppgift 5c här.


# hitta min värde
def min_värde(num_lista):
    min_tal = num_lista[0]
    for rad in num_lista[1:]:
        if rad < min_tal:
            min_tal = rad
    return min_tal


# hitta max värde
def max_värde(num_lista):
    max_tal = num_lista[0]
    for rad in num_lista[1:]:
        if rad > max_tal:
            max_tal = rad
    return max_tal


# hitta medelvärdet
def medelvärde(num_lista):
    total = 0
    for num in num_lista:
        total += num
    medel = total / len(num_lista)
    return medel


# hitta den mittersta värdet
def median_värde(num_lista):
    sorted_list = sorted(num_lista)
    n = len(sorted_list)
    if n % 2 == 1:
        return sorted_list[n // 2]
    else:
        mid1 = sorted_list[n // 2 - 1]
        mid2 = sorted_list[n // 2]
        return (mid1 + mid2) / 2  # returnera medelvärdet av de 2 värdena i mitten


def analysera_data(lista):
    headers = lista[0]
    data = lista[1:]

    ladder_score = []
    logged_gdp_per_capita = []
    social_support = []
    healthy_life_expectancy = []
    freedom_to_make_life_choices = []
    generosity = []
    perceptions_of_corruption = []

    # Skapa kolumner med data
    for row in data:
        # print("row:", row)
        ladder_score.append(float(row[1]))
        logged_gdp_per_capita.append(float(row[2]))
        social_support.append(float(row[3]))
        healthy_life_expectancy.append(float(row[4]))
        freedom_to_make_life_choices.append(float(row[5]))
        generosity.append(float(row[6]))
        perceptions_of_corruption.append(float(row[7]))

    kolumn = [ladder_score, logged_gdp_per_capita, social_support, healthy_life_expectancy, freedom_to_make_life_choices, generosity, perceptions_of_corruption]

    print(f"\n\nUppgift 5c\n+{'-'*34}+{'-'*12}+{'-'*8}+{'-'*8}+{'-'*7}+")
    print(f"|{'År 2023':<34}|{'medelvärde':<12}|{'median':<8}|{'min':<8}|{'max':<7}|")
    print(f"+{'-'*34}+{'-'*12}+{'-'*8}+{'-'*8}+{'-'*7}+")

    for i, kol in enumerate(kolumn):
        header = headers[i + 1]
        medel = medelvärde(kol)
        median = median_värde(kol)
        min_val = min_värde(kol)
        max_val = max_värde(kol)

        print(
            f"|{header:<34}|{medel:<12.2f}|{median:<8.2f}|{min_val:<8.3f}|{max_val:<7.3f}|"
        )
        print(f"+{'-'*34}+{'-'*12}+{'-'*8}+{'-'*8}+{'-'*7}+")


analysera_data(WHR1Data)


# Deluppgift 5d
# Om du väljer att lösa deluppgift 5d med funktioner skriv kod här.
# Du får också skriva koden direkt i huvudprogrammet om du vill.

## (värden_för_år_ 2007– värden_för_ år_2006)/ värden_för_år_2006 * 100
def analysera_WHR2(lista):
    landet = input("Ange det land som ska analyseras: ")





