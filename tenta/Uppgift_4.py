# Tentamen 2024-05-27 - 28 Uppgift 4 (7p)
print('Uppgift 4\n')

# Skriv kod för ditt program med utskrift här:
import matplotlib.pyplot as plt

def bakterie_growth(initial_population, tillväxtfaktorn): #förändringsfaktor
    population = initial_population
    populationer = [population] # start värde
    tid = 0
    tider = [tid]

    while population < 10 * initial_population: # tills det dubblar tio gånger
        population = population + tillväxtfaktorn * population  #  P(t+1) = P(t) + r * P(t)
        tid += 1
        populationer.append(population)
        tider.append(tid)
    
    return tider, populationer



start_värde = 10000

öknings_procent = float(input("Ange tillväxtfaktorn i procent: "))
öknings_rate = öknings_procent

# beräkna tillväxten
tider, populationer = bakterie_growth(start_värde, öknings_rate)

# printa ut resultatet
print("Tid - Populationsmängd")
print("----------------------")
for i in range(len(tider)):
    print(f"{tider[i]:<4}  {populationer[i]:.2f}")


# printa ut tiden det populationen att ta tiodubblas
print(f"\nDet tar {tider[-1]} minuter för population att tiodubblas")
print(f"och populationsstorleken vid denna tidpunkt är {populationer[-1]:.0f}")


# printa graferna
plt.plot(tider, populationer)
plt.xlabel('Tid (minuter)')
plt.ylabel('Populationsmängd')
plt.title(f'Populationsmängd för tillväxtfaktorn {öknings_procent}')
plt.grid(True)
plt.show()

