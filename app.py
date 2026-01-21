students = {}

def mark_attendance(name, status):
    students[name] = status

def view_attendance():
    print("Attendance List:")
    for name, status in students.items():
        print(name, "-", status)

mark_attendance("Oviya", "Present")
mark_attendance("Pradeep", "Absent")
view_attendance()
