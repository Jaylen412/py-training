import importlib
import os

import pytest

mod = importlib.import_module(
    "sol_09_03" if os.environ.get("COURSE_SOLUTIONS") else "ex_09_03"
)


def test_salaried_employee():
    ada = mod.SalariedEmployee("Ada", 60000)
    assert ada.name == "Ada"
    assert ada.monthly_pay() == pytest.approx(5000.0)
    assert ada.describe() == "Ada: 5000.00"


def test_salaried_employee_is_an_employee():
    assert isinstance(mod.SalariedEmployee("Ada", 1), mod.Employee)


def test_hourly_employee_no_overtime():
    assert mod.HourlyEmployee("Alan", 20, 100).monthly_pay() == pytest.approx(2000.0)
    assert mod.HourlyEmployee("Alan", 20, 160).monthly_pay() == pytest.approx(3200.0)


def test_hourly_employee_overtime():
    assert mod.HourlyEmployee("Alan", 20, 170).monthly_pay() == pytest.approx(3500.0)


def test_hourly_employee_zero_hours():
    assert mod.HourlyEmployee("Linus", 30, 0).monthly_pay() == 0


def test_manager_pay_and_describe():
    grace = mod.Manager("Grace", 48000, 2000)
    assert grace.monthly_pay() == pytest.approx(6000.0)
    assert grace.describe() == "Grace: 6000.00 (manager)"


def test_manager_is_salaried_employee():
    grace = mod.Manager("Grace", 48000, 2000)
    assert isinstance(grace, mod.SalariedEmployee)
    assert grace.annual_salary == 48000


def test_team_totals():
    team = mod.Team("Data")
    team.add(mod.SalariedEmployee("Ada", 60000))
    team.add(mod.HourlyEmployee("Alan", 20, 170))
    team.add(mod.Manager("Grace", 48000, 2000))
    assert team.total_monthly_pay() == pytest.approx(14500.0)
    assert team.highest_paid() == "Grace"


def test_team_empty():
    team = mod.Team("Empty")
    assert team.members == []
    assert team.total_monthly_pay() == 0
    assert team.highest_paid() is None
