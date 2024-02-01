# write your solution here

# ask for exercise and student files
if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_points = input("Exam points:")
else:
    student_info = "src/students1.csv"
    exercise_data = "src/exercises1.csv"
    exam_points = "src/exam_points1.csv"


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

exam_pts = {}
with open(f"{exam_points}") as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split(";")
        if parts[0] == 'id':
            continue
        total = (int(parts[1]) + int(parts[2]) + int(parts[3]))
        exam_pts[int(parts[0])] = total


for id, name in students.items():
    if id in scores and id in exam_pts:
        results = (scores[id] / 40) * 100
        points = min(results // 10, 10)

        pts = exam_pts[id]
        total_score = points + pts
        final_grade = 0

        if total_score >= 28:
            final_grade = 5
        elif total_score >= 24:
            final_grade = 4
        elif total_score >= 21:
            final_grade = 3
        elif total_score >= 18:
            final_grade = 2
        elif total_score >= 15:
            final_grade = 1
        else:
            final_grade = final_grade

        print(f'{name} {final_grade}')

