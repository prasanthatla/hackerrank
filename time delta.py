from datetime import datetime
number=int(input())
for x in range(number):
    t1=datetime.strptime(input(),'%a %d %b %Y %H:%M:%S %z')
    t2=datetime.strptime(input(),'%a %d %b %Y %H:%M:%S %z')
    # datetime.now()
    print (int(abs((t1-t2).total_seconds())))