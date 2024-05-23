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