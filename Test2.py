class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self.average_grade()}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}")

    def average_grade(self):
        total = 0
        count = 0
        for course_grades in self.grades.values():
            total += sum(course_grades)
            count += len(course_grades)
        return round(total / count, 1) if count > 0 else 0

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return super().__str__() + f"\nСредняя оценка за лекции: {self.average_grade()}"

    def average_grade(self):
        total = 0
        count = 0
        for course_grades in self.grades.values():
            total += sum(course_grades)
            count += len(course_grades)
        return round(total / count, 1) if count > 0 else 0


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


# Пример использования
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 8)

print(best_student.grades)  # {'Python': [10, 9, 8]}

lecturer = Lecturer('John', 'Doe')
lecturer.courses_attached += ['Python']

best_student.rate_lecturer(lecturer, 'Python', 9)
best_student.rate_lecturer(lecturer, 'Python', 10)
best_student.rate_lecturer(lecturer, 'Python', 8)

print(lecturer.grades)  # {'Python': [9, 10, 8]}
print(lecturer)