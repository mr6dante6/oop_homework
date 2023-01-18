class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lector, course, grade):
        if isinstance(lector, Lector) and course in self.courses_in_progress and course in lector.courses_attached:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        fin_courses = ', '.join(self.finished_courses)
        cour_in_progress = ', '.join(self.courses_in_progress)
        for key, val in self.grades.items():
            res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {round(sum(val)/len(val), 2)}\n' \
                  f'Курсы в процессе изучения: {cour_in_progress}\n' \
                  f'Завершенные курсы: {fin_courses}'
            return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


class Lector(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        for val in self.grades.values():
            res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {round(sum(val)/len(val), 2)}'
            return res


best_student1 = Student('Ruoy', 'Eman', 'male')
best_student1.courses_in_progress += ['Python', 'JavaScript', '1c']
best_student1.finished_courses += ['Java']

best_student2 = Student('Tobbie', 'Perlman', 'male')
best_student2.courses_in_progress += ['Python', '1c']
best_student2.finished_courses += ['JavaScript']

cool_mentor1 = Mentor('Jim', 'Falton')
cool_mentor1.courses_attached += ['Python']

cool_mentor2 = Mentor('Eddie', 'Cruise')
cool_mentor2.courses_attached += ['Python']

cool_reviewer1 = Reviewer('Emily', 'Hide')
cool_reviewer1.courses_attached += ['Python', 'JavaScript']

cool_reviewer2 = Reviewer('Le', 'Wan')
cool_reviewer2.courses_attached += ['Python', '1c']

cool_lector1 = Lector('Jo', 'Neels')
cool_lector1.courses_attached += ['Python', '1c']

cool_lector2 = Lector('Ron', 'Berckle')
cool_lector2.courses_attached += ['Python', 'JavaScript']

cool_reviewer1.rate_hw(best_student1, 'JavaScript', 10)
cool_reviewer1.rate_hw(best_student1, 'JavaScript', 10)
cool_reviewer1.rate_hw(best_student1, 'JavaScript', 10)

cool_reviewer2.rate_hw(best_student2, '1c', 8)
cool_reviewer2.rate_hw(best_student2, '1c', 7)
cool_reviewer2.rate_hw(best_student2, '1c', 6)

cool_reviewer1.rate_hw(best_student2, 'Python', 9)
cool_reviewer1.rate_hw(best_student2, 'Python', 5)
cool_reviewer1.rate_hw(best_student2, 'Python', 5)

cool_reviewer2.rate_hw(best_student1, '1c', 10)
cool_reviewer2.rate_hw(best_student1, '1c', 10)
cool_reviewer2.rate_hw(best_student1, '1c', 10)

cool_reviewer2.rate_hw(best_student2, 'Python', 9)
cool_reviewer2.rate_hw(best_student2, 'Python', 5)
cool_reviewer2.rate_hw(best_student2, 'Python', 5)

best_student1.rate_hw(cool_lector1, '1c', 10)
best_student1.rate_hw(cool_lector1, '1c', 10)
best_student1.rate_hw(cool_lector1, '1c', 9)

best_student1.rate_hw(cool_lector2, 'JavaScript', 7)
best_student1.rate_hw(cool_lector2, 'JavaScript', 8)
best_student1.rate_hw(cool_lector2, 'JavaScript', 7)

best_student2.rate_hw(cool_lector1, 'Python', 9)
best_student2.rate_hw(cool_lector1, 'Python', 9)
best_student2.rate_hw(cool_lector1, 'Python', 9)

best_student2.rate_hw(cool_lector2, 'Python', 9)
best_student2.rate_hw(cool_lector2, 'Python', 10)
best_student2.rate_hw(cool_lector2, 'Python', 7)


def average_student(student_list, course):
    sum_grades = {course: []}
    for student in student_list:
        for k, v in student.grades.items():
            if course == k:
                sum_grades[course] += v
                break
    for average in sum_grades.values():
        try:
            return round(sum(average) / len(average), 2)
        except:
            return 'у студентов ещё нет оценок по данному курсу!'


def average_lector(lector_list, course):
    sum_grades = {course: []}
    for lector in lector_list:
        for k, v in lector.grades.items():
            if course == k:
                sum_grades[course] += v
                break
    for average in sum_grades.values():
        try:
            return round(sum(average) / len(average), 2)
        except:
            return 'у лекторов ещё нет оценок по данному курсу!'


print('\nРевьюеры:')
print(f'{cool_reviewer1}\n')
print(f'{cool_reviewer2}')
print('---------------------')
print('Преподаватели:')
print(f'{cool_lector1}\n')
print(f'{cool_lector2}')
print('---------------------')
print('Студенты:')
print(f'{best_student1}\n')
print(f'{best_student2}')
print('---------------------')

print()
student_list = [best_student1, best_student2]
student_course = 'Python'
print(f'Средняя оценка студентов на курсе {student_course} = {average_student(student_list, student_course)}')

print()
lector_list = [cool_lector1, cool_lector2]
lector_course = '1c'
print(f'Средняя оценка лекторов на курсе {lector_course} = {average_lector(lector_list, lector_course)}')
