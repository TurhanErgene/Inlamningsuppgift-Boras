import matplotlib.pyplot as plt


# Given data
country_data = [
    ['Belgium', [11617623, 11730662, 11829411, 12009045, 12179830, 12343820, 12473485, 12559197, 12604824, 12631664, 12656450, 12687096, 12717035, 12727839, 12709791, 12669272, 12617173, 12556067]],
    ['Bulgaria', [6838937, 6941042, 6860349, 6574153, 6333689, 6155181, 6001378, 5857619, 5719739, 5577599, 5434519, 5307774, 5207097, 5133224, 5086931, 5066952, 5066236, 5072147]],
    ['Czechia', [10516707, 10963888, 11017341, 10851301, 10728942, 10716445, 10733221, 10747331, 10747298, 10713330, 10643474, 10568913, 10526487, 10520741, 10541581, 10575571, 10614609, 10645693]],
    ['Denmark', [5873420, 5927971, 5979924, 6059699, 6112281, 6140844, 6149190, 6150048, 6152708, 6163606, 6176804, 6186068, 6190185, 6184150, 6168918, 6149167, 6134161, 6126086]]
]

# Prepare data structure for the normalized percentage changes
percentage_changes = {country: [100] for country, _ in country_data}  # Start at 100 for each country

# Calculate the percentage changes
for country, populations in country_data:
    for i in range(1, len(populations)):
        yearly_change = ((populations[i] - populations[i - 1]) / populations[i - 1]) * 100
        percentage_changes[country].append(percentage_changes[country][-1] + yearly_change)  # Cumulative sum from 100

# Plotting the data
plt.figure(figsize=(10, 6))
for country, values in percentage_changes.items():
    plt.plot(range(2022, 2022 + len(values)), values, label=country)

plt.title('Normalized Annual Change of Population Percentage')
plt.xlabel('Year')
plt.ylabel('Index (Base value = 100)')
plt.legend()
plt.grid(True)
plt.show()





# # Transforming the list
# flattened_list = [item[:1] + item[1] for item in country_data]

# # # Displaying the transformed list
# for country in flattened_list:

#     print(country[1:])



# def population_change(lista):
#     for row in lista:
#         population_years = list(map(int, row[:]))  # Omvandla befolkningstal till heltal och spara inom en lista
#         change = (population_years[-1] - population_years[0]) / population_years[0] * 100
#     return change

# population_change(flattened_list)
