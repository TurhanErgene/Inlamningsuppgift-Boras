#0.5p
ordbok = [['jag','I'],['tycker','think'],['är','is'],['lätt','easy'],['svårt','hard'],['roligt','fun']]

sprak = input('Välkommen till (1)svenska-->engelska & (2)engelska-->svenska språköversättaren. Välj alt. 1 eller 2: ')
mening = input('Skriv in mening till översättning: ')

#1p
orden = mening.split() #dela upp inläst mening in till en lista (mellanslag blir separatorn)

#3.5p
if sprak == '1':
    for i in range(0, len(orden)): #gå igenom alla orden i meningen
        for j in range(0, len(ordbok)): #gå igenom hela ordboken
            if ordbok[j][0] == orden[i]: #om ett ord matchar ett i ordboken
                orden[i] = ordbok[j][1] #skriv direkt över ordet i orden-listan med översättningen
                break #ej nödvändigt för funktion, men ineffektivt att fortsätta gå igenom när vi redan hittat översättningen
       
    print('Översättning: ', end="")
    for x in orden:
        print(x, end=" ")

#visar ett annat sätt att "spara" resultatet på. Och finns fler varianter att göra detta på!
resultat = ""
if sprak == '2':
    for i in range(0, len(orden)):
        for j in range(0, len(ordbok)):
            if ordbok[j][1] == orden[i]:
                resultat += ordbok[j][0] + ' ' #vi sparar och bygger upp den översatta (eller delvis översatta) meningen i en ny sträng-variabel
                break
            if j == len(ordbok)-1: #ingen översättning funnen..
                resultat += orden[i] + ' '
    
    print('Översättning: ', resultat)



    
# def analysera_kol(lista, kol):

#     # Högsta 8
#     print("\nDe 8 lägsta värdena i kolumn ", kol)
#     print("Country name\t\t\t ", str(lista[0][kol]))
#     print(f"+{'-'*31}+{'-'*31}+")
#     for i, row in enumerate(lista[1:9], start=1):
#         print("|",lista[i][0],"\t\t\t|", row[kol],"\t\t\t|")
#         print(f"+{'-'*31}+{'-'*31}+")


#     # # minsta 8
#     print("\nDe 8 lägsta värdena i kolumn ", kol)
#     print("Country name\t\t\t ", str(lista[0][kol]))
#     print(f"+{'-'*31}+{'-'*29}+")
#     for i, row in enumerate(lista[-8:], start=1):
#         print("|",lista[i][0],"\t\t\t|", row[kol],"\t\t\t|")
#         print(f"+{'-'*31}+{'-'*31}+")
    


# antal_kol = int(input("Ange vilken kolumn (1-7) i listan WHR1Data som ska analyseras: "))
# analysera_kol(WHR1Data, antal_kol)
