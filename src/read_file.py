try:
  employee_file = open("employee", "r")
  #print(employee_file.readable())

  #for employee in employee_file.readlines():
    #print(employee)
  emp_name = []
  emp_des = []
  for employee in employee_file.readlines():
    emp = employee.split(",")
    emp_name.append(emp[0].strip())
    emp_des.append(emp[1].strip())

  print(emp_name)
  print(emp_des)
except FileNotFoundError as err:
  print(err)
finally:
  employee_file.close()