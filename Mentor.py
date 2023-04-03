from Student import Student


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def get_rate(self, student, course):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            return f"{student.name} {student.surname}'s grades on the course {course}: " \
                   f"{', '.join(map(str, student.grades[course]))}"
        else:
            return "Error"
