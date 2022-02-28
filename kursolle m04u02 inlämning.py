#Inlämningsuppgift 2 moment 04
#Lukas Hermansson TE20C

lista = []

def scen(): #Valt att lägga allt i en funktion som jag kan kalla på varje gång användaren vill fortsätta. Gör att koden kan pågå hur länge som helst.
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

    restart = input("Vill du köra igen? J/N\n")
    if restart == "J":
        scen()
    elif restart == "N":
        lista.append(f"Rektangeln har haft sidorna {sid1} och {bas1} vilket gör att arean är {sid1*bas1}")
        print(lista)
        if sid1 == bas1:
            print("Detta är även en kvadrat")
        exit()
scen()