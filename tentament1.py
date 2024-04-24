import datetime


# def volymPyramid(B, h):
#   resultat = (B*h)/3
#   return round(resultat, 1)

# print(volymPyramid(10,5))

time = datetime.datetime.now().year


while True:
  pengar = int(input("Hur mycket pengar du har? "))
  persons_ar = int(input("Vilket år du född? "))

  gammal_ar = int(time) - persons_ar

  print("Kontroll sker...")

  if gammal_ar < 0 or gammal_ar > 150:
    print("Ogiltig år! Försök igen")

  elif pengar < 0:
    print("Pengar kan inte vara mindre än 0! Försök igen")

  elif gammal_ar > 0 and gammal_ar < 7:
    print("Biljetten är grattis för barn under 7 år")
    print("Du har råd")

  elif gammal_ar >= 7 and gammal_ar < 18 and pengar >= 50:
    print("Biljetten kostar 50:- för ungdomar") 
    print("Du har råd")

  elif gammal_ar > 18 and pengar >= 100:
    print("Biljetten kostar 100:- för vuxna") 
    print("Du har råd")

  else:
    print("Otillräckligt pengar")

