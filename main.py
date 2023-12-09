chis1 = "348x79643"
chis2 = "16x52"
chis3 = "43x7"
p = 23
krat = 12
num1 = list(chis1)
num2 = list(chis2)
num3 = list(chis3)
num1.reverse()
num2.reverse()
num3.reverse()
walve1 = 0
walve2 = 0
walve3 = 0
ans = 0
for x in range(p-1, -1, -1):
    walve1 = 0
    walve2 = 0
    walve3 = 0
    for i in range(len(num1)):
        t = num1[i]
        if t == "x":
            t = x
        t = int(t)
        walve1 += t * (p**i)
    for i in range(len(num2)):
        t = num2[i]
        if t == "x":
            t = x
        t = int(t)
        walve2 += t * (p**i)
    for i in range(len(num3)):
        t = num3[i]
        if t == "x":
            t = x
        t = int(t)
        walve3 += t * (p**i)
    ans = walve1 + walve2 + walve3
    if ans % krat == 0:
        print(x)
        break