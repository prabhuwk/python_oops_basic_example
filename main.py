from employee import Manager, Developer, Tester

employees = [
    Manager("Jack", 4000),
    Developer("Jill", 3000),
    Developer("Chris", 3000),
    Tester("Dane", 2500),
]

for e in employees:
    print(f"{e.name}, ${e.salary}, {e.job_title}")
