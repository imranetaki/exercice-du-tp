tab=[]
nbr_de_classe=int(input("entrer le nbr d'élève : "))
for i in range (0,nbr_de_classe) :
    note=int(input(f"enter la note numéro {i+1} : "))
    tab.append(note)

for i in range(0,nbr_de_classe) :
    if tab[i] > 10 :
        print(tab[i],end=" ")