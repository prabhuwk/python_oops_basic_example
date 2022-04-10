from abc import ABC, abstractmethod

class Report(ABC):
    def __init__(self, emp_list):
        self._emp_list = emp_list

    @abstractmethod
    def print_report(self):
        pass

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

class ScheduleReport(Report):
    def print_report(self):
        print("Schedule Report")
        print("============")
        for e in self._emp_list:
            print(f"{e.get_full_name()}, {e.shift.get_shift_info()}")
