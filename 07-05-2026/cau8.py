def cau7():
    n = int(input("Nhap n = "))
    while n > 100 or n < 0:
        n = int(input("Nhap n (0 < n < 100): "))

    tong = 0
    for i in range(n):
        x = int(input("Nhap phan tu thu %d: " % (i + 1)))
        kt = True
        if x < 2:
            kt = False
        else:
            for j in range(2, int(x ** 0.5) + 1):
                if x % j == 0:
                    kt = False
        if kt == True:
            tong = tong + x

    print("Tong cac so nguyen to la: ", tong)

    if tong % 2 != 0 and tong > 50:
        print("Tong la so le va lon hon 50")
    else:
        print("Tong khong la so le va lon hon 50")

def cau8():
    x = int(input("Nhap x: "))
    y = int(input("Nhap y: "))
    z = int(input("Nhap z: "))
    tich = x * y * z

    print("Tich =", tich)

    dem = 0
    max = 0 

    while tich > 0:
        cs = tich % 10
        dem = dem + 1
        if cs > max:
            max = cs
        tich = tich // 10

    print("So chu so =", dem)
    print("chu so lon nhat =", max)

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