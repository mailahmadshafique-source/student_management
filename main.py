from student_manager import StudentManager
def main():
 manager = StudentManager()
 while True:
    print("1.add student")
    print("2.view student")
    print("3.delete student")
    print("4.exit")
    choice = int(input("Enter your choice: "))
    if choice == "1":
        r=input("roll no: ")
        n=input("student name: ")
        a=input("age: ")
        manager.add_student(r,n,a)
        print("student added successfully")
    elif choice == "2":
        manager.view_student()
    elif choice == "3":
        roll_no=input("enter roll no to delete:")
        manager.delete_student(roll_no)
        print("student deleted successfully")
    elif choice == "4":
        print("exit")
        break
    else:
        print("invalid choice")



