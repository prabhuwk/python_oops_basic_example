from employee import Manager, Developer, Tester
from report import AccountReport, StaffReport, ScheduleReport
from shift import MorningShift, AfternoonShift
employees = [
    Manager("Jack", "Brown", 4000, MorningShift()),
    Developer("Jill", "Jones", 3000, AfternoonShift()),
    Developer("Chris", "Dawn", 3000, MorningShift()),
    Tester("Dane", "Joey", 2500, AfternoonShift()),
]

reports = [
    AccountReport(employees),
    StaffReport(employees),
    ScheduleReport(employees)
]

for r in reports:
    r.print_report()
    print()
