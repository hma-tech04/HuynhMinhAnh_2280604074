def kiem_tra_so_NT(n):
    if n < 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
number = int(input("Nhap so can kiem tra vao: "))
if kiem_tra_so_NT(number):
    print("La so nguyen to")
else:
    print("Khong phai la so nguyen to")