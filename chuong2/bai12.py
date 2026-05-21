tong = 0

while True:
    n = int(input("Nhap n hoac 0 de thoat: "))

    if n == 0:
        break
    if n % 2 == 0:
        tong = tong + n

print(tong)
