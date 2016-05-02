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
azian_skin = "CGCGGGCCG"

# Here we will check all the rapameters
print ("Black hair:", DNA_koda.find(black_hair))
print ("Brown hair:", DNA_koda.find(brown_hair))
print ("Carrot hair:", DNA_koda.find(carrot_hair))
print ("Sqare face:", DNA_koda.find(square))
print ("Circle face:", DNA_koda.find(circle))
print ("Oval face:", DNA_koda.find(oval))
print ("Blue eyes:", DNA_koda.find(blue_eyes))
print ("Green eyes:", DNA_koda.find(green_eyes))
print ("Brown eyes:", DNA_koda.find(brown_eyes))
print ("Male:", DNA_koda.find(male))
print ("Female:", DNA_koda.find(female))
print ("White skin:", DNA_koda.find(white_skin))
print ("Black skin:", DNA_koda.find(black_skin))
print ("Azian skin:", DNA_koda.find(azian_skin))

# Now, let's se only the important ones!
print ("Naš osumljenec ima:")
if DNA_koda.find(black_hair) > -1:
    print ("Black hair")
if DNA_koda.find(brown_hair) > -1:
    print ("Brown hair")
if DNA_koda.find(carrot_hair) > -1:
    print ("Carrot hair")
if DNA_koda.find(square) > -1:
    print ("Sqare face")
if DNA_koda.find(circle) > -1:
    print ("Circle face")
if DNA_koda.find(oval) > -1:
    print ("Oval face")
if DNA_koda.find(blue_eyes) > -1:
    print ("Blue eyes")
if DNA_koda.find(green_eyes) > -1:
    print ("Green eyes")
if DNA_koda.find(brown_eyes) > -1:
    print ("Brown eyes")
if DNA_koda.find(male) > -1:
    print ("Male")
if DNA_koda.find(female) > -1:
    print ("Female")
if DNA_koda.find(white_skin) > -1:
    print ("White skin")
if DNA_koda.find(black_skin) > -1:
    print ("Black skin")
if DNA_koda.find(azian_skin) > -1:
    print ("Azian skin")

# And now, let's wind out who is the guilty one :)
# Ziga = "TGCAGGAACTTCAAAACCTCATTAGCTATCGCAAGTAGTGACACCACAA"
# Matej = "TGCAGGAACTTCAAAACCTCACCAGCAATCGCTTGTGGTGGCAGGCCTCA"
# Miha = "TGCAGGAACTTCAAAACCTCAGCCAGTGCCGGGGAGGTGGCGCCACGG"
#
# if (Ziga.find("GCCAGTGCCG") > -1 and Ziga.find("GCCACGG") > -1):
#    if (Ziga.find("GGGAGGTGGC") > -1 and Ziga.find("TGCAGGAACTTC") > -1 and Ziga.find("AAAACCTCA") > -1):
#       print ("Ziga JE pojedel sladoled.")
# if (Matej.find("GCCAGTGCCG") > -1 and  Matej.find("GCCACGG") > -1 and Matej.find("GGGAGGTGGC") > -1):
#    if (Matej.find("TGCAGGAACTTC") > -1 and Matej.find("AAAACCTCA") > -1):
#        print ("Matej JE pojedel sladoled.")
# if (Miha.find("GCCAGTGCCG") > -1 and Miha.find("GCCACGG") > -1 and Miha.find("GGGAGGTGGC") > -1):
#    if (Miha.find("TGCAGGAACTTC") > -1 and Miha.find("AAAACCTCA") > -1):
#        print ("Miha JE pojedel sladoled.")

Ziga = str(male + white_skin + carrot_hair + brown_eyes + circle)
Matej = str(male + white_skin + black_hair + blue_eyes + oval)
Miha = str(male + white_skin + brown_hair + green_eyes + square)

if (Ziga.find(male) > -1 and Ziga.find(white_skin) > -1):
    if (Ziga.find(brown_hair) > -1 and Ziga.find(green_eyes) > -1 and Ziga.find(square) > -1):
        print ("Ziga JE pojedel sladoled.")
if (Matej.find(male) > -1 and  Matej.find(white_skin) > -1 and Matej.find(brown_hair) > -1):
    if (Matej.find(green_eyes) > -1 and Matej.find(square) > -1):
        print ("Matej JE pojedel sladoled.")
if (Miha.find(male) > -1 and Miha.find(white_skin) > -1 and Miha.find(brown_hair) > -1):
    if (Miha.find(green_eyes) > -1 and Miha.find(square) > -1):
        print ("Miha JE pojedel sladoled.")


