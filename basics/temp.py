number = int(input("Enter the number: "))
result = 0
while True:
    result = result + (number%10)
    number = number // 10
    if result < 10 and number == 0:
        break
    if number == 0:
        number = result
        result = 0
print(result)
