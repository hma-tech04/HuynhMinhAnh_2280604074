from Student import Student


class StudentManagement:
    def __init__(self):
        self.listStudent = []

    def quantityStudent(self):
        return len(self.listStudent)

    def generateID(self):
        if self.quantityStudent() == 0:
            return 1
        return max(student._id for student in self.listStudent) + 1

    def addStudentToList(self):
        studentId = self.generateID()
        studentName = input("Nhập tên sinh viên: ")
        sex = input("Nhập giới tính sinh viên: ")
        major = input("Nhập ngành học của sinh viên: ")
        avgScore = float(input("Nhập điểm sinh viên: "))
        student = Student(studentId, studentName, major, sex, avgScore)
        self.rating(student)
        self.listStudent.append(student)

    def rating(self, student: Student):
        if student._avgScore >= 8.5:
            student._academicRanking = "Giỏi"
        elif student._avgScore >= 6.5:
            student._academicRanking = "Khá"
        elif student._avgScore >= 5:
            student._academicRanking = "Trung bình"
        else:
            student._academicRanking = "Yếu"

    def updateStudent(self, Id):
        student: Student = self.findByID(Id)
        if student is not None:
            student._name = input("Nhập tên sinh viên: ")
            student._sex = input("Nhập giới tính sinh viên: ")
            student._major = input("Nhập ngành học của sinh viên: ")
            student._avgScore = float(input("Nhập điểm sinh viên: "))
            self.rating(student)

    def findByID(self, ID):
        for student in self.listStudent:
            if student._id == ID:
                return student
        return None

    def sortByID(self):
        self.listStudent.sort(key=lambda x: x._id)

    def sortByName(self):
        self.listStudent.sort(key=lambda x: x._name.lower())

    def sortByAvgScore(self):
        self.listStudent.sort(key=lambda x: x._avgScore)

    def findByName(self, keyword):
        keyword = keyword.lower()
        return [student for student in self.listStudent
                if keyword in student._name.lower()]

    def deleteById(self, id):
        student = self.findByID(id)
        if student:
            self.listStudent.remove(student)
            print("Xóa sinh viên thành công!")
            return True
        print("Không tìm thấy sinh viên để xóa!")
        return False

    def showListStudent(self, student_list):
        if not student_list:
            print("Danh sách sinh viên trống!")
            return

        print(
            "{:<10} {:<20} {:<10} {:<20} {:<10} {:<15}".format(
                "ID", "Name", "Sex", "Major", "Avg Score", "Academic Rank"
            )
        )
        print("-" * 80)
        for student in student_list:
            print(
                "{:<10} {:<20} {:<10} {:<20} {:<10.2f} {:<15}".format(
                    student._id, student._name, student._sex,
                    student._major, student._avgScore, student._academicRanking
                )
            )

    def getListStudent(self):
        return self.listStudent
