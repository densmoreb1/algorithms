# https://www.hackerrank.com/challenges/grading/problem
# see the link for rules
# round to the nearest 5 unless...

def gradingStudents(grades):
    new = []
    for grade in grades:
        # base = 5 * round(grade/5)
        if grade >= 38:
            if grade % 5 == 3:
                grade += 2
                # new.append(grade)
            elif grade % 5 == 4:
                grade += 1
                # new.append(grade)
        new.append(grade)

    return new
