from time import time


class Employee:
    def __init__(self, first_name: str, last_name: str, salary: int, start_time: time, end_time: time):
        self._first_name = first_name
        self._last_name = last_name
        self.salary = salary
        self.start_time = start_time
        self.end_time = end_time

    def get_full_name(self):
        return f"{self._first_name} {self._last_name}"

class Manager(Employee):
    job_title = "Manager"

class Developer(Employee):
    job_title = "Developer"

class Tester(Employee):
    job_title = "Tester"
