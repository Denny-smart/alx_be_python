#using for loop to create a multiplication table

number = int(input("Enter a number to see its multiplication table: "))

for y in range(1, 11):
    print(f"{number} * {y} = {number * y}")
