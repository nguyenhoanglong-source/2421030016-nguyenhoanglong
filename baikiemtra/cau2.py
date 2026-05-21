n = int(input("Nhap n: "))

tong = 0
temp = n

while temp > 0:
    tong += temp % 10
    temp //= 10

if tong % 3 == 0:
    print("Tong chu so chia het cho 3")
else:
    print("Tong chu so khong chia het cho 3")
