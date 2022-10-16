def start(length, unit):
    try:
        if unit == "cm":
            print(str(float(length) / 2.54))
        elif unit == "inch":
            print(str(float(length) * 2.54))
        else:
            print("Not correct unit!")
    except:
        print("Not valid values!")
if __name__ == '__main__':
    length = input("Adjon meg egy számot és egy mértékegységet (cm/inch):\n")
    unit = input()
    start(length, unit)
