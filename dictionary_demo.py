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



def analysera_data_uppg2(lista):
    result_list = []
    for row in lista:
        country = row[0]
        year_tvatva = int(row[1])
        year_hundra = int(row[18])
       

        population_change = (year_hundra - year_tvatva) / year_hundra * 100
        result_list.append([country, population_change])
    return result_list


befolkningsdata_2022 = read_file("befolkningsdata_2022.csv")

def find_extremes(data):
    # Sorting the list based on the percentage change
    data_sorted = sorted(data, key=lambda x: x[1])

    # Selecting the top 5 decreases and increases
    lowest_five = data_sorted[:5]
    highest_five = data_sorted[-5:][::-1]

    # Creating dictionaries for increases and decreases
    countries_decrease = {country: round(value, 2) for country, value in lowest_five}
    countries_increase = {country: round(value, 2) for country, value in highest_five}

    return countries_increase, countries_decrease



analyzed_data = analysera_data_uppg2(befolkningsdata_2022)

countries_increase, countries_decrease = find_extremes(analyzed_data)
print("Countries with the largest population increase:")
print(countries_increase)
print("\nCountries with the largest population decrease:")
print(countries_decrease)
