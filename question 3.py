number = int(input("Enter the number: "))
reverse_number = 0
while number > 0:
    reverse_number = (reverse_number * 10) + number % 10
    number = number / 10
    number = int(number)
print("reversed number = ", reverse_number)
