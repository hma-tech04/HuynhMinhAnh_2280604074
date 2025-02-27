def truy_cap_phan_tu(tuple_data):
    first_Element = tuple_data[0]
    last_Element = tuple_data[-1]
    return first_Element, last_Element

input = eval(input("Nhap tuple, vi du (1, 2, 3)"))
first, last = truy_cap_phan_tu(input)

print("So dau tien la : ", first)

print("So cuoi cung la : ", last)