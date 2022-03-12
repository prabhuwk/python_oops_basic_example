from employee import Manager, Developer, Tester
from report import AccountReport, StaffReport

employees = [
    Manager("Jack", "Brown", 4000),
    Developer("Jill", "Jones", 3000),
    Developer("Chris", "Dawn", 3000),
    Tester("Dane", "Joey", 2500),
]

reports = [
    AccountReport(employees),
    StaffReport(employees)
]

for r in reports:
    r.print_report()
    print()
