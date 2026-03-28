
import random

def create_sections():
    sections = int(input("Enter the number of sections: "))
    ids = []

    for i in range(sections):
        students = int(input(f"How many students in section {i + 1}? "))

        section = []
        for _ in range(students):
            section.append(random.randint(1000, 9999))
        
        ids.append(section)

    return ids

# Example usage:
student_ids = create_sections()
for section in student_ids:
    print(section)