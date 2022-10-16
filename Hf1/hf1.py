from collections import Counter

def start():
    szoveg = input("Adjon meg egy mondatot:\n")
    gyakorisag = dict(Counter(szoveg))
    print("Betűk gyakorisága: " + str(gyakorisag))
    reverse = szoveg[::-1]
    print("Fordítva: " + reverse)
    rendezve = szoveg.split(" ")
    print("Listába rendezve szavanként: " + str(rendezve))

if __name__ == '__main__':
    start()
