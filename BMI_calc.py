#weight/height^2
#input weight in kg, height in meter
#whole number as output

weight =input("Enter your weight in kg:")
height = input("Enter your height in meter:")


Bmi = float(weight)/float(height)**2


Bmi_print = round(Bmi,1)
print(f"Your BMI is:{Bmi_print}")



if(Bmi < 16.0):
    print("Underweight(severe thinness)")
elif(Bmi >= 16.0 and Bmi<= 16.9):
    print("Underweight(moderate thinness)")
elif(Bmi >= 17.0 and Bmi<= 18.4):
    print("Underweight(mild thinness)")
elif(Bmi >= 18.5 and Bmi<= 24.9):
    print("Normal weight")
elif(Bmi >= 25.0 and Bmi<= 29.9):
    print("Overweight(pre-obese)")
elif(Bmi >= 30.0 and Bmi<= 34.9):
    print("Obese(Class 1)")
elif(Bmi >= 35.0 and Bmi<= 39.9):
    print("Obese(Class 2)")
elif(Bmi >= 40.0):
    print("Obese(Class 3)")

