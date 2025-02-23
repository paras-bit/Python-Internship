def leapyear(n):
    if (n%4==0 and n%100!=0) or (n%400==0):
        return "leap year"
    else:
        return "not leap year"

print(leapyear(2007))