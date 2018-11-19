def is_leap(year):
    leap = False

    if (year%4)==0:
        if (year%100)==0:
            if (year%400)==0:
                print("leaf year")
            else:
                print("it is not leaf year")
        else:
            print("it is not leaf year")

    else:
        print("it not leaf year")


year = int(input())
print(is_leap(year))