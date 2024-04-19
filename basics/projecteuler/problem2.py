first_in_sequence = 1
second_in_sequence = 2
sum = 2
while True:
    third_in_sequence = first_in_sequence + second_in_sequence
    if third_in_sequence > 4000000:
        break
    if third_in_sequence % 2 == 0:
        sum += third_in_sequence
    # swap values
    first_in_sequence = second_in_sequence
    second_in_sequence = third_in_sequence
print(sum)
