# Functions


def computepay(h, r):
    return totalpay


h = float(input("Enter hours? "))
r = float(input("Enter rate per hour? "))

if h > 40:
  overtime = (h-40)*(r*0.5)
  totalpay = (h*r) + overtime

p = computepay(h, r)
print("Pay", p)