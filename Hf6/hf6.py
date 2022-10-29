print("\t", end="")
for i in range(1,13):
    print('%5i' % i, end="")
print("\n :--------------------------------------------------------------")
for i in range(1,13):
    print(str(i) + ":\t", end="")
    for y in range(1,13,2):
        print('%5i' % (i*y), '%4i' % (i*(y+1)), end="")
    print("\n")
