from Student import Student
from Lecturer import Lecturer
from Reviewer import Reviewer


def start():
    # Students
    student1 = Student("Jane", "Doe", "female")
    student2 = Student("John", "Doe", "male")

    student1.courses_in_progress += ["Fullstack developer on Python"]
    student2.courses_in_progress += ["Fullstack developer on JavaScript"]

    # Mentors
    reviewer1 = Reviewer("Reviewer1's_name", "Reviewer's_surname")
    reviewer2 = Reviewer("Reviewer2's_name", "Reviewer's_surname")
    lecturer1 = Lecturer("Lecturer1's_name", "Lecturer's_surname")
    lecturer2 = Lecturer("Lecturer2's_name", "Lecturer's_surname")

    reviewer1.courses_attached += ["Fullstack developer on Python"]
    reviewer2.courses_attached += ["Fullstack developer on JavaScript"]
    lecturer1.courses_attached += ["Fullstack developer on Python"]
    lecturer2.courses_attached += ["Fullstack developer on JavaScript"]

    reviewer1.set_rate(student1, "Fullstack developer on Python", 10)
    reviewer2.set_rate(student1, "Fullstack developer on Python", 8)

    reviewer1.set_rate(student2, "Fullstack developer on JavaScript", 9)
    reviewer2.set_rate(student2, "Fullstack developer on JavaScript", 5)

    lecturer1.set_rate("Fullstack developer on Python", 10)
    lecturer2.set_rate("Fullstack developer on JavaScript", 9)

    # Print objects
    print(f"{student1}\n")
    print(f"{student2}\n")
    print(f"{reviewer1}\n")
    print(f"{reviewer2}\n")
    print(f"{lecturer1}\n")
    print(f"{lecturer2}\n")

    # Print average rates
    print(get_hw_average([student1, student2]))
    print(get_lecture_average([lecturer1, lecturer2]))


def get_hw_average(students):
    __sum = 0
    for student in students:
        if isinstance(student, Student):
            __sum += student.average_grade
        else:
            return "Error"
    return f"Average grade for homeworks is {__sum / len(students)}"


def get_lecture_average(lecturers):
    __sum = 0
    for lecturer in lecturers:
        if isinstance(lecturer, Lecturer):
            __sum += lecturer.average_grade
        else:
            return "Error"
    return f"Average grade for lecturers is {__sum / len(lecturers)}"


if __name__ == "__main__":
    start()
