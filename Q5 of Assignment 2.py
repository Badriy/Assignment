a = [23,54,76,12,90]
for i in range(len(a)):
    if (i == len(a) -1):
        print(a[i], end="")
    else:
        print(a[i], end=" | ")
