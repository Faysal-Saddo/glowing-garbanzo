#weight/height^2
#input weight in kg, height in meter
#whole number as output

weight =input("Enter your weight in kg:")
height = input("Enter your height in meter:")


Bmi = float(weight)/float(height)**2

Bmi = int(Bmi)

print("Your BMI is:",Bmi)