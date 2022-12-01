#Python

def nbLignes(fichier):

    nbLignes = len(fichier.readlines())

    return nbLignes

def maxDansListe(li):

    max = 0

    for nb in li:
        if (nb > max):
            max = nb
    
    return max

def maxDansListeEtLeRetire(li):

    max = 0
    indiceDeMax = 0

    for i in range(0, len(li) - 1):
        if (li[i] > max):
            max = li[i]
            indiceDeMax = i

    li.pop(indiceDeMax)
    return max

# MAIN

fichier = open("elvesItems.txt","r");
sommeParElfes = 0
caloriesParElfes = []

for ligne in fichier:

    if(ligne != "\n"):
        ligne = ligne[:-1]
        sommeParElfes += int(ligne)
        
        #sommeParElfes += int(ligne)
    else:
        caloriesParElfes.append(sommeParElfes)
        sommeParElfes = 0


top1 = maxDansListeEtLeRetire(caloriesParElfes)
print("top 1 : " + str(top1))
top2 = maxDansListeEtLeRetire(caloriesParElfes)
print("top 2 : " + str(top2))
top3 = maxDansListeEtLeRetire(caloriesParElfes)
print("top 3 : " + str(top3))

print(top1 + top2 + top3)





