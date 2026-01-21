print("Welcome - Updated by Developer B")


from login import login

students = {}

def mark_attendance(name, status):
    students[name] = status

def view_attendance():
    print("\nAttendance List:")
    for name, status in students.items():
        print(name, "-", status)

# Main program
if login():
    print("\nLogin successful. Access granted.\n")

    mark_attendance("Oviya", "Present")
    mark_attendance("Pradeep", "Absent")
    view_attendance()
else:
    print("Access denied. Invalid login.")
