# enumerate() - gets index + value, it loops with position and the value 

names = list(map(str, input().split()))

for index, value in enumerate(names):
    print(index, value)


# zip() - it combines multiple lists together 

students = ["Saniya", "Alikhan", "Lera", "Aruzhan"]
scores = [95, 93, 91, 90]

for student, score in zip(students, scores):
    print(student,score)