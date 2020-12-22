num1 = 0
miles = 0.621371
kilometres = 1.60934
answer = 0

num1 = input("What number would you to convert?")

op = input("Would you to convert into miles of kilometres?")


if op == "miles":
    answer = float(num1) * float(0.621371)
    print(answer)


if op == "kilometres":
    answer = float(num1) * float(1.60934)
    print(answer)


