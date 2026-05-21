finput = open("input.txt", "r", encoding="utf-8")
fchu = open("outchu.txt", "w", encoding="utf-8")
fso = open("outso.txt", "w", encoding="utf-8")

for line in finput:
    for w in line.split():
        if w.isdigit():
            fso.write(w + "\n")
        else:
            fchu.write(w + " ")

finput.close()
fchu.close()
fso.close()