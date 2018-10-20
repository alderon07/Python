myScore = float(input("What is your score?"))
totalScore = float(input("What is the total score?"))
myGrade = (myScore / totalScore) * 100.0

if myGrade >= 90:
    print("Your letter grade on the test is an A.")
elif myGrade >=80 and myGrade <= 90:
    print("Your letter grade on the test is an B.")
elif myGrade >=70 and myGrade <= 80:
    print("Your letter grade on the test is a C")
elif myGrade >=60 and myGrade <= 70:
    print("Your letter grade on the test is a D")
else:
    print("Your letter grade on the test is an F")


print("Your test score is %.2f" % myGrade)