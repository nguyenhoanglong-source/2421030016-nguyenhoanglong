a=[]
n=int(input("Nhap so phan tu cua day so: "))

for i in range(1,n+1):
    k=int(input("Nhap phan tu thu " + str(i) + ":"))
    a.append(k)

for i in a:
    print("Luy thua cua 2 so do:", str(i*i))
