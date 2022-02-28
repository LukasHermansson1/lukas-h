#Inlämningsuppgift 1 moment 04
#Lukas Hermansson TE20C

print("Denna applikation gör ett antal beräkningar på en rektangel/rätblock.")
sid1 = int(input("Ange rektangelns ena sida: "))
bas1 = int(input("Ange rektangelns andra sida: "))
print(f"Rektangeln har sidorna {sid1} och {bas1} vilket gör att arean är {sid1*bas1}")


area = sid1 * bas1
x = ("-")
y = ("|")

if sid1 == bas1:
    print("Eftersom bägge sidorna är lika långa så är denna rektangel en kvadrat.")


print(f"\nHöjden | Volym\n{x:-<14}")
for i in range(1, 11):
    volym = bas1 * i * bas1
    print("{0: >6} | {1: >5}".format(i, volym))
