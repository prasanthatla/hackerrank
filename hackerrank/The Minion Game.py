
def minion(string):
    list = [st for st in string]
    l = len(list)
    vowels = ['A','E','I','O','U']
    consonants = ['Q','W','R','T','Y','P','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
    firstletters = []
    secondletters = []
    word = [list[i:j+1] for i in range(l)for j in range(i, l)]
    for list in word:
        if list[0] in vowels:
            firstletters.append(list)
    for list in word:
        if list[0] in consonants:
            secondletters.append(list)
    if len(firstletters) == len(secondletters):
        print("DRAW")
    if len(firstletters) > len(secondletters):
        print("Stuart",len(firstletters))
    if len(firstletters) < len(secondletters):
        print("binny",len(secondletters))


str = input()
minion(str)
