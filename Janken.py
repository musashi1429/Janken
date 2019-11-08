from random import choice
import json

# insert pseudo of player
print("Pour acceder au jeu merci d'inserer votre pseudo ou nom")
pseudo = input("qu'elle est votre nom?\n ->  ")

#print hi and pseudo and add variable of score and rock paper scisor.
print("bonjour",pseudo)
pfc = ("Pierre", "Feuille", "Ciseaux")
joueurscore = 0
iascore = 0

# add while for the game.The game can upload score and pseudo in json File.
while input("Jouez (y/n): ").lower() != "n":

    print("\n------------------------------------")
    print("Choisissez un chiffre entre 0 et 2 sachant que Pierre>Ciseaux>Feuille>Pierre ")
    print("------------------------------------\n")

    a = int(input("Choisissez un chiffre:\n0: Pierre\n1: Feuille\n2: Ciseaux\n-> "))
    b = choice(range(3))

    print("\n{} VS {}".format(pfc[a], pfc[b]))
# if choice is equal point is null.
    if a == b:
        print("EGALITE\n")
        info = {pseudo : "EGALITE"}
        fichier = open("pseudoscore.json","a")
        fichier.write(json.dumps(info))
        fichier.close()
#  if choice of player win add one point in joueurscore.
    elif (a>b and b+1==a) or (a<b and a+b==2):
        joueurscore += 1
        print("GAGNEZ\n")
        info = {pseudo : "GAGNEZ"}
        fichier = open("pseudoscore.json","a")
        fichier.write(json.dumps(info))
        fichier.close()
# if iascore choice win add one point in iascore
    else:
        iascore += 1
        print("PERDU\n")
        info = {pseudo : "PERDU"}
        fichier = open("pseudoscore.json","a")
        fichier.write(json.dumps(info))
        fichier.close()

# if somebody have 3 points first he win and the point become null for all.
    if joueurscore == 3 :
        print("vous ete arrivé a 3 point manche gagnante !!")
        iascore = 0
        joueurscore = 0
# if somebody have 3 points first he win and the point become null for all.
    if iascore == 3 :
        print("ia est arrivé a 3 point manche gagnante !!")
        iascore = 0
        joueurscore = 0

print("vous avez obtenu : ",joueurscore)
print("et l'ia a obtenu : ",iascore)


# def read():
#     pseudoscore = []
#     with open("pseudoscore.json") as f:
#         data = json.load(f)
#         for entrie in data:
#             read.append(entrie["":""])
#         return read
