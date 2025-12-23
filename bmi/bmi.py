def calculate_bmi(weight, height):
    return weight / (height ** 2)


def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweigsad"
    else:
        return "Obese"


while True:
    print("\n--- BMI Calculator ---")

    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    height = float(input("Enter your height in meters: "))
    weight = float(input("Enter your weight in kilograms: "))

    bmi = calculate_bmi(weight, height)
    category = bmi_category(bmi)

    print(f"\n{name}, Age {age}")
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Category: {category}")

    another = input("\nWould you like to add another person? (yes/no): ").lower()
    if another != "yes":
        print("\nThank you for using the BMI Calculator!")
        break
