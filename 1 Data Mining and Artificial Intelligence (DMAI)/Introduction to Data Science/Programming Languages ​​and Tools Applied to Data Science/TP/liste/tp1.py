x = 0
while(x<1 or x>10):
    x=int(input("entrer un nombre entier entre 1 et 10 : "))
print(x)
L = []
for i in range(0,101):
    if i%x==0:
        L.append(i)
print(L)