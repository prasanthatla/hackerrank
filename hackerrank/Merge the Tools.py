s=str(input())
k=int(input())
l=int(len(s)/k)
for x in range(l):
    list=((s[x*k : (x+1)*k]))
    print(''.join([j for i,j in enumerate(list) if j not in list[:i]]))