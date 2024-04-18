maths = int(input("Enter the marks of maths: "))
science = int(input("Enter the marks of science: "))
social = int(input("Enter the marks of social: "))
average = (maths + science + social) // 3

if average >= 90 and average <= 100:
    print("A1")
elif average >= 80 and average < 90:
    print("A2")
elif average >= 70 and average < 80:
    print("B1")
elif average >= 60 and average < 70:
    print("B2")
elif average >= 50 and average < 60:
    print("C1")
elif average >= 40 and average < 50:
    print("C2")
elif average >= 33 and average < 40:
    print("D")
elif average <= 32:
    print("F")
else:
    print("Enter marks not petrol prices")