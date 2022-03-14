

def student_grades(grade1, grade2, grade3, average_type):
    if average_type in ['A', 'a']:
        return (grade1 + grade2 + grade3) / 3
    elif average_type in ['P', 'p']:
        return (grade1 * 5 + grade2 * 3 + grade3 * 2) / 10


print(student_grades(5, 5, 6, 'A'))
print(student_grades(5, 5, 6, 'P'))
