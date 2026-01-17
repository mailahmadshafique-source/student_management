from  student import student
from file_manager import filemanager

class studentmanager:
    def add_student(self, name, age,roll_no):
        students =filemanager.load_data()
        student=students(name, age,roll_no)
        student.append(student.to_dict())
        filemanager.save_data(student)

    def view_student(self):
        student = filemanager.load_data()
        for s in student:
            print(s)

    def delete_student(self,roll_no):
        students = filemanager.load_data()
        students=[s for s in students if s["roll no"] != roll_no]
        filemanager.save_data(student)

