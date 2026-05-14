# Jordan R. Worrobah
# 5/12/2026
# Show Major

student_name = input("Enter student name: ")
student_major = input("Enter major code: ").upper()

if student_major == "ENG":
    major_name = "Engineering"
    office_location = "Building A"

elif student_major == "BUS":
    major_name = "Business"
    office_location = "Building B"

elif student_major == "CSC":
    major_name = "Computer Science"
    office_location = "Building C"

elif student_major == "ART":
    major_name = "Art"
    office_location = "Building D"

else:
    major_name = "<unknown>"
    office_location = ""

print(f"Student Name: {student_name}")
print(f"Major Code: {student_major}")
print(f"Major Name: {major_name}")
print(f"Office Location: {office_location}")