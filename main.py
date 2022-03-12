class Employee:
    def __init__(self, name: str, salary: int):
        self.name = name
        self.salary = salary

employees = [
    Employee("Jack", 4000),
    Employee("Jill", 3000),
    Employee("Chris", 3000),
    Employee("Dane", 2500),
]

for e in employees:
    print(f"{e.name}, ${e.salary}")
