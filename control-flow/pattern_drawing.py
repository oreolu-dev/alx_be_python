number = int(input("Enter the size of the pattern: "))

while number <= 0:
    print("You must enter a positive integer!")
    number = int(input("Enter the size of the pattern(i.e., length of each square): "))

row = 0
while row < number:
    for i in range(number):
        print("*", end="")
    print()
    row += 1

    