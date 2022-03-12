class Employee:
    def __init__(self, first_name: str, last_name: str, salary: int):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

class Manager(Employee):
    job_title = "Manager"

class Developer(Employee):
    job_title = "Developer"

class Tester(Employee):
    job_title = "Tester"
