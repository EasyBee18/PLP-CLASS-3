# ask user to enter student score
score = int(input("Enter the student score(0-100): "))

if score >= 90:
    grade ='A'
    
elif score >= 80:
    grade = 'B'

elif score >= 70:
    grade = 'C'

elif score >= 60:
    grade = 'D'

else:
    grade = 'F'

# print the result


# print("The student grade is: "+ grade)
print(f"The student grade is: {grade}")

