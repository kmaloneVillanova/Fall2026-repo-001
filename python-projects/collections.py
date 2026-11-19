lst=[10,20,30,40,50]
print(lst)

lst.append(5)
lst.append(6)
lst.append(7)
print(lst)

lst.remove(5)
print(lst)

lst.pop(3)
print(lst)
lst.pop()

lst.reverse()
print(lst)

lst.sort()
print(lst)

newlst=lst[1:]
print(newlst)

lst.append(20)
lst.append(20)
print(lst)

count20=lst.count(20)
print(count20)

index20=lst.index(20)
print(index20)

cpylst=lst
print(cpylst)

cpylst[0]=999
print(cpylst)
print(lst)

cpylst=lst.copy()
cpylst=lst[:]

cpylst[-1]=999
print(cpylst)
print(lst)

empty=[]
for val in lst:
    if val >= 20 and val <= 50:
        empty.append(val)

print(empty)

empty=[1]*10
print(empty)
empty[0]=10
print(empty)

squares=[]
for i in range(1,10):
    squares.append(i*i)
print(squares)

print(lst)
newlst=[val for val in lst if val>=20 and val<=50]
print(newlst)

aset=set()
aset={1,2,3,3,3,2}
print(aset)
aset.add(5)


fav_foods={'kathleen': 'pizza', 'steve':'burgers','john':'steak',
           'michelle':'pasta','pat':'burgers'}
print(fav_foods)
favfood=fav_foods['kathleen']
print(favfood)

if 'bob' in fav_foods:
    print(fav_foods['bob'])
else:
    fav_foods['bob']="ice cream"
print(fav_foods)

# print(fav_foods['george'])

for key,value in fav_foods.items():
    print(key,value)