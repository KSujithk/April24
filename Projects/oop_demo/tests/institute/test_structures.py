"""
This test cases test the institute structures
"""
from learning.institute.structure import Course, Student

def test_student_course():
    """Testing the basic functionality
    """
    python_course = Course(
        "x123",
        "Python"
    )
    devops_course = Course(
        "x121",
        "DevOps"
    )
    cloud_course = Course(
        "x121",
        "DevOps"
    )
    student = Student(
        student_id = "s1001",
        name = "Abhay"
    )

    assert len(student.courses) == 0
    # now lets enroll student to python
    student.enroll_course(python_course)
    assert len(student.courses) == 1
    student.enroll_course(devops_course)
    assert len(student.courses) == 2
    student.enroll_course(cloud_course)
    assert len(student.courses) == 3
