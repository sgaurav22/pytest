try:
   #result = 10/0
   value = int(input("Enter integer value : "))
   print(value)
except ZeroDivisionError as err:
  print(err)
except ValueError as err:
  print("invalid input")
finally:
  print("graceful closing")
