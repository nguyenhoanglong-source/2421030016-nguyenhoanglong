n = int(input("Nhap n="))
dem = 0

for i in range(1, n):
    if n % i == 0:
        dem += 1

print(dem)
