"""Paavo vinüülplaatide projekt

See programm aitab kasutajal saada ülevaadet oma vinüülplaatide kogumikust.
Samuti saab lisada vinüülplaate juurde ning otsida neid nime järgi.
"""

print("Tere, Paavo!")

# See rida küsib, et kas kasutaja soovib lisada nimekirja uut plaati.
b = input("Kas soovid lisada vinüülplaatide nimekirja albumit? jah/ei ")

"""Plaatide lisamine
----------------------------
Siin saab lisada nimekirja uusi vinüülplaate. Tuleb lisada esitaja, album,
aasta ning laul. Laulude küsimine toimub seni kuni while-tsükkel kestab.
----------------------------

Tingimuslause - if-statment
----------------------------
grupp : str
    esitaja/grupi nimi
album : str
    albumi nimi
aasta : str
    aasta
laul : str
    laulu nimi
"""

if b == "jah":
    seis = "aktiivne"
    grupp = input("Sisestage esitaja nimi: ")
    album = input("Sisestage albumi nimi: ")
    aasta = input("Sisestage aasta: ")
    # Tsükkel kestab kuni seis = aktiivne.
    while seis == "aktiivne":

        laul = input("Sisestage laulu pealkiri:")
        # Liidab kokku esitaja, albumi, aasta ning laulu. Vahel on tabulutsioon.
        laulupealkiri = grupp.title() + "\t" + album.title() + "\t" + aasta + "\t" + laul.title()
        fail = open("albumid.txt", "a", encoding="UTF-8")
        # Lisab nimekirja uue plaadi andmed.
        fail.write("\n" + laulupealkiri)

        # Küsib, kas kasutaja soovib veel laule sisestada.
        b = input("Kas soovite veel laule lisada? jah/ei")
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

# Küsib kas kasutaja soovib näha vinüülplaatide nimekirja.
y = input("Kas soovid näha vinüülplaatide nimekirja? jah/ei ")

# Avatakse fail ning salvestatakse informatsioon listi.
fail = open("albumid.txt", encoding="UTF-8")
albumid = []

"""Funktsioon albumiteKriipsud
------------------------------
Funktsioon - function
------------------------------
Antud funktsioon jagab vinüülplaatide informatsiooni osadeks.
Salvestatakse esineja, albumi, aasta ja laulu info eraldi.
Albumid lisatakse listi ning kui eelnev album ei ühine hetke albumiga,
siis pannakse vahele kriipsud.
"""


def albumiteKriipsud():
    for rida in fail:
        elemendid = rida.split("\t")
        esineja = elemendid[0]
        album = elemendid[1]
        albumid.append(album)
        aasta = elemendid[2]
        laul = elemendid[3]
        if len(albumid) > 1:
            if albumid[-2] != albumid[-1]:
                print()
                print("--------------------------------------------")
                print()
        print(rida)


# Kui kasutaja soovib näha plaatide nimekirja, siis kutsutakse ellu vastav funktsioon.
if y == "jah":

    albumiteKriipsud()

else:
    # Küsitakse kas kasutaja soovib otsida nimekirjast laulu.
    w = input("Kas soovid otsida laulu? jah/ei ")

    """
    Laulude otsimine
    --------------------------------
    Tingimuslause - if-statment
    --------------------------------
    Lisatakse plaatide informatsioon listi ning siis on võimalik soovitud
    lugu otsida.
    """

    if w == "jah":

        for rida in fail:
            albumid.append(rida)

        nimi = input("Sisesta albumi või artisti nimi: ")
        x = nimi.title()

        for str in albumid:
            if x in str:
                print(str)

    else:
        print("Ei soovinud midagi!")

fail.close()