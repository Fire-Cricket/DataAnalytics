# Jordan R. Worrobah
# 5/26/2026

f = open('about_me.txt', "r")
'''
print(f.read(50))
print(f.readline(10))
print(f.readline())

for i in range(1,20): 
   print(f.readline())

print(f.readlines(1))
print(f.readlines(1))

print(f.readlines(10))
print(f.readlines(10))

print(f.readlines(100))
print(f.readlines(-1))
'''

first_50 = f.read(50)

line_list = []

for i in range(1, 5):
    line_list.append(f.readline())

remaining_lines = f.readlines(100)
'''
print("-----READ(50)-----")
print(first_50)

print("\n-----READLINE LOOP-----")
print(line_list)

print("\n-----READLINES(100)-----")
print(remaining_lines)
'''

print(f"First 50 characters: {first_50}")

print(
    f"\nNext four lines, as list by line: "
    f"{line_list}"
)

print(
    f"\nNext 100 characters, as list by line, "
    f"rounded up to complete lines: "
    f"{remaining_lines}"
)
f.close()
