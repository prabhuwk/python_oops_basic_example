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

employees = [
    Manager("Jack", 4000),
    Developer("Jill", 3000),
    Developer("Chris", 3000),
    Tester("Dane", 2500),
]

for e in employees:
    print(f"{e.name}, ${e.salary}, {e.job_title}")
