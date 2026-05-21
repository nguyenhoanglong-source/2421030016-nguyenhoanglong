n = int(input("Nhap n: "))

tong = 0
dem = 0

for i in range(n):
    x = float(input(f"x[{i}] = "))

    if 0 < x < 1000:
        tong += x
        dem += 1

if dem > 0:
    tbc = tong / dem
    print("Trung binh cong =", tbc)
else:
    print("Khong co phan tu thoa man")
