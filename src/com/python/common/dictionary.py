# dictionaries are same as map. which stores key value pair

monthConversion = {
  "Jan" : "January",
  "Feb" : "Febuary",
  "Mar" : "March"
}

print(monthConversion["Jan"])

print(monthConversion.get("Feb"))

monthConversionFromNumber = {
  1 : "January",
  2 : "Febuary",
  3 : "March"
}

print(monthConversionFromNumber[1])
print(monthConversionFromNumber[2])
