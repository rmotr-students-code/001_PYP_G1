import random


students = ['amar.zlojic@gmail.com',
 'a89.warren@gmail.com',
 'benhgift@gmail.com',
 'bogdanpintican@gmail.com',
 'bwoodske@gmail.com',
 'mcphersond13@gmail.com',
 'andykaysbox@gmail.com',
 'jdagostino2@gmail.com',
 '8bityamist@gmail.com',
 'msears024@gmail.com',
 'preston3050@gmail.com'
]
print(len(students))


def get_random_groups(students_list, group_size=3):
    def _get_random_student(students_copy):
        return students_copy.pop(random.randint(0, len(students_copy)-1))

    students_copy = students_list[:]
    groups = []
    current_group = []
    for _ in range(len(students_copy)):
         student = _get_random_student(students_copy)
         current_group.append(student)
         if len(current_group) == group_size:
              groups.append(current_group)
              current_group = []
    if len(current_group):
        groups.append(current_group)
    return groups


print(get_random_groups(students))