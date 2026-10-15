students_name = (input("What is your name?"))
students_age = int(input("What is your age?"))
students_class = (input("What is your class?"))
amount_of_grades = int(input("How many grades do you have?"))
average_grade = 0
highest_grade = 0
lowest_grade = 0
all_grades = []
eight_or_above = 0
between_five_seven = 0
below_five_five = 0
EXCELLENT_GRADE = 8
GOOD_GRADE = 7
PASSING_GRADE = 5.5
MIN_AMOUNT_GRADES = 6

if amount_of_grades < MIN_AMOUNT_GRADES:
    print("You must enter more than 6 grades.")
else:
    for x in range(amount_of_grades):
        grade_total = float(input("Please enter your grades: "))
        all_grades.append(grade_total)

print(" ")
print("Student Report")
print("---------------\n")

print("Name: ", students_name)
print("Age: ", students_age)
print("Class: ", students_class)
print(" ")

print("Grades: ", (str(all_grades).strip("[]")))
print(" ")

grade_total = sum(all_grades)

average_grade = grade_total / amount_of_grades
print("Your average grade is: ", round(average_grade, 1))

highest_grade = max(all_grades)
print("Your highest grade is: ", highest_grade)
lowest_grade = min(all_grades)
print("Your lowest grade is: ", lowest_grade)
print(" ")

for x in all_grades:
    if x >= EXCELLENT_GRADE:
      eight_or_above += 1
    elif x < PASSING_GRADE:
      below_five_five += 1
    else:
      between_five_seven += 1
 
print("Grades 8+: ", eight_or_above)
print("Grades 5.5-7.9: ", between_five_seven)
print("Grades 5.5 and below:", below_five_five)

print(" ")

if average_grade >= EXCELLENT_GRADE:
    print("Peformance: Excellent ")
    print("Status: Passed")
    
elif average_grade >= GOOD_GRADE:
    print("Performance: Good ")
    print("Status: Passed ")
    
elif average_grade >= PASSING_GRADE:
    print("Performance: Passed ")
    print("Status: Passed ")
    
else:
    print("Performance: Failed ") 
