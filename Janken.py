print("Pour acceder au jeu merci d'inserer votre pseudo ou nom")
pseudo = input("qu'elle est votre nom?\n ->  ")



from random import choice
import json
print("bonjour",pseudo)
pfc = ("Pierre", "Feuille", "Ciseaux")


while input("Jouez (y/n): ").lower() != "n":

    print("\n------------------------------------")
    print("Choisissez un chiffre entre 0 et 2 sachant que Pierre>Ciseaux>Feuille>Pierre ")
    print("------------------------------------\n")

    a = int(input("Choisissez un chiffre:\n0: Pierre\n1: Feuille\n2: Ciseaux\n-> "))
    b = choice(range(3))

    print("\n{} VS {}".format(pfc[a], pfc[b]))
    if a == b:
        print("ÉGALITÉ\n")
        info = {pseudo : "ÉGALITÉ"}
        fichier = open("pseudoscore.json","a")
        fichier.write(json.dumps(info))
        fichier.close()
    elif (a>b and b+1==a) or (a<b and a+b==2):
        print("GAGNEZ\n")
        info = {pseudo : "GAGNEZ"}
        fichier = open("pseudoscore.json","a")
        fichier.write(json.dumps(info))
        fichier.close()
    else:
        print("PERDU\n")
        info = {pseudo : "PERDU"}
        fichier = open("pseudoscore.json","a")
        fichier.write(json.dumps(info))
        fichier.close()
else:
    def read():
        pseudoscore = []
        with open("pseudoscore.json") as f:
            data = json.load(f)
            for entrie in data:
                read.append(entrie["":""])
            return read
print(read)
