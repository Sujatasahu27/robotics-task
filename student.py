students = {}

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        roll = input("Enter Roll No: ")
        name = input("Enter Name: ")
        students[roll] = name

    elif choice == 2:
        for roll, name in students.items():
            print("Roll:", roll, "Name:", name)

    elif choice == 3:
        break

    else:
        print("Invalid Choice")