a = int(input("Nhap a: "))
b = int(input("Nhap b: "))

tong = a + b
print("Tong =", tong)

solonnhat = 0
temp = tong

while temp > 0:
    digit = temp % 10
    if digit > solonnhat:
        solonnhat = digit
    temp //= 10

print("Chu so lon nhat:", solonnhat)
