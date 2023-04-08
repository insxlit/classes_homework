import statistics

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = ["Как пользоваться личным кабинетом"]
        self.courses_in_progress = []
        self.grades = {}
        self.average_grade = 0

    def update_grades(self, course, grade):
        if course in self.grades:
            self.grades[course].append(grade)
        else:
            self.grades[course] = [grade]

        all_values = [value for value in self.grades.values()]
        all_values_flat = [item for sublist in all_values for item in sublist]
        self.average_grade = statistics.mean(all_values_flat)

    def __count_average(self):
        __marks = 0
        __sum = 0
        for course in self.grades:
            __marks += len(self.grades.get(course))
            __sum += sum(self.grades.get(course))
        return __sum / __marks

    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n" \
               f"Средняя оценка за домашние задания: {self.average_grade}\n" \
               f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n" \
               f"Завершенные курсы: {', '.join(self.finished_courses)}"

    def __lt__(self, other):
        return self.average_grade < other.average_grade

    def __eq__(self, other):
        return self.average_grade == other.average_grade

    def __gt__(self, other):
        return self.average_grade > other.average_grade
