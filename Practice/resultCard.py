# taking input from user 
userName = input("Enter your name: ").title()
regNo = int(input("Enter your registration number: "))
mathMarks = int(input("Enter your marks in Math: "))
phyMarks = int(input("Enter your marks in Physics: "))
engMarks = int(input("Enter your marks in English: "))
PFMarks = int(input("Enter your marks in PF: "))
ICTMarks = int(input("Enter your marks in ICT: "))
# calculations
obtainedMarks = mathMarks + phyMarks + engMarks + PFMarks + ICTMarks
totalMarks = 500
percentage = (obtainedMarks / totalMarks) * 100
# defining grades
if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
elif percentage >= 50:
    grade = "E"
else:
    grade = "F"
# printing result card    
print("Name ".center(20) + "\t|\t" + "Registration No.".center(18) + "\t|\t" + "Obtained Marks".center(15) + "\t|\t" + "Total Marks".center(15) + "\t|\t" + "Percentage".center(15) + "\t|\t" + "Grade".center(15) + "\t|\n")
print(userName.center(20) + "\t|\t" + str(regNo).center(18) + "\t|\t" + str(obtainedMarks).center(15) + "\t|\t" + str(totalMarks).center(15) + "\t|\t" + str(round(percentage,2)).center(15) + "\t|\t" + grade.center(15) + "\t|\n")

print("\n\nThe student got {0} marks out of {1} marks and his percentage is {2}% and grade is {3}.".format(obtainedMarks, totalMarks, percentage, grade))