n = int(input())
list = []
list2 = []
if n>1:
    for x in range(n):
        value = int(input())
        list.append(value)
    maxi = max(list)
    for i in list:
        if (i<maxi):
            list2.append(i)
    runnerup = max(list2)
    print(runnerup)
else:
    print("please enter above 1")



