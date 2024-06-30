


def demander_nom():
    nom = ''
    while nom == '':
        nom = input("Entre votre nom espèce de fainéant")
        try:
            int(nom)
            print("C'est une erreur, re essaye")
            nom = ''
        except:
             print("C'est une erreur, re essaye")
    return nom

name_asked = demander_nom()

print(name_asked)