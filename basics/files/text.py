import random

def write_result(principal, rate, time, result):
    """This functions appends the results to the end of the file
    """
    with open("results.csv", "a") as writer:
        writer.write(f"{principal},{rate},{time},{result}\n")

def read_results():
    with open("results.csv", "r") as reader:
        for line in reader.readlines():
            print(line)



if __name__ == "__main__":
    for index in range(3):
        p = random.randint(1000,10000)
        i = random.randint(6,24)
        t = random.randint(1,10)
        r = random.randint(1000,10000)
        write_result(p,i,t,r)
    read_results()

