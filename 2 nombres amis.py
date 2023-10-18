n=int(input("entrer la valeur de n svp "))
s=0
while n<= 0:
    n=int(input("entrer la valeur de n"))
print("les diviseurs sont : ")
for i in range (2,n) :
    if (n % i == 0 ) : 
        print (i,end=" ")
        s=s+i
print()
print("la somme des diviseurs est ",s)
print()

n1=int(input("entrer la valeur de n svp "))
s1=0
while n1<= 0:
    n1=int(input("entrer la valeur de n"))
print("les diviseurs sont : ")
for j in range (2,n1) :
    if (n1 % j == 0 ) : 
        print (j,end=" ")
        s1=s1+j
print()
print("la somme des diviseurs est :",s1)
if n==s1 and n1==s:
    print("les deux nombres sont amis ")
else :
    print("les deux nombres ne sont pas amis ")
