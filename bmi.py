def calculate_bmi(height, weight):
    bmi = weight / (height ** 2)
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    print("BMI = " + str(round(bmi, 2)))

    if bmi < 18.5:
        print("You are underweight")
        return -1
    elif bmi >= 18.5 and bmi <= 25.0:
        print("You have a normal weight")
        return 0
    else:
        print("You are overweight")
        return 1

calculate_bmi(weight=57, height=1.73)