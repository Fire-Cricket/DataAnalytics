# Jordan R. Worrobah
# 5/11/2026
# Greeting Script

currentHour = int(input("Enter the current hour (0-23): "))

if currentHour >= 23 or currentHour < 4:
    print("What are you doing up so late?")

elif 5 <= currentHour < 12:
    print("Good morning!")

elif 12 <= currentHour < 18:
    print("Good day!")

else:
    print("Good evening!")