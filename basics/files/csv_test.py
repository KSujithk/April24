import random
import csv
import os

def write_record(path,p,i,t,r):
    # find if file exists
    file_exists = False
    if os.path.exists(path):
        file_exists = True
    with open(path, 'a') as file:
        results_writer = csv.writer(file)
        results_writer.writerow([p,i,t,r])
        

    


def write_random_data():
    csv_path = "results.csv"
    for index in range(3):
        p = random.randint(1000,10000)
        i = random.randint(6,24)
        t = random.randint(1,10)
        r = random.randint(1000,10000)
        write_record(csv_path,p,i,t,r)

def read_results(file_path):
    with open(file_path, 'r') as reader:
        result_reader = csv.reader(reader,delimiter=',')
        for record in result_reader:
            print(record)




if __name__ == "__main__":
    write_random_data()
    #read_results("results.csv")