 '''
 Example tool for calculating a student's grade.
 Program gets student's status ('UG' == Undergrad; 'G'== Graduate Student; 'DL' == Distance Learning) from input,
 else excludes any other inputs & exits program.
 Program then calculates ((points earned / points possible) * 100) & outputs as a percentage to the hundredths place.
 '''

student_status = str(input(f'Please enter student type: '))
if student_status == 'G':
    pass                        
elif student_status == 'DL': 
    pass
elif student_status == 'UG':
    pass
else:
    print('Error: student status must be UG, G or DL')
    exit()
# gets student status from user
# exit program if input not recognized


hw_pts = float(input(f'Homework Points: '))
quiz_pts = float(input(f'Quiz Points: '))
midterm_pts = float(input(f'Midterm Points: '))
final_exam_pts = float(input(f'Final Exam Points: '))
# read scores as floats from input


hw_grade = (hw_pts / 800.0) * 100 
quiz_grade = (quiz_pts/ 400.0) * 100
midterm_grade = (midterm_pts / 150.0) * 100
final_exam_grade = (final_exam_pts / 200.0) * 100
# calculates scores as percentages based on max possible points


print(f'Homework: {hw_grade:.2f}%')
print(f'Quizzes: {quiz_grade:.2f}%')
print(f'Midterm: {midterm_grade:.2f}%')
print(f'Final Exam: {final_exam_grade:.2f}%')
# outputs students grades









