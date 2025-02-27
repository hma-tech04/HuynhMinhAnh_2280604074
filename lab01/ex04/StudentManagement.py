from Student import Student

class StudentManagement:
    listStudent = []

    def quantityStudent(self):
        return self.listStudent.__len__
    
    def generateID(self):
        maxID = 1
        if(self.quantityStudent() > 0):
            maxID = self.listStudent[0]._id
            for item in self.listStudent:
                if(maxID < item._id):
                    maxID = item._id
            maxID = maxID + 1
        return maxID
    
    def addStudentToList(self):
        studentId = self.generateID()
        studentName = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh sinh vien: ")
        major = input("Nhap nganh hoc cua sinh vien: ")
        avgScore = float(input("Nhap diem sinh vien: "))
        student = Student(studentId, studentName, sex, major, avgScore)
        self.rating(student)
        self.listStudent.append(student)

    def rating(self, student:Student):
        if student._agvScore >= 8.5:
            student._study = "Gioi"
        elif student._agvScore >= 6.5:
            student._study = "Kha"
        elif student._agvScore >= 5:
            student._study = "Trung binh"
        else:
            student._study ="Yeu"

    def updateStudent(self, Id):
        student:Student = self.findByID()
        if student != None:
            studentName = input("Nhap ten sinh vien: ")
            sex = input("Nhap gioi tinh sinh vien: ")
            major = input("Nhap nganh hoc cua sinh vien: ")
            avgScore = float(input("Nhap diem sinh vien: "))
            student._name = studentName
            student._major = major
            student._sex = sex
            student._avgScore = avgScore
            student._study = self.rating(student)

    def findByID(self, ID):
        searchResult = None
        if (self.quantityStudent() > 0):
            for item in self.listStudent:
                if item._id == ID:
                    searchResult = item
        return searchResult
    
    def sortByID(self):
        self.listStudent.sort(key=lambda x: x._id, reverse=False)

    def sortByName(self):
        self.listStudent.sort(key=lambda x: x._name, reverse=False)

    def sortByAvgScore(self):
        self.listStudent.sort(key=lambda x: x._avgScore, reverse=False)





        