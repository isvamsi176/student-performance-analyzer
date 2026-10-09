def calculate_total(marks):
    return sum(marks)

def calculate_average(marks):
    return sum(marks) / len(marks)

def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"

def check_result(marks):
    if all(mark >= 35 for mark in marks):
        return "PASS"
    else:
        return "FAIL"

print("=" * 40)
print(" STUDENT PERFORMANCE ANALYZER")
print("=" * 40)

student_name = input("Enter student name: ")

while True:
    try:
        number_of_subjects = int(
            input("Enter number of subjects: ")
        )

        if number_of_subjects > 0:
            break
        else:
            print("Enter at least one subject.")

    except ValueError:
        print("Please enter a valid whole number.")

marks = []

for i in range(number_of_subjects):

    while True:
        try:
            mark = float(
                input(f"Enter marks for Subject {i + 1}: ")
            )

            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print("Marks must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")

total = calculate_total(marks)
average = calculate_average(marks)
grade = calculate_grade(average)
result = check_result(marks)

percentage = (total / (number_of_subjects * 100)) * 100

print("\n" + "=" * 40)
print("       STUDENT REPORT")
print("=" * 40)

print("Student Name :", student_name)
print("Subject Marks:", marks)
print("Total Marks  :", total)
print("Average      :", round(average, 2))
print("Percentage   :", round(percentage, 2), "%")
print("Highest Mark :", max(marks))
print("Lowest Mark  :", min(marks))
print("Grade        :", grade)
print("Final Result :", result)

print("=" * 40)
print("Thank you for using the application!")