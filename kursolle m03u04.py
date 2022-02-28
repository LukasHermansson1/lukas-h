#Lukas Hermansson
#TE20D
#Inte inlämningsuppgift utan vanliga m03u00

from time import localtime, strftime


timme = (localtime())
print(timme.tm_hour)



if timme == 17 or 18 or 19 or 20 or 21 or 22 or 23:
    print("Skolan är slut")
elif timme == 8 or 9 or 10 or 11 or 12 or 13 or 14 or 15 or 16:
    print("Skolan är igång")
elif timme == 00 or 1 or 2 or 3 or 4 or 5 or 6 or 7:
    print("Skolan har inte börjat")