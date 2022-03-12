from time import time

from shift import Shift


class Employee:
    def __init__(self, first_name: str, last_name: str, salary: int, shift):
        self._first_name = first_name
        self._last_name = last_name
        self.salary = salary
        self.shift = shift

    def get_full_name(self):
        return f"{self._first_name} {self._last_name}"

class Manager(Employee):
    job_title = "Manager"

class Developer(Employee):
    job_title = "Developer"

class Tester(Employee):
    job_title = "Tester"
