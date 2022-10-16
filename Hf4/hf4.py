def start():
    try:
        while(1):
            a = input("Add meg 'a' értékét: ")
            b = input("Add meg 'b' értékét: ")
            c = int(a) / int(b)
            print(str(c))
    except ZeroDivisionError:
        print("Divide by zero is not allowed!")

if __name__ == "__main__":
    start()
