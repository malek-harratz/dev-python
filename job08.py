a = float (input("entrer la longueur a :"))
b = float (input("entrer la longueur b :"))
c = float (input("entrer la longueur c :"))

if a <= 0 or b <= 0 or c <= 0:
    print("Les longueurs doivent être positives.")


elif a + b > c and a + c > b and b + c > a:
    print("Un triangle est possible.")

    
    if a == b == c:
        print("Le triangle est équilatéral.")
    elif a == b or a == c or b == c:
        print("Le triangle est isocèle.")
    else:
        print("Le triangle est quelconque.")

    
    cotes = sorted([a, b, c])

    if abs(cotes[0]**2 + cotes[1]**2 - cotes[2]**2) < 1e-9:
        print("Le triangle est rectangle.")

else:
    print("Il est impossible de construire un triangle avec ces longueurs.")