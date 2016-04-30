# This Python file uses the following encoding: utf-8
DNA_koda = open("dna.txt", "r").read()

black_hair = "CCAGCAATCGC"
brown_hair = "GCCAGTGCCG"
carrot_hair = "TTAGCTATCGC"
square = "GCCACGG"
circle = "ACCACAA"
oval = "AGGCCTCA"
blue_eyes = "TTGTGGTGGC"
green_eyes = "GGGAGGTGGC"
brown_eyes = "AAGTAGTGAC"
male = "TGCAGGAACTTC"
female = "TGAAGGACCTTC"
white_skin = "AAAACCTCA"
black_skin = "CGACTACAG"
azin_skin = "CGCGGGCCG"

# Here we will check all the rapameters
print ("Black hair:", DNA_koda.find("CCAGCAATCGC"))
print ("Brown hair:", DNA_koda.find("GCCAGTGCCG"))
print ("Carrot hair:", DNA_koda.find("TTAGCTATCGC"))
print ("Sqare face:", DNA_koda.find("GCCACGG"))
print ("Circle face:", DNA_koda.find("ACCACAA"))
print ("Oval face:", DNA_koda.find("AGGCCTCA"))
print ("Blue eyes:", DNA_koda.find("TTGTGGTGGC"))
print ("Green eyes:", DNA_koda.find("GGGAGGTGGC"))
print ("Brown eyes:", DNA_koda.find("AAGTAGTGAC"))
print ("Male:", DNA_koda.find("TGCAGGAACTTC"))
print ("Female:", DNA_koda.find("TGAAGGACCTTC"))
print ("White skin:", DNA_koda.find("AAAACCTCA"))
print ("Black skin:", DNA_koda.find("CGACTACAG"))
print ("Azian skin:", DNA_koda.find("CGCGGGCCG"))

# Now, let's se only the important ones!
print ("Naš osumljenec ima:")
if DNA_koda.find("CCAGCAATCGC") > -1:
    print ("Black hair")
if DNA_koda.find("GCCAGTGCCG") > -1:
    print ("Brown hair")
if DNA_koda.find("TTAGCTATCGC") > -1:
    print ("Carrot hair")
if DNA_koda.find("GCCACGG") > -1:
    print ("Sqare face")
if DNA_koda.find("ACCACAA") > -1:
    print ("Circle face")
if DNA_koda.find("AGGCCTCA") > -1:
    print ("Oval face")
if DNA_koda.find("TTGTGGTGGC") > -1:
    print ("Blue eyes")
if DNA_koda.find("GGGAGGTGGC") > -1:
    print ("Green eyes")
if DNA_koda.find("AAGTAGTGAC") > -1:
    print ("Brown eyes")
if DNA_koda.find("TGCAGGAACTTC") > -1:
    print ("Male")
if DNA_koda.find("TGAAGGACCTTC") > -1:
    print ("Female")
if DNA_koda.find("AAAACCTCA") > -1:
    print ("White skin")
if DNA_koda.find("CGACTACAG") > -1:
    print ("Black skin")
if DNA_koda.find("CGCGGGCCG") > -1:
    print ("Azian skin")

# And now, let's wind out who is the guilty one :)
Ziga = "TGCAGGAACTTCAAAACCTCATTAGCTATCGCAAGTAGTGACACCACAA"
Matej = "TGCAGGAACTTCAAAACCTCACCAGCAATCGCTTGTGGTGGCAGGCCTCA"
Miha = "TGCAGGAACTTCAAAACCTCAGCCAGTGCCGGGGAGGTGGCGCCACGG"

if Ziga.find("GCCAGTGCCG") > -1:
    if Ziga.find("GCCACGG") > -1:
        if Ziga.find("GGGAGGTGGC") > -1:
            if Ziga.find("TGCAGGAACTTC") > -1:
                if Ziga.find("AAAACCTCA") > -1:
                    print ("Ziga JE pojedel sladoled)")
if Matej.find("GCCAGTGCCG") > -1:
    if Matej.find("GCCACGG") > -1:
        if Matej.find("GGGAGGTGGC") > -1:
            if Matej.find("TGCAGGAACTTC") > -1:
                if Matej.find("AAAACCTCA") > -1:
                    print ("Matej JE pojedel sladoled)")
if Miha.find("GCCAGTGCCG") > -1:
    if Miha.find("GCCACGG") > -1:
        if Miha.find("GGGAGGTGGC") > -1:
            if Miha.find("TGCAGGAACTTC") > -1:
                if Miha.find("AAAACCTCA") > -1:
                    print ("Miha JE pojedel sladoled)")
