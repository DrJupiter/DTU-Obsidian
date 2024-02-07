class Student:
    def __init__(self, name, courses):
        """
        Initializes a new Student instance.

        :param name: A string representing the student's name.
        :param courses: A list of strings representing the course names the student is attending.
        """
        self.name = name
        self.courses = courses

    def attends(self, course):
        """
        Checks if the student is attending a given course.

        :param course: A string representing the course name to check.
        :return: True if the student is attending the course, False otherwise.
        """
        return course in self.courses

from typing import List
def coursestudents(students: List[Student], course_number: str) -> List[str]:
    return [student.name for student in students if student.attends(course_number)]