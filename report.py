class AccountReport:
    def __init__(self, emp_list):
        self._emp_list = emp_list
        
    def print_account_report(self):
        print("Account Report")
        print("==============")
        for e in self._emp_list:
            print(f"{e.get_full_name()}, ${e.salary}")

class StaffReport:
    def __init__(self, emp_list):
        self._emp_list = emp_list

    def print_staff_report(self):
        print("Staff Report")
        print("============")
        for e in self._emp_list:
            print(f"{e.get_full_name()}, {e.job_title}")