# Store subjects and marks in a dictionary
marks = {
    "English": int(input("Enter English marks: ")),
    "Hindi": int(input("Enter Hindi marks: ")),
    "Math": int(input("Enter Math marks: ")),
    "Physics": int(input("Enter Physics marks: ")),
    "Chemistry": int(input("Enter Chemistry marks: "))
}

# 1. Loop to check each subject
for subject, score in marks.items():
    if score < 33:
        print(f"Alert: You failed in {subject} [Marks: {score}]")

# 2. Calculate Total and Percentage
total = sum(marks.values())
percentage = total / len(marks)

# 3. Grade Logic
if percentage >= 91:
    grade = "A+"
elif percentage >= 81:
    grade = "A"
elif percentage >= 71:
    grade = "B+"
elif percentage >= 61:
    grade = "B"
elif percentage >= 51:
    grade = "C+"
elif percentage >= 41:
    grade = "C"
elif percentage >= 33:
    grade = "D"
else:
    grade = "Fail"

print("-" * 20)
print(f"Total Marks: {total}")
print(f"Percentage: {percentage}%")
print(f"Final Grade: {grade}")
