    nicknames_to_delete = ["nutuk", "kuran", "miyavettin"]

    nicknames = None
    with open("deneme.csv") as sourceFile:
        nicknames = sourceFile.read().splitlines()

    for nick in nicknames_to_delete:
        try:
            if nick in nicknames:
                nicknames.pop(nicknames.index(nick))
            else:
                print(nick + " is not found in the file")
        except ValueError:
            pass

    with open("deneme.csv", "a") as nicknamesFile:
        nicknamesFile.seek(0)
        nicknamesFile.truncate()
        nicknamesWriter = csv.writer(nicknamesFile)
        for name in nicknames:
            nicknamesWriter.writerow([str(name)])
    nicknamesFile.close()