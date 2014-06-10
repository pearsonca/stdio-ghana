class Employee:
    'Common base for all employees'

    def __init__(self, name, salary = 20):
        self.name = name
        self.salary = salary

    def displayEmployee(self):
        print ("Name: ", self.name, ", Salary: ", self.salary)

if __name__ == "__main__":
    emp1 = Employee('name')
    emp1.displayEmployee()
    emp2 = Employee('name2', 25)
    emp2.displayEmployee()
