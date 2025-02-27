def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]
input_String = input("Moi ban nhap chuoican dao nguoc: ")
print("Chuoi sau khi duoc dao nguoc la: ", dao_nguoc_chuoi(input_String))