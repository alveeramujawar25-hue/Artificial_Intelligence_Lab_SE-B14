print("Enter marks of 5 subjects (out of 100):")
subject1 = float(input("subject1: "))
subject2 = float(input("subject2: "))
subject3 = float(input("subject3: "))
subject4 = float(input("subject4: "))
subject5 = float(input("subject5: "))
total_marks = subject1+subject2+subject3+subject4+subject5
percentage = (total_marks/500)*100
print(f"\ntotal_marks:{total_marks}/500")
print(f"percentage:{percentage:.2f}%")
if percentage>= 75:
    print("Grade:Distinction")
elif percentage>=65 and percentage<=75:
    print("Grade:I class(first class)")
elif percentage>=55 and percentage<=65:
    print("Grade:II class(first class)")
else:
    print("Fail")



