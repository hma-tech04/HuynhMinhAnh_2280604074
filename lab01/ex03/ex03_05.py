def dem_so_lan_xuat_hien(list):
    count_dict = {}
    for item in list:
            if item in count_dict:
                count_dict[item] += 1
            else:
                 count_dict[item] = 1
    return count_dict

inputStr = input("Nhap danh sach ca tu, cah nhau boi dau cach: ")
word_list = inputStr.split()

so_lan_XH = dem_so_lan_xuat_hien(word_list)
print("So lan xuat hien cua cac phan tu: ", so_lan_XH)