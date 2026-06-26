yil = int(input())
is_leap_vear = (yil % 4 == 0 and yil % 100 != 0) or (yil % 400 == 0)
print(is_leap_vear)