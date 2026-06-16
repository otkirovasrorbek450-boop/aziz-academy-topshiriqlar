yigindi = 0
sanoq = 0
son = int(input())
while son != 0:
    yigindi += son
    sanoq += 1
    son = int(input())
if sanoq == 0:
    print(0)
else:
    print(yigindi / sanoq)