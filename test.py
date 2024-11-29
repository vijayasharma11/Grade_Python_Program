# Function to calculate grade based on percentage
def calculate_grade(percentage):
    if percentage >= 70:
        return 'A'
    elif percentage >= 60:
        return 'B'
    elif percentage >= 50:
        return 'C'
    elif percentage >= 45:
        return 'D'
    else:
        return 'No Grade'

# Function to calculate percentage
def calculate_percentage(coursework_mark, prelim_mark):
    total_marks = coursework_mark + prelim_mark
    return (total_marks * 100) / 150

# Function to process one student
def process_student(name, coursework_mark, prelim_mark):
    percentage = calculate_percentage(coursework_mark, prelim_mark)
    grade = calculate_grade(percentage)
    print(f"Student: {name}, Coursework Mark: {coursework_mark}, Prelim Mark: {prelim_mark}")
    print(f"Percentage: {percentage:.2f}%, Grade: {grade}\n")
    return grade, percentage

# Function to read and process all students from file
def process_all_students(names_file, mark1_file, mark2_file):
    with open(names_file, 'r') as nf, open(mark1_file, 'r') as m1f, open(mark2_file, 'r') as m2f:
        names = nf.readlines()
        mark1 = list(map(int, m1f.readlines()))
        mark2 = list(map(int, m2f.readlines()))

    grades = []
    percentages = []
    
    for i in range(len(names)):
        name = names[i].strip()
        coursework_mark = mark1[i]
        prelim_mark = mark2[i]
        
        grade, percentage = process_student(name, coursework_mark, prelim_mark)
        grades.append(grade)
        percentages.append(percentage)
    
    return grades, percentages

# Function to count occurrences of "A" grade
def count_A_grades(grades):
    return grades.count('A')

# Function to find the student with the best percentage
def find_best_percentage(names, percentages):
    best_index = percentages.index(max(percentages))
    return names[best_index].strip(), max(percentages)

# Main program
if __name__ == "__main__":
    # File paths
    names_file = 'names.txt'
    mark1_file = 'mark1.txt'
    mark2_file = 'mark2.txt'

    # Process all students
    grades, percentages = process_all_students(names_file, mark1_file, mark2_file)

    # Task 7: Count "A" grades and find the best student
    num_A_grades = count_A_grades(grades)
    best_student, best_percentage = find_best_percentage(grades, percentages)

    print(f"\nNumber of 'A' grades: {num_A_grades}")
    print(f"Best student: {best_student} with percentage: {best_percentage:.2f}%")

    # Task 8: Explain fetch-execute cycle in program context
    # This will be explained in the report.
