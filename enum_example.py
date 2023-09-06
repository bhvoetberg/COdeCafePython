from enum import Enum, auto
from typing import List


class Role(Enum):
    PRESIDENT = auto()
    VICEPRESIDENT = auto()
    INTERN = auto()
    MANAGER = auto()


class Employee:
    role = Role
    name = str


class Company:
    def __int__(self) -> None:
        self.employees = List[Employee]

    def add_employee(self, employee: Employee) -> None:
        self.employees.append(employee)

    def find_employee_role(self, role: Role) -> List[Employee]:
        return [employee for employee in self.employees if employee.role == role]

        # vs
        # employees = []
        # for employee in self.employees:
        #     if employee.role == role:
        #         employees.append(employee)
        # return employees


# def main() -> None:
a_company = Company()
henk = Employee
henk.role = Role.VICEPRESIDENT
a_company.add_employee(henk)
print('8888')
print(a_company.find_employee_role(Role.VICEPRESIDENT))
