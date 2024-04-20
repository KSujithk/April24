

def is_even(number) -> bool:
    """This method determines if the number is even or not
    """
    if number <= 0:
        return False
    return number%2 == 0

def print_fibbonacci_sequence(end: int) -> None:
    """This method prints the fibonnaci sequence till end value passed

    Args:
      end(int): prints fibbonaci sequence till end
    """
    if end <= 1:
        return None
    first = 1
    second = 2
    print(first, end=" ")
    print(second, end=" ")
    while True:
        third = first + second
        if third > end:
            return None
        print(third, end=" ")
        first = second
        second = third


def get_fibbonaci_sequence(end):
    """This method returns the fibonnaci sequence till end value passed

    Args:
      end(int): prints fibbonaci sequence till end

    Returns:
      list of numbers
    """
    if end <= 2:
        return None
    first = 1
    second = 2
    fibbonacci_sequence = [] # list
    fibbonacci_sequence.append(first)
    fibbonacci_sequence.append(second)
    while True:
        third = first + second
        if third > end:
            return fibbonacci_sequence
        fibbonacci_sequence.append(third)
        first = second
        second = third


def project_euler_2():
    """Solution of project euler 2
    """
    # lets solve project euler problem 2
    max = 4000000
    sequence = get_fibbonaci_sequence(max)
    print("fibonnaci under 4million are")
    print(sequence)
    even_sequence = []
    for item in sequence:
        if is_even(item):
            even_sequence.append(item)
    print("even numbers in sequence are as follows")
    print(even_sequence)
    # sum of all of the sequnce
    sum_of_even_fibbonaci = sum(even_sequence)
    print(sum_of_even_fibbonaci)
