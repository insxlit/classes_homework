from Mentor import Mentor


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.grades = {}
        self.average_grade = 0
        super(Lecturer, self).__init__(name, surname)

    def set_rate(self, course, grade):
        if course in self.courses_attached:
            if course in self.grades:
                self.grades[course] += [grade]
            else:
                self.grades[course] = [grade]
            self.average_grade = self.__count_average()
        else:
            return "Error"

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
               f"Средняя оценка за лекции: {self.average_grade}"
