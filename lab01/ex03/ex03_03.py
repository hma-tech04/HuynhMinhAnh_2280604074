def tao_tuple_tu_list(list):
    return tuple(list)
input = input("Nhap danh sach cac so, cach nhau boi dau phay: ")
nums = list(map(int, input.split(',')))
print("List: ", nums)
print("Tuple tu list: ", tao_tuple_tu_list(nums))

