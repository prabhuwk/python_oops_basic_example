from employee import Manager, Developer, Tester
from report import AccountReport, StaffReport, ScheduleReport
import datetime

employees = [
    Manager("Jack", "Brown", 4000, datetime.time(8, 00), datetime.time(14, 00)),
    Developer("Jill", "Jones", 3000, datetime.time(12, 00), datetime.time(20, 00)),
    Developer("Chris", "Dawn", 3000, datetime.time(8, 00), datetime.time(14, 00)),
    Tester("Dane", "Joey", 2500, datetime.time(12, 00), datetime.time(20, 00)),
]

reports = [
    AccountReport(employees),
    StaffReport(employees),
    ScheduleReport(employees)
]

for r in reports:
    r.print_report()
    print()
