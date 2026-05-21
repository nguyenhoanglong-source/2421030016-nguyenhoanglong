toan = float(input("Nhap diem toan: "))
ly = float(input("Nhap diem ly: "))
hoa = float(input("Nhap diem hoa: "))

tb = (toan + ly + hoa) / 3
print("Diem trung binh:", tb)

if tb < 5:
    print("Xep loai Yeu")

if tb >= 5 and tb < 7:
    print("Xep loai Trung Binh")

if tb >= 7 and tb < 9:
    print("Xep loai Kha")

if tb >=9:
    print("Xep loai gioi")
