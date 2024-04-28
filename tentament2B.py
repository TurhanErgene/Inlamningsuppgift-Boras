ANTAL_KOLUMNER = 5
tal = 2
raknare = 0

antal_primal = int(input("Skriv in antal primtal som önskas visas: "))
print(f'De första {antal_primal} primtalen är:')

while raknare < antal_primal:
    ar_prim = True  # Change to True initially
    divisor = 2
    while divisor <= tal // 2:  # Change to integer division
        if tal % divisor == 0:
            ar_prim = False  # Set to False only if divisor is found
            break  # Exit the inner loop if not prime
        divisor += 1  # Move this inside the while loop

    if ar_prim:
        raknare += 1
        print(f'{tal:5d}', end='')
        if raknare % ANTAL_KOLUMNER == 0:
            print()

    tal += 1
