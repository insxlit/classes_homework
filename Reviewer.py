from Mentor import Mentor
from Student import Student


class Reviewer(Mentor):
    def set_rate(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            student.update_grades(course, grade)
        else:
            return "Error"

    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}"
