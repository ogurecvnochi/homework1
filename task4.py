lecture = ["Аня", "Борис", "Вика", "Гоша", "Аня"]
seminar = ["Вика", "Дима", "Борис", "Ева"]
list_students = list(set(lecture + seminar))
cnt_student = len(list_students)
list_lect = []
list_both = []
for student in list_students:
    if student in lecture and student in seminar:
        list_both.append(student)
    elif student in lecture:
        list_lect.append(student)
print('Всего уникальных студентов:', cnt_student)
print('На обеих парах:', list_both)
print('Только на лекции:', list_lect)
print('Хотя бы на одной:', list_students)