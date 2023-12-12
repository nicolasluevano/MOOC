# Write your solution here
def get_data():
    data = []
    while True:
        ask = input("Exam points and exercises completed: ")
        if ask == '':
            break
        data.append(ask)
    return data

def exam_points(data):
    pts = []
    for i in data:
        ex_pts = i.split(' ')
        pts.append(int(ex_pts[0]))
    return pts


def exer_completed(data):
    excercises_completed = []
    for i in data:
        comp = i.split(' ')
        excercises_completed.append(int(comp[-1]))
    return excercises_completed



def exer_pts(excercises_completed):
    exer_pts = []
    for i in excercises_completed:
        if i == 100:
            exer_pts.append(10)
        else:
            exer_pts.append(int(str(i)[:1]))
    return exer_pts




def total_points_exam(exam_pts, exer_pts):
    total_points = []
    for i in range(0, len(exam_pts)):
        if exam_pts[i] < 10:
            total_points.append(0)
        else:
            total_points.append(exam_pts[i] + exer_pts[i])
    return total_points



def total_points(exam_pts, exer_pts):
    total_points = []
    for i in range(0, len(exam_pts)):
            total_points.append(exam_pts[i] + exer_pts[i])
    return total_points



def grades(total_points_exam):
    grades = []
    for i in total_points_exam:
        if i <= 14:
            grades.append(0)
        elif 15 <= i <= 17:
            grades.append(1)
        elif 18 <= i <= 20:
            grades.append(2)
        elif 21 <= i <= 23:
            grades.append(3)
        elif 24 <= i <= 27:
            grades.append(4)
        elif 28 <= i <= 30:
            grades.append(5)

    return grades



def points_average(total_points):
    points_all = 0
    for i in total_points:
        points_all += i
    points_average = points_all / len(total_points)
    return f'Points average: {points_average:.1f}'


def pass_percentage(grades):
    num_of_passed = 0
    for i in grades:
        if i > 0:
            num_of_passed += 1
    pass_percentage = (num_of_passed / len(grades)) * 100
    return f'Pass percentage: {pass_percentage:.1f}'




def grade_distribution(grades):
    five = "5: "
    four = "4: "
    three = "3: "
    two = "2: "
    one = "1: "
    zero = "0: "

    for i in grades:
        if i == 0:
            zero += "*"
        if i == 1:
            one += "*"
        if i == 2:
            two += "*"
        if i == 3:
            three += "*"
        if i == 4:
            four += "*"
        if i == 5:
            five += "*"
    print("Grade distribution:")
    print(five)
    print(four)
    print(three)
    print(two)
    print(one)
    print(zero)



def main():
    data = get_data()
    exam_pts = exam_points(data)
    exer_comp = exer_completed(data)
    exer_pt = exer_pts(exer_comp)
    ttl_points_exm = total_points_exam(exam_pts, exer_pt)
    tt_points = total_points(exam_pts, exer_pt)
    grade = grades(ttl_points_exm)

    print("Statistics:")
    print(points_average(tt_points))
    print(pass_percentage(grade))
    grade_distribution(grade)


main()