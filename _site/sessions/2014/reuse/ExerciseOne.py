import datetime as dt
import math as mt


class Employee():

    pay_scale_list = [500, 500, 800, 800, 1000, 1000, 1000, 1000, 1100, 1100, 1100, 1100, 1200]

    def __init__(self, name, start_date):
        self.name = name
        self.start_date = start_date

    def calc_pay(self):
        now = dt.date.today()
        start = self.start_date
        service = now - start
        pay_step = mt.floor(service.days / 365)

        if pay_step > 12:
            pay_step = 12

        pay = Employee.pay_scale_list[pay_step]

        print(self.name + ":" + str(pay))



employee_list = list()

employee_list.append(Employee("Andrewe", dt.date(2012, 8, 1)))
employee_list.append(Employee("Barbara", dt.date(2004,1,19)))
employee_list.append(Employee("Claire", dt.date(2007,11,30)))
employee_list.append(Employee("Daniel", dt.date(2001,5,23)))
employee_list.append(Employee("Edith", dt.date(2010,7,4)))

for employee in employee_list:
    employee.calc_pay()
