from  student import student
from file_manager import FileManager

class StudentManager:
    def add_student(self, name, age,roll_no):

        students =FileManager.load_data()
        student=students(name, age,roll_no)
        students.append(student.to_dict())
        FileManager.save_data(students)

    def view_student(self):
        students = FileManager.load_data()
        for s in students:
            print(s)

    def delete_student(self,roll_no):
        students = FileManager.load_data()
        students=[s for s in students if s["roll_no"] != roll_no]
        FileManager.save_data(students)

