n = int(input("Nhap n: "))

tich = 1
temp = n

while temp > 0:
    tich *= temp % 10
    temp //= 10

if tich % 2 == 0 and tich > 20:
    print("Dung")
else:
    print("Sai")
