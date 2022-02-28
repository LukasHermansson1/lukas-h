#Lukas Hermansson
#TE20D
#Inte inlämningsuppgift utan vanliga m03u00

namn = input("Vad heter du?: ")
alder = int(input("Hur gammal är du?: "))

namn = namn.strip()

print(f"Så ditt namn är {namn} och din ålder är {alder}.")
print(f"Första boktstaven i ditt namn måste vara {namn[0]}.")

if alder >= 18:
    print("Din ålder säger mig att du är myndig. \nEftersom du är över 18 år. KUL!")
else:
    print("Myndig är du dock ej.")