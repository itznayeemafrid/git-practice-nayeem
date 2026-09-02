import datetime
from utils import add, subtract, divide

print("Name: Nayeem Islam")
print("Today's Date:", datetime.date.today())
print("5 + 3 =", add(5, 3))
print("10 - 4 =", subtract(10, 4))

try:
    print("10 / 0 =", divide(10, 0))
except ZeroDivisionError as e:
    print("Error:", e)