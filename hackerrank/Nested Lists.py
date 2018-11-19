n=int(input())
python_studends=[]
python_studends2=[]
for x in range(n):
    students=[]
    name = input()
    score = float(input())
    students.append(name)
    students.append(score)
    python_studends.append(students)
maximum=max(python_studends)
for y in range(n):
    if python_studends[y]<maximum:
        python_studends2.append(python_studends[1])
maximum=max(python_studends2)
print(maximum[0])




