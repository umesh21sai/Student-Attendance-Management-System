#Student Attendance Management System
import json

class Student:
    def __init__(self,name,roll_number):
        self.name=name
        self.roll_number=roll_number
        self.attendance={}

    def mark_attendance(self,attendance_date,status):
        if status not in ("Present","Absent"):
            print("Invalid Status")
            return

        if attendance_date in self.attendance:
            print("Attendance already recorded!")
            return

        self.attendance[attendance_date]=status
        print("Attendance marked successfully!")

    def attendance_percentage(self):
        total=len(self.attendance)
        if total==0:
            return 0
        present=list(self.attendance.values()).count("Present")
        return (present/total)*100

    def report(self):
        total=len(self.attendance)
        present=list(self.attendance.values()).count("Present")
        absent=total-present
        percentage=self.attendance_percentage()

        print("\n" + "*" * 20 + " Attendance Report " + "*" * 20)
        print("Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Total Days:", total)
        print("Present:", present)
        print("Absent:", absent)
        print(f"Attendance: {percentage:.2f}%")

        if total>0 and percentage<75:
            print("WARNING!: Attendance is below 75%.")

class AttendanceSystem:
    def __init__(self):
        self.students={}

    def add_student(self):
        name=input("Enter student name:")
        roll=input("Enter roll number:")
        if roll in self.students:
            print("Roll number already exists!")
            return
        self.students[roll]=Student(name,roll)
        print("Student added successfully!")

    def students_list(self):
        if not self.students:
            print("No students found")
            return
        print("\n" + "*" * 20 + " Student List " + "*" * 20)
        for roll,student in self.students.items():
            print("Roll Number:",roll)
            print("Name:",student.name)

    def mark_attendance(self):
        roll = input("Enter roll number: ")
        if roll not in self.students:
            print("Student not found!")
            return

        attendance_date = input("Enter date (DD-MM-YYYY): ")
        status = input("Enter status (Present/Absent): ").capitalize()

        self.students[roll].mark_attendance(attendance_date, status)

    def show_report(self):
        roll=input("Enter roll number:")
        if roll not in self.students:
            print("Student not found!")
            return
        self.students[roll].report()

    def save_data(self):
        data = {}

        for roll, student in self.students.items():
            data[roll] = {
                "name": student.name,
                "roll_number": student.roll_number,
                "attendance": student.attendance
            }

        with open("students.json", "w") as file:
            json.dump(data, file, indent=4)

        print("Data saved successfully!")

    def load_data(self):
        try:
            with open("students.json", "r") as file:
                data = json.load(file)

            for roll, details in data.items():
                student = Student(
                    details["name"],
                    details["roll_number"]
                )
                student.attendance = details["attendance"]
                self.students[roll] = student

            print("Data loaded successfully!")

        except FileNotFoundError:
            print("No saved data found. Starting fresh.")

    

    def run(self):
        while True:
            print("\n--- Student Attendance System ---")
            print("1. Add Student")
            print("2. List Students")
            print("3. Mark Attendance")
            print("4. Show Report")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.students_list()
            elif choice == "3":
                self.mark_attendance()
            elif choice == "4":
                self.show_report()
            elif choice == "5":
                self.save_data()
                print("Exiting system. Goodbye!")
                break
            else:
                print("Invalid choice! Try again.")




system = AttendanceSystem()
system.load_data()
system.run()


        

