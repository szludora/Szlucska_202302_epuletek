from Epulet import Epulet

epuletek = []


def beolvas(fajlnev):

    fajl = open(fajlnev, "r", encoding="utf-8")
    fajl.readline()
    sorok = fajl.readlines()
    fajl.close()

    i = 0
    while i < len(sorok):
        sor = sorok[i].strip().split("$")
        epulet = Epulet(sor)
        epuletek.append(epulet)
        i += 1


def epuletek_szama():
    return len(epuletek)


def magasabbmint():
    magasabb = 0
    i = 0
    while i < len(epuletek):

        if epuletek[i].magassag * 3.280839895 > 555:
            magasabb += 1
        i += 1

    return magasabb


def legoregebb_orszag():
    legoregebb = 99999
    oregorszag = "hiba"

    i = 0
    while i < len(epuletek):
        if epuletek[i].ev < legoregebb:
            legoregebb = epuletek[i].ev
            oregorszag = epuletek[i].orszag
        i += 1

    return oregorszag
