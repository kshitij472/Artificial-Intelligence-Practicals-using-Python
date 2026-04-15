# implement a basic Ai agent with simple decision making rules

temp = int(input("enter temperature: "))
hungry_input = input("are you hungry? (yes/no):").lower()

hungry = True if hungry_input == "yes" else False

if temp > 25:
    print("It's Hot - Turn on the fan")
elif hungry:
    print("I'm hungry - eat food")
else:
    print("All good - relex")