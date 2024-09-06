# Tentamen 2024-05-27 - 28 Uppgift 1 (4p)
print('Uppgift 1\n')
# Skriv kod för din funktion här:

pi = 3.14159

# skapar funktioner enligt formulen finns i uppgiften
def vol_klot(r):
    return (4 * pi * r**3)/3

def vol_cyln(r, h):
    return pi * r**2 * h

def vol_kon(r, h):
    return (pi * r**2)/3 * h

def vol_rblock(l, b, h):
    return l * b * h


# Skriv kod för ditt huvudprogram med utskrift här:


while True:
        # menyn
        print("\n-------------------")
        print("Volymberäkning:")
        print("1. Beräkna volymen av ett klot i kubikcentimeter")
        print("2. Beräkna volymen av en cylinder i kubikcentimeter")
        print("3. Beräkna volymen av en kon i kubikcentimeter")
        print("4. Beräkna volymen av ett rätblock i kubikcentimeter")
        
        val = input("Välj vilken volym du vill beräkna: ")

        # kallar funktioner enligt användarens input
        if val == '1':
            r = float(input("Ange klotets radie: "))
            volym = vol_klot(r)
            print("Volym av klot är", str(volym), " cm^3")
        
        elif val == '2':
            r = float(input("Ange cylinderns radie: "))
            h = float(input("Ange cylinderns höjd: "))
            volym = vol_cyln(r, h)
            print("Volym av cylindern är", str(volym), " cm^3")
        
        elif val == '3':
            r = float(input("Ange konens radie: "))
            h = float(input("Ange konens höjd: "))
            volym = vol_kon(r, h)
            print("Volym av kon är", str(volym), " cm^3")
        
        elif val == '4':
            l = float(input("Ange rätblockets längd: "))
            b = float(input("Ange rätblockets bredd: "))
            h = float(input("Ange rätblockets höjd: "))
            volym = vol_rblock(l, b, h)
            print("Volym av rätblock är", str(volym), " cm^3")
        
        else:
            print("Ogiltigt val, försök igen.")
            continue

        fortsätt = input("Vill du beräkna ytterligare volymer (j/n): ")
        if fortsätt== 'n':
            break










