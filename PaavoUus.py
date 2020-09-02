class laul():
    def __init__(self, lauluNimi):
        self.lauluNimi = lauluNimi

class artist():
    def __init__(self, artistiNimi):
        self.artistiNimi = artistiNimi

class album():
    def __init__(self, albumiNimi):
        self.albumiNimi = albumiNimi

fail = open("albumid.txt", encoding="UTF-8")
albumid = []

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

vastus = input("Kas soovite albumite nimekirja näha?: ")
if vastus == "jah":
    albumiteKriipsud()

fail.close()

