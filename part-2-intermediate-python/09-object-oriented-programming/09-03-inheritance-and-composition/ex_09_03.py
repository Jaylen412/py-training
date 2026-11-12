"""Exercises for 09-03 Inheritance and composition."""


class Employee:
    """Base class for all employees. Already complete: do not change it."""

    def __init__(self, name):
        self.name = name

    def monthly_pay(self):
        raise NotImplementedError("subclasses must implement monthly_pay()")

    def describe(self):
        return f"{self.name}: {self.monthly_pay():.2f}"


class SalariedEmployee(Employee):
    """An employee paid a fixed annual salary."""

    def __init__(self, name, annual_salary):
        """Call the parent __init__, then store annual_salary."""
        raise NotImplementedError

    def monthly_pay(self):
        """Return the annual salary divided by 12.

        Example: SalariedEmployee("Ada", 60000).monthly_pay() returns 5000.0
        """
        raise NotImplementedError


class HourlyEmployee(Employee):
    """An employee paid by the hour, with overtime."""

    def __init__(self, name, hourly_rate, hours):
        """Call the parent __init__, then store hourly_rate and hours
        (hours worked this month)."""
        raise NotImplementedError

    def monthly_pay(self):
        """The first 160 hours are paid at hourly_rate; any hours above 160
        are paid at 1.5 times hourly_rate.

        Example: HourlyEmployee("Alan", 20, 170).monthly_pay() returns 3500.0
        """
        raise NotImplementedError


class Manager(SalariedEmployee):
    """A salaried employee who also gets a fixed monthly bonus."""

    def __init__(self, name, annual_salary, monthly_bonus):
        """Use super().__init__ for name and salary, then store monthly_bonus."""
        raise NotImplementedError

    def monthly_pay(self):
        """Salaried monthly pay (use super()) plus the bonus."""
        raise NotImplementedError

    def describe(self):
        """The parent's describe() followed by " (manager)".

        Example: "Grace: 6000.00 (manager)"
        """
        raise NotImplementedError


class Team:
    """A team HAS employees (composition)."""

    def __init__(self, name):
        """Store the name and start with an empty list called members."""
        raise NotImplementedError

    def add(self, employee):
        """Add an employee to the team."""
        raise NotImplementedError

    def total_monthly_pay(self):
        """Return the sum of every member's monthly_pay()."""
        raise NotImplementedError

    def highest_paid(self):
        """Return the name of the member with the highest monthly pay,
        or None if the team is empty."""
        raise NotImplementedError
