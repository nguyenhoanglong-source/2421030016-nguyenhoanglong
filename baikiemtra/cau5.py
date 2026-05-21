m = int(input("Nhap m: "))
n = int(input("Nhap n: "))

tong = 0
temp = n

while temp > 0:
    tong += temp % 10
    temp //= 10

if tong != 0 and m % tong == 0:
    print(m, "chia het cho", tong)
else:
    print(m, "khong chia het cho", tong)
