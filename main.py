from student_manager import studentmanager
print("student management system")
manager = studentmanager()
while true:
    print("1.add student")
    print("2.view student")
    print("3.delete student")
    print("4.exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        r=input("roll no: ")
        n=input("student name: ")
        a=input("age: ")
        manager.add_student(r,n,a)
    elif choice == "2":
        manager.view_student()
    elif choice == "3":
        manager.delete_student()
    elif choice == "4":
        print("exit")
        break


