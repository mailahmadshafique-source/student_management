import json
import os

class StudentManager:
     def __init__(self,filename="students.json"):
         self.filename = filename
         self.students = []
         self.load_students()
     def load_students(self):
         if os.path.exists(self.filename):
             with open(self.filename,"r",encoding="utf-8") as f:
                 try:
                     self.students = json.load(f)
                 except json.decoder.JSONDecodeError:
                     self.students = []
                 else:
                     self.students=[]
     def save_students(self):
         with open(self.filename,"w",encoding="utf-8") as f:
             json.dump(self.students,f,indent=4)
     def add_student(self,student_id,name,age):
         student={
             "id":student_id,
             "name":name,
             "age":age
         }
         self.students.append(student)
         self.save_students()
     def show_students(self):
         for student in self.students:
             print(student)
     def delete_student(self,student_id):
         self.students=[
             student for student in self.students
             if student["id"]!=student_id
         ]
         self.save_students()

