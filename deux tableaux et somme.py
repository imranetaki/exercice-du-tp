tab1=[]
tab2=[]
N=int(input("entrer la meme taille des 2 tableux : "))
for i in range (0,N) :
    x=int(input(f"enter l'element numéro {i+1} du tableau num 1 : ")) 
    tab1.append(x)
for j in range (0,N) :
    y=int(input(f"enter l'element numéro {j+1} du tableau num 2 : ")) 
    tab2.append(y)
print(tab1)
print(tab2)
tab=[]
for z in range (0,N) :
    tab.append(tab1[z]+tab2[z])
print("la somme des deux elements de chaque tab est : " ,tab)

