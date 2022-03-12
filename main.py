from employee import Manager, Developer, Tester

employees = [
    Manager("Jack", "Brown", 4000),
    Developer("Jill", "Jones", 3000),
    Developer("Chris", "Dawn", 3000),
    Tester("Dane", "Joey", 2500),
]

def print_account_report():
    print("Account Report")
    print("==============")
    for e in employees:
        print(f"{e.get_full_name()}, ${e.salary}")

def print_staff_report():
    print("Staff Report")
    print("============")
    for e in employees:
        print(f"{e.get_full_name()}, {e.job_title}")

print_account_report()
print()
print_staff_report()
