from StudentManagement import StudentManagement

students = StudentManagement()

while True:
    print("\n        Chuong Trinh Quan Ly Sinh Vien")
    print("     *******************************************************")
    print("     ** 1. Them sinh vien                                 **")
    print("     ** 2. Cap nhat sinh vien boi ID                      **")
    print("     ** 3. Xoa sinh vien boi ID                           **")
    print("     ** 4. Tim kiem sinh vien theo ten                    **")
    print("     ** 5. Sap xep sinh vien theo diem trung binh         **")
    print("     ** 6. Sap xep sinh vien theo ten                     **")
    print("     ** 7. Hien thi danh sach sinh vien                   **")
    print("     ** 0. Thoat chuong trinh                             **")
    print("     *******************************************************")

    key = int(input("Nhap tuy chon: "))
    if (key == 1):
        print("\nThem sinh vien.")
        students.addStudentToList()
        print("\nThem sinh vien thanh cong")
    elif (key == 2):
        if students.quantityStudent() > 0:
            ID = int(input("Nhap ID sinh vien: "))
            students.updateStudent(ID)
        else:
            print("Danh sach sinh vien rong.")
    elif (key == 3):
        if students.quantityStudent() > 0:
            ID = int(input("Nhap ID sinh vien can xoa: "))
            if students.deleteById(ID):
                print("Xoa sinh vien co ID", ID, " thanh cong.")
            else:
                print("Sinh vien co ID", ID, " khong ton tai!!")
        else:
            print("Danh sach sinh vien rong!!!")
    elif (key == 4):
        if students.quantityStudent() > 0:
            name = input("Nhap ten sinh vien can tim kiem: ")
            searchResult = students.findByName(name)
            students.showListStudent(searchResult)
        else:
            print("Danh sach sinh vien rong !!!")
    elif (key == 5):
        if students.quantityStudent() > 0:
            print("\nSinh vien duoc sap xep theo diem trung binh \n")
            students.sortByAvgScore()
            students.showListStudent(students.getListStudent())
        else:
            print("Danh sach sinh vien rong")
    elif (key == 6):
        if students.quantityStudent() > 0:
            print("\nSinh vien duoc sap xep theo ten \n")
            students.sortByName()
            students.showListStudent(students.getListStudent())
        else:
            print("Danh sach sinh vien rong")
    elif (key == 7):
        if students.quantityStudent() > 0:
            print("\nDanh sach sinh vien.")
            students.showListStudent(students.getListStudent())
        else:
            print("Dannh sach sinh vien rong !!!")
    elif (key == 0):
        print("Ban da thoat chuong trinh !!!")
        break
    else:
        print("\nKhong co chuc nang nay \nVui long chon chuc nang tron Menu")
