def tinh_tong_so_chan(list):
    tong = 0
    for i in list:
        if i % 2 == 0:
            tong += i
    return tong

input_list = input("Nhap danh sach cac so, cach nhau boi dau phay: ")
nums = list(map(int, input_list.split(',')))

tong_chan = tinh_tong_so_chan(nums)
print("Tong cac so chan trong list la: ", tong_chan)