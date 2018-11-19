from itertools import groupby
s=input()
for a,b in groupby(s):
    print(*[(len(list(b)), int(a))])
