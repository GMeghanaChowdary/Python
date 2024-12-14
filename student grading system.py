def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"
    
def student_grading_system():
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    grade = get_grade(marks)
    print(f"Student: {name}, Marks: {marks}, Grade: {grade}")

student_grading_system()
