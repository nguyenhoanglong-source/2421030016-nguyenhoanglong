m=int(input("Nhap m="))
n=int(input("Nhap n="))
a=[]

for i in range(0,m):
    a.append([])
    for j in range(0,n):
        x = float(input("Nhap phan tu thu a[%d][%d]: " % (i+1,j+1)))
        a[i].append(x)

print("Mang vua nhap la: ")

for i in range(0,m):
    for j in range(0,n):
        print("%8.2f " % a[i][j], end='')
    print