# Jordan R. Worrobah


with open("students.txt", "w") as file:
    file.write("Alice\n")
    file.write("Bob\n")

with open("students.txt", "r") as file:
    content = file.read()
    print(content)


with open("example", "w") as file:
    file.write("Hello, python!")

