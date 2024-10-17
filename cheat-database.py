print("------------------------------------------------")
print("Először írd be a szót, majd a fogalmát!")
print("A befejezéshez írj 'print'-et")
print("------------------------------------------------")
database = {}

while True:
    szoInput = input("Szó --> ")

    if szoInput == "print":
        print(".txt fájl készítése...")
        with open("./database.txt", "w", encoding='utf-8') as file:
            file.write("let database = {\n")
            for index, (key, value) in enumerate(database.items()):
                if index == len(database) - 1:
                    file.write(f'\t"{key}": "{value}"\n')
                else:
                    file.write(f'\t"{key}": "{value}",\n')
            file.write("};")
            file.write("\ndatabase = Object.fromEntries(Object.entries(database).sort((a, b) => a[0].localeCompare(b[0], 'hu')));")
        break
    else:
        fogalomInput = input("Fogalom --> ")
        database[szoInput] = fogalomInput
