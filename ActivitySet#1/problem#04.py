# Conditional Execution

hrs = float(input("Enter hours? "))
h = float(hrs)
rate = float(input("Enter rate? "))
r = float(rate)
pay=hrs*rate
if hrs>40:
  extratime = (hrs-40)*(rate*0.5)
  Salary = (hrs*rate) + extratime
else:
  Salary = hrs*rate
print(Salary)