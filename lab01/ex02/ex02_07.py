print("Nhap ca dong van ban (Nhap 'done' de ket thuc): ")
lines = []
while True:
    line = input();
    if line.lower() == 'done':
        break
    lines.append(line)
print("\n Cac dong da nhap sau khi duoc chuyen thanh chu in hoa: ")
for i in lines:
    print(i.upper())