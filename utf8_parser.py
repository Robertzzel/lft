binary_to_hexa = lambda nr: hex(int(nr, 2))[2:]
numere = [int(input("Numar 1: ")),int(input("Numar 2: ")),int(input("Numar 3: "))]
numere = list(map(lambda nr: bin(nr)[2:], numere))
numere = list(map(lambda nr: nr.rjust(8, '0'), numere))

if numere[0].startswith("0"):
    print(f"U+{binary_to_hexa(numere[0][1:])}")
elif numere[0].startswith("110"):
    parte_nr1 = numere[0][3:]
    parte_nr2 = numere[1][2:]
    print(f"U+{binary_to_hexa(parte_nr1 + parte_nr2)}")
elif numere[0].startswith("1110"):
    parte_nr1 = numere[0][4:]
    parte_nr2 = numere[1][2:]
    parte_nr3 = numere[2][2:]
    print(f"U+{binary_to_hexa(parte_nr1 + parte_nr2 + parte_nr3)}")
elif numere[0].startswith("11110"):
    parte_nr1 = numere[0][5:]
    parte_nr2 = numere[1][2:]
    parte_nr3 = numere[2][2:]
    print(f"U+{binary_to_hexa(parte_nr1 + parte_nr2 + parte_nr3)}")
else:
    print("Ce-ai facut maica")
