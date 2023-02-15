class Employee:

  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + '.' + last + '@gmail.com'

  def fullname(self):
    return '{} {}'.format(self.first,self.last)

emp_1 = Employee('Daniel', 'Santiago' , 60000)
emp_2 = Employee('Jose', 'Guisao', 50000)

print(emp_1.first,emp_1.last,emp_1.pay,emp_1.email)
print(emp_2.first,emp_2.last,emp_2.pay,emp_2.email)

print()
print(emp_1.fullname())
print(Employee.fullname(emp_1))
print('...end...')
