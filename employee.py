class Employee:
    def __init__(self, name: str, salary: int):
        self.name = name
        self.salary = salary

class Manager(Employee):
    job_title = "Manager"

class Developer(Employee):
    job_title = "Developer"

class Tester(Employee):
    job_title = "Tester"
