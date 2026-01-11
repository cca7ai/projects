L = [0,1,2,3,4,5,6,7,8,9]
#L = [x+1 for x in L]
for x in L:
    x = x+1
L.append(11)
L.extend([12,13])
print(L[0])
print(L[0:2])
print(L[-1])
print(L[-2:])
LP = []
LI = []
for x in L:
    if x%2==0:
        LP.append(x)
    else:
        LI.append(x)
print(LP)
print(LI)
index_4 = L.index(4)
L.insert(index_4,3.5)
L.remove(3.5)
L.reverse()
print(L)
k = int(input("Entrez un nombre :"))
if k in L:
    print(k," se trouve dans L, à la ",L.index(k)," position")
else:
    print(k," n'est pas present dans L")