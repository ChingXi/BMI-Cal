# BMI Calculator!
# BMI = kg/m^2
user_weight = False
user_height = False
w = 0
h = 0


while not user_weight:
    try:
        weight = float(input("Enter your weight in kg: "))
        if weight > 0:
            print("Weight entered successfully!")
            user_weight = True
            w = weight
        else:
            print("Weight cannot be 0 or less!")
    except ValueError:
        print("Sorry, I didn't understand that.")

while not user_height:
    try:
        height = float(input("Enter your height in cm: "))
        if height > 0:
            print("Height entered successfully!")
            user_height = True
            h = height
        else:
            print("Height cannot be 0 or less!")
    except ValueError:
        print("Sorry, I didn't understand that.")

bmi = (w / (h / 100) ** 2)
dp_bmi = float("{:.2f}".format(bmi))

print("Your BMI is:", dp_bmi)

if dp_bmi < 18.5:
    print("You are underweight! ")
elif 18.5 <= dp_bmi <= 24.9:
    print("You are healthy!")
elif 25 <= dp_bmi <= 29.9:
    print("You are overweight!")
else:
    print("You are obese!")
