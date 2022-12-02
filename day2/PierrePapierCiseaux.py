



def monScore():

    scoreTotal = 0
    fichier = open("donnees.txt","r")
    for ligne in fichier:

        
        coupAdverse = ligne[0]
        monCoup = ligne[2]

        if (coupAdverse == "A"):
            coupAdverse = 1

        elif(coupAdverse == "B"):
            coupAdverse = 2

        else:
            coupAdverse = 3
    
    """ 
    --- Exercice 1 ---

        if (monCoup == "X"):
            monCoup = 1

        elif (monCoup == "Y"):
            monCoup = 2

        else: 
            monCoup = 3

        if (coupAdverse == monCoup):
            scoreTotal += monCoup + 3
        elif (monCoup == 3):
            if (coupAdverse == 1):
                scoreTotal += 0 + monCoup
            elif (coupAdverse == 2):
                scoreTotal += 6 + monCoup
        elif (monCoup == 1):
            if (coupAdverse == 2):
                scoreTotal += 0 + monCoup
            elif (coupAdverse == 3):
                scoreTotal += 6 + monCoup
        elif (monCoup == 2):
            if (coupAdverse == 3):
                scoreTotal += 0 + monCoup
            elif (coupAdverse == 1):
                scoreTotal += 6 + monCoup

    print(scoreTotal)

    """

        
        


monScore()
