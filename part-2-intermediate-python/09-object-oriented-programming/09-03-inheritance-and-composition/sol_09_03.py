"""Solutions for 09-03 Inheritance and composition."""

OVERTIME_THRESHOLD = 160


class Employee:
    """Base class for all employees."""

    def __init__(self, name):
        self.name = name

    def monthly_pay(self):
        raise NotImplementedError("subclasses must implement monthly_pay()")

    def describe(self):
        return f"{self.name}: {self.monthly_pay():.2f}"


class SalariedEmployee(Employee):
    def __init__(self, name, annual_salary):
        super().__init__(name)
        self.annual_salary = annual_salary

    def monthly_pay(self):
        return self.annual_salary / 12


class HourlyEmployee(Employee):
    def __init__(self, name, hourly_rate, hours):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours = hours

    def monthly_pay(self):
        regular_hours = min(self.hours, OVERTIME_THRESHOLD)
        overtime_hours = max(self.hours - OVERTIME_THRESHOLD, 0)
        return regular_hours * self.hourly_rate + overtime_hours * self.hourly_rate * 1.5


class Manager(SalariedEmployee):
    def __init__(self, name, annual_salary, monthly_bonus):
        super().__init__(name, annual_salary)
        self.monthly_bonus = monthly_bonus

    def monthly_pay(self):
        return super().monthly_pay() + self.monthly_bonus

    def describe(self):
        return super().describe() + " (manager)"


class Team:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add(self, employee):
        self.members.append(employee)

    def total_monthly_pay(self):
        return sum([member.monthly_pay() for member in self.members])

    def highest_paid(self):
        if not self.members:
            return None
        best = self.members[0]
        for member in self.members:
            if member.monthly_pay() > best.monthly_pay():
                best = member
        return best.name
