class Report:
    def __init__(self, emp_list):
        self._emp_list = emp_list

class AccountReport(Report):
    def print_report(self):
        print("Account Report")
        print("==============")
        for e in self._emp_list:
            print(f"{e.get_full_name()}, ${e.salary}")

class StaffReport(Report):
    def print_report(self):
        print("Staff Report")
        print("============")
        for e in self._emp_list:
            print(f"{e.get_full_name()}, {e.job_title}")