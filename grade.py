def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i] < 38:
            continue        
        elif (5 * (grades[i] // 5 + 1) - grades[i]) < 3:
            grades[i] = 5 * (grades[i] // 5 + 1)
            continue
        else:
            grades[i]
            continue
    return grades
grade = [100,80,39,33]
print(gradingStudents(grade))