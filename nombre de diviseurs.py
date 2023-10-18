n=int(input("entrer un entier svp : "))
div=0
for i in range(1,n+1):
    if n % i ==0 :
        print(i)
        div=div+1
print("le nombre des diviseurs est : ", div)