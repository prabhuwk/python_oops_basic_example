from employee import Manager, Developer, Tester
from report import AccountReport, StaffReport

employees = [
    Manager("Jack", "Brown", 4000),
    Developer("Jill", "Jones", 3000),
    Developer("Chris", "Dawn", 3000),
    Tester("Dane", "Joey", 2500),
]

account_report = AccountReport(employees)
account_report.print_account_report()

staff_report = StaffReport(employees)
staff_report.print_staff_report()
