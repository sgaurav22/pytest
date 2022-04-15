try:
  emp_file = open("employee", "a")
  emp_file.write("\n")
  emp_file.write("Raman, Staff")
except FileNotFoundError as err:
  print(err)
finally:
  emp_file.close()
