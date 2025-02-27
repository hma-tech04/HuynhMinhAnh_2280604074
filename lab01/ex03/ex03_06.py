def xoa_phan_tu(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False
    
my_dict = {'a' : 1, 'b': 2, 'c': 3, 'd': 4}
keyDel = 'b'
res = xoa_phan_tu(my_dict, keyDel)
if res:
    print("Phan tu duoc xoa tu dictK: ", my_dict )
else:
    print("Khong tim thay phan tu can xoa")
    