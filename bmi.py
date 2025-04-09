height = float(input("What is your height (in foot (foot): "))
weight = float(input("What is your weight (in kilograms (kg): "))
height_mt = height/3.281
bmi = weight/height_mt ** 2
bmi = round(bmi, 1)
Underweight = 18.5
Healthy_Weight = 18.5 
Overweight = 29.9 
Obese = 30.0
if bmi <= Underweight:
    category =  "Underweight"
elif bmi <= Healthy_Weight:
    category =  "Normal"
elif bmi <= Overweight:
    category =  "Overweight"
else: 
    category =  "Obese"
print(f"Your BMI of {bmi} makes you {category}")
