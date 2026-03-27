weight = [2,3,4,4,5,6,1,2,2,2,1,8,2]

y=0
list = []
y=0
for i in weight:
    if i%2 == 0:
        y+= i
    if 1 %2 == 1:
        list.append(y)
        y=0
    print((list))