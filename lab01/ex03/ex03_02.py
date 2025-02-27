def dao_nguoc(list):
    return list[::-1]

input = input("Nhap danh sach cac so, cach nhau boi dau phay: ")
nums = list(map(int, input.split(',')))
print("List sau khi dao nguoc la: ", dao_nguoc(nums))


