

_average_score = None
_sum_of_scores = 0

print("How many students are there in the class?")
_students_of_the_teacher = int(input("Teacher: "))

for i in range(int(_students_of_the_teacher)):
    print(f"\nEnter the score of Stduent No.{i+1}: ")
    _student_score = int(input("Student: "))
    _sum_of_scores += _student_score

    if i == _students_of_the_teacher - 1:
        _average_score = _sum_of_scores / (_students_of_the_teacher)
        print(f"\nAverage score is: {float(_average_score)}")
        break

