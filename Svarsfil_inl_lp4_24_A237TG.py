# Skriv en inledande kommentar som talar om vad programmet gör. 


# Placera dina modulimpoter här:


# Deluppgift 1: Funktioner från deluppgift 1 i ordning.
# Skriv din kod här:
def menu():
  while True:
        print("""
        Meny
        =====
        1. Hämta data från fil – uppgift 1
        2. Analysera data - uppgift 2
        3. Analysera data - uppgift 3
        4. Analysera data - uppgift 4
        5. Analysera data - uppgift 5
        6. Avsluta
        """)
        choice = input("Välj menyalternativ (1-6): ")
        if choice == '1':
            read_files()
        elif choice == '2':
            analyze_data_uppgift2()
        elif choice == '3':
            analyze_data_uppgift3()
        elif choice == '4':
            analyze_data_uppgift4()
        elif choice == '5':
            analyze_data_uppgift5()
        elif choice == '6':
            print("Programmet avslutas...")
            break
        else:
            print("Ogiltigt val, försök igen.")

def read_files():
    print("read files")

# Deluppgift 2: Funktioner från deluppgift 2 i ordning.
# Skriv din kod här:
def analyze_data_uppgift2():
    print("Plats för funktionen som analyserar data för uppgift 2.")

# Deluppgift 3: Funktioner från deluppgift 3 i ordning.
# Skriv din kod här:
def analyze_data_uppgift3():
    print("Plats för funktionen som analyserar data för uppgift 3.")

# Deluppgift 4: Funktioner från deluppgift 4 i ordning.
# Skriv din kod här:
def analyze_data_uppgift4():
    print("Plats för funktionen som analyserar data för uppgift 4.")

# Deluppgift 5: Funktioner från deluppgift 5 i ordning.
# Skriv din kod här:
def analyze_data_uppgift5():
    print("Plats för funktionen som analyserar data för uppgift 5.")

# Huvudprogram med Meny från deluppgift 0. Använd menyrubriker enl. uppgiftsbeskrivningen.
# Skriv din kod här:

menu()