height = int(input("Enter Height(cm):"))
weight = int(input("Enter Weight(kg):"))

bmi = weight / ((height*0.01)**2)

if bmi < 16:
    print("Severely underweight")
elif bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")