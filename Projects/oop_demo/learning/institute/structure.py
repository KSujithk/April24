"""This module defines the basic structures necessary
"""


class Course:
    """This represents Course"""

    def __init__(self, course_id: str, name: str) -> None:
        self.__course_id = course_id
        self.__name = name

    @property
    def name(self):
        """This property returns name"""
        return self.__name

    @property
    def course_id(self):
        """Course Id propert"""
        return self.__course_id


class Student:
    """
    This class Represents the student
    """

    def __init__(
        self,
        student_id: str,
        name: str,
    ) -> None:
        self.student_id = student_id
        self.name = name
        self.courses = []

    def enroll_course(self, course: Course):
        """We are enrolling student to a course"""
        self.courses.append(course)
