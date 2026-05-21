def cau9():
    a = int(input("Nhap a: "))
    b = int(input("Nhap b: "))
    c = int(input("Nhap c: "))
    tong = a + b + c

    print("tong =", tong)

    dem = 0
    for i in str(tong):
        if int(i) % 2 == 0:
            dem += 1

    print("So chu so chan: ", dem)