a = "Szárad a darázs."
ekezet = ["á", "é", "í", "ó", "ö", "ő", "ú", "ü", "ű", ".", ",", "-", " ", "?", "!", ":"]
csere = ["a", "e", "i", "o", "o", "o", "u", "u", "u", "", "", "", "", "", "", ""]
a = a.lower()
for i in range(len(ekezet)):
    a = a.replace(ekezet[i], csere[i])
b = list(a)
c = list(a)[::-1]
dupla = ["ny", "sz", "ty", "gy", "zs", "dzs", "ssz", "ggy", "tty", "cs", "ccs", "ly"]
dupla2 = ["yn", "zs", "yt", "yg", "sz", "szd", "zss", "ygg", "ytt", "sc", "scc", "yl"]
for i in range(len(b)-1):
    for y in range(len(dupla)):
        if b[i]+b[i+1] == dupla[y]:
            print(b[i]+b[i+1])
            temp = list(dupla2[y])
            b[i] = temp[0]
            b[i+1] = temp[1]
            break
b = b[::-1]
if ''.join(b) == a or ''.join(c) == a:
    print("This is a palindrom")
else:
    print("This is not a palindrom")
