#54-59,17-62


def part1InclusDansPart2(debutPart1,finPart1,debutPart2,finPart2):
    
    if(debutPart1 >= debutPart2 and finPart1 <= finPart2):
        return True
    else:
        return False

def part2InclusDansPart1(debutPart1,finPart1,debutPart2,finPart2):
    
    if(debutPart2 >= debutPart1 and finPart2 <= finPart1):
        return True
    else:
        return False


def part1ChevaucheDansPart2(debutPart1,finPart1,debutPart2,finPart2):
    
    if(finPart1 >= debutPart2 and debutPart1 <= finPart2):
        return True
    else:
        return False

def part2ChevaucheDansPart1(debutPart1,finPart1,debutPart2,finPart2):
    
    if(finPart2 >= debutPart1 and debutPart2 <= finPart1):
        return True
    else:
        return False


fichier = open("data.txt","r")
compteur = 0
for ligne in fichier:
    ligne.strip()
    part1 = ligne[:(ligne.find(","))]
    part2 = ligne[(ligne.find(",") + 1):]

    debutPart1 = int(part1[:(part1.find("-"))])
    finPart1 = int(part1[(part1.find("-") + 1):])

    debutPart2 = int(part2[:(part2.find("-"))])
    finPart2 = int(part2[(part2.find("-") + 1):])

    """if(part1InclusDansPart2(debutPart1,finPart1,debutPart2,finPart2) or part2InclusDansPart1(debutPart1,finPart1,debutPart2,finPart2)):
        print("ligne : " + ligne)
        compteur += 1
        print("compteur : " + str(compteur))
        print()"""
    if(part1ChevaucheDansPart2(debutPart1,finPart1,debutPart2,finPart2) or part2ChevaucheDansPart1(debutPart1,finPart1,debutPart2,finPart2)):
        
        print("ligne : " + ligne)
        compteur += 1
        print("compteur : " + str(compteur))
        print()
        
    




