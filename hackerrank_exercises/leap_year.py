def is_leap(year):
    leap = False
    if (year % 4 != 0):
        return False
    if (year % 100 == 0 and year % 400 != 0):
        return False
    else:
        return True

year = int(input())
