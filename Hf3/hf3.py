def start():
    print("Adja meg a háromszög három cm-ben:")
    a = int(input("a oldal (cm): "))
    b = int(input("b oldal (cm): "))
    c = int(input("c oldal (cm): "))
    if ((a + b) >= c and (b + c) >= a and (a + c) >= b):
        print("A " + str(a) + ", " + str(b) + " és " + str(c) + " oldalú háromszög szerkeszthető.")
    else:
        print("A " + str(a) + ", " + str(b) + " és " + str(c) + " oldalú háromszög NEM szerkeszthető.")
if __name__ == '__main__':
    start()
