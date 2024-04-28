# import datetime


# # def volymPyramid(B, h):
# #   resultat = (B*h)/3
# #   return round(resultat, 1)

# # print(volymPyramid(10,5))

# time = datetime.datetime.now().year


# while True:
#   pengar = int(input("Hur mycket pengar du har? "))
#   persons_ar = int(input("Vilket år du född? "))

#   gammal_ar = int(time) - persons_ar

#   print("Kontroll sker...")

#   if gammal_ar < 0 or gammal_ar > 150:
#     print("Ogiltig år! Försök igen")

#   elif pengar < 0:
#     print("Pengar kan inte vara mindre än 0! Försök igen")

#   elif gammal_ar > 0 and gammal_ar < 7:
#     print("Biljetten är grattis för barn under 7 år")
#     print("Du har råd")

#   elif gammal_ar >= 7 and gammal_ar < 18 and pengar >= 50:
#     print("Biljetten kostar 50:- för ungdomar") 
#     print("Du har råd")

#   elif gammal_ar > 18 and pengar >= 100:
#     print("Biljetten kostar 100:- för vuxna") 
#     print("Du har råd")

#   else:
#     print("Otillräckligt pengar")

numbers = [-15, -2, -7, -30]
max_val = float('-inf')

for num in numbers:
    if num > max_val:
        max_val = num

print(max_val)  # Output will be -3, the highest number in the list


numbers = [10, -20, 5, 8]
max_val = 0

for num in numbers:
    if num > max_val:
        max_val = num

print(max_val)  # Output will be 20, the highest number in the list
