# Python Object-Oriented Programming


class Employee:

    number_of_employees = 0
    raise_amount = 1.04

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = f'{first_name.lower()}.{last_name.lower()}@company.com'

        Employee.number_of_employees += 1

    def __repr__(self):
        return f"Employee({self.first_name}, {self.last_name}, {self.pay})"

    def __str__(self):
        return f'{self.fullname()} - {self.email}'

    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, employee_str):
        first_name, last_name, pay = employee_str.split('-')
        return cls(first_name, last_name, pay)

    @staticmethod
    def is_workday(day):
        return True if day.weekday() < 5 else False


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first_name, last_name, pay, prog_lang):
        super().__init__(first_name, last_name, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first_name, last_name, pay, employees=None):
        super().__init__(first_name, last_name, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def print_employees(self):
        for employee in self.employees:
            print('--> ' + employee.fullname())


employee_1 = Employee('Sam', 'Smith', 45000)
employee_2 = Employee('Jane', 'Doe', 45000)
developer_1 = Developer('John', 'Doe', 50000, 'Python')

manager_1 = Manager('Werner', 'Schmidt', 90000, [employee_1, developer_1])

print(repr(employee_1))
print(str(employee_1))
