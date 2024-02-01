# write your solution here

# ask for exercise and student files
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")


# grab student information
students = {}
with open(f"{student_info}") as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split(";")
        if parts[0] == 'id':
            continue
        students[int(parts[0])] = f'{parts[1]} {parts[2]}'

scores = {}
with open(f"{exercise_data}") as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split(";")
        if parts[0] == 'id':
            continue
        total = (int(parts[1]) + int(parts[2]) + int(parts[3]) + int(parts[4]) + int(parts[5]) + int(parts[6]) + int(parts[7]))
        scores[int(parts[0])] = total

for id, name in students.items():
    if id in scores:
        results = scores[id]
        print(f'{name} {results}')
