# Jordan R. Worrobah    
# 5/11/2026
# Ex3A_string_cleaning.py

name_1 = "PRIYA SHARMA" 
name_2 = "bob NGUYEN" 
name_3 = "LaTonya Williams" 
salary_1 = "$82,500" 
salary_2 = "$74,000"

name1Lower = name_1.lower()
name2Lower = name_2.lower() 
name3Lower = name_3.lower()

print(name1Lower)
print(name2Lower) 
print(name3Lower)

name1Title = name_1.title()
name2Title = name_2.title()
name3Title = name_3.title()

print(name1Title)
print(name2Title)
print(name3Title)

salary1Replace = salary_1.replace("$", "").replace(",", "")
salary2Replace = salary_2.replace("$", "").replace(",", "")

print(salary1Replace, type(salary1Replace))
print(salary2Replace, type(salary2Replace))

salaryInt1 = int(salary1Replace)
salaryInt2 = int(salary2Replace)

print(salaryInt1, type(salaryInt1))
print(salaryInt2, type(salaryInt2))
