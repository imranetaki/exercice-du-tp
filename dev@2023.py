essaie = 0
max=3 
mdp="dev@2023"
ques="film préféré"
reponse="interstellar"

while essaie<max :
    x=input("entrer le mot de passe svp : ")
    if x==mdp :
        print("bonjour")
        break
    essaie+=1

    if essaie==max :
        y=input("répondez à la question secrète ")
        if y==reponse :
            print("bonjour")
            break
        else :
            print("vous avez apuisé tous les chances")

