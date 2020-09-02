class laulA():
    def __init__(self, lauluNimi):
        self.lauluNimi = lauluNimi

class artist():
    def __init__(self, artistiNimi):
        self.artistiNimi = artistiNimi

class albumA():
    def __init__(self, albumiNimi):
        self.albumiNimi = albumiNimi



b = input("Kas soovite lisada laule juurde?: ")
if b == "jah":
    seis = "aktiivne"
    grupp = artist(input("Sisestage esitaja nimi: "))
    album = albumA(input("Sisestage albumi nimi: "))
    aasta = input("Sisestage aasta: ")
    # Tsükkel kestab kuni seis = aktiivne.
    while seis == "aktiivne":
        laul = laulA(input("Sisestage laulu pealkiri: "))
        # Liidab kokku esitaja, albumi, aasta ning laulu. Vahel on tabulutsioon.
        laulupealkiri = grupp.artistiNimi.title() + "\t" + album.albumiNimi.title() + "\t" + aasta + "\t" + laul.lauluNimi.title()
        fail = open("albumid.txt", "a", encoding="UTF-8")
        # Lisab nimekirja uue plaadi andmed.
        fail.write("\n" + laulupealkiri)

        # Küsib, kas kasutaja soovib veel laule sisestada.
        b = input("Kas soovite veel laule lisada? jah/ei: ")
        if b == "jah":
            # Seis püsib aktiivne.
            seis = "aktiivne"
        else:
            # Seisu muutmine inaktiivseks.
            seis = "inaktiivne"
            fail.close()



# Kui vastus ei ole jah, siis liigub järgmise küsimuse juurde.
else:
    pass

fail = open("albumid.txt", encoding="UTF-8")
albumid = []

def albumiteKriipsud():
    for rida in fail:
        elemendid = rida.split("\t")
        esineja = artist(elemendid[0])
        album = albumA(elemendid[1])
        albumid.append(elemendid[1])
        aasta = elemendid[2]
        laul = laulA(elemendid[3])
        if len(albumid) > 1:
            if albumid[-2] != albumid[-1]:
                print()
                print("--------------------------------------------")
                print()
        print(esineja.artistiNimi, album.albumiNimi, aasta, laul.lauluNimi)




vastus = input("Kas soovite albumite nimekirja näha?: ")
if vastus == "jah":
    albumiteKriipsud()

fail.close()

