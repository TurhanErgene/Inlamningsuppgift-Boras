import csv
import matplotlib.pyplot as plt
import numpy as np


def read_file(file_name):
    data = []
    try:
        with open(file_name, newline="", encoding="utf-8-sig") as file:
            reader = csv.reader(file, delimiter=";")
            next(reader)  # Skip header
            data = [row for row in reader]
        print(f"Data loaded successfully from {file_name}")
    except FileNotFoundError:
        print(f"Error: The file {file_name} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return data


def analysera_data_uppg2(lista):
    result_list = []
    for row in lista:
        country = row[0]
        population_years = list(map(int, row[1:]))
        lowest_population = min(population_years)
        highest_population = max(population_years)
        lowest_year = 2022 + population_years.index(lowest_population)
        highest_year = 2022 + population_years.index(highest_population)
        population_change = (
            (population_years[-1] - population_years[0]) / population_years[0]
        ) * 100
        result_list.append(
            [
                country,
                lowest_population,
                lowest_year,
                highest_population,
                highest_year,
                population_change,
            ]
        )
    return result_list


def analysera_data_uppg3(lista):
    data_rows_sorted = sorted(lista, key=lambda x: float(x[-1]), reverse=True)
    top_increases = data_rows_sorted[:5]
    top_decreases = data_rows_sorted[-5:]
    print_table("De fem länder med högsta förväntad befolkningsökning:", top_increases)
    print_table("De fem länder med minsta förväntad befolkningsökning:", top_decreases)
    return top_increases, top_decreases


def print_table(title, data):
    print("\n" + "=" * 100)
    print(title)
    print(
        "{:<20} {:<20} {:<15} {:<20} {:<15} {:<10}".format(
            "Land",
            "Lägst befolkningstalet",
            "År",
            "Högst befolkningstalet",
            "År",
            "Förändring [%]",
        )
    )
    for row in data:
        try:
            # Ensure the last element, the percentage change, is treated as a float for formatting
            print(
                "{:<20} {:<20} {:<15} {:<20} {:<15} {:<10.2f}".format(
                    row[0], row[1], row[2], row[3], row[4], float(row[5])
                )
            )
        except ValueError as e:
            print(f"Error formatting row {row}: {e}")


def normalisera_population_data(data):
    """ Normalize population data such that the value for 2022 is 100. """
    base_value = float(data[0].strip())  # Assuming the first value is for 2022
    return [100 * (float(value.strip()) / base_value) for value in data]


def interpolate_data_to_2100(years, data):
    """ Interpolate data to fill up to the year 2100 if necessary """
    if years[-1] < 2100:
        extended_years = list(range(years[0], 2101))
        interpolated_data = np.interp(extended_years, years, data)
        return extended_years, interpolated_data
    return years, data

def analysera_data_uppg4(countries_data, top_increase, top_decrease):
    plt.figure(figsize=(12, 8))

    # Find the range of years based on the length of any data entry (assuming all are the same length)
    start_year = 2022
    end_year = 2022 + len(countries_data[0][1:]) - 1  # assumes all rows have same number of data points
    years = list(range(start_year, end_year + 1))

    # Collect all relevant countries into one list for easier processing
    relevant_countries = top_increase + top_decrease

    for country_data in relevant_countries:
        country_name = country_data[0]
        population_data = country_data[1:]  # Exclude the country name from the data
        normalized_data = normalisera_population_data(population_data)

        plt.plot(years, normalized_data, label=country_name)

    plt.title('Förväntad befolkningsutveckling inom EU för tidsperioden 2022 - 2100')
    plt.xlabel('År')
    plt.ylabel('Relativ befolkningsförändring från 2022 (%)')
    plt.axhline(100, color='grey', linestyle='--', linewidth=0.8)  # Base line at 100%
    plt.grid(True)
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))  # Adjust legend location
    plt.xlim(start_year, end_year)
    plt.show()

    

def menu():
    befolkningsdata_2019 = []
    befolkningsdata_2022 = []
    analyzed_data = []
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
            if file1.strip() == "":
                befolkningsdata_2019 = read_file("befolkningsdata_2019.csv")
                befolkningsdata_2022 = read_file("befolkningsdata_2022.csv")
            else:
                befolkningsdata_2019 = read_file(file1)
                file2 = input("Ange filnamn för befolkningsdata 2022: ")
                befolkningsdata_2022 = read_file(file2)
        elif choice == "2":
            if befolkningsdata_2022:
                analyzed_data = analysera_data_uppg2(befolkningsdata_2022)
                print("Analysresultat:")
                for data in analyzed_data:
                    print(data)
            else:
                print("Vänligen ladda befolkningsdata 2022 först (Menyalternativ 1).")
        elif choice == "3":
            if analyzed_data:
                analysera_data_uppg3(analyzed_data)
            else:
                print("Problem uppstod vid choice 3")
        elif choice == "4":
            if befolkningsdata_2022:
                top_increases, top_decreases = analysera_data_uppg3(befolkningsdata_2022)
                analysera_data_uppg4(befolkningsdata_2022, top_increases, top_decreases)
            else:
                print("Problem uppstod vid choice 4")

        elif choice == "5":
            pass  # Implement when ready
        elif choice == "6":
            print("Avslutar programmet.")
            break
        else:
            print("Ogiltigt val, försök igen.")


if __name__ == "__main__":
    menu()
