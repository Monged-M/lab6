class RegistrationError(Exception):
    pass

class Student:
    def __init__(self, student_id):
        self.student_id = student_id
        self.courses = {}
