employee_file = open("employee", "r")
#print(employee_file.readable())

#for employee in employee_file.readlines():
  #print(employee)
emp_name = []
emp_des = []
for employee in employee_file.readlines():
  emp = employee.split(",")
  emp_name.append(emp[0])
  emp_des.append(emp[1].strip())

print(emp_name)
print(emp_des)