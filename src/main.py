# Main execution script for calculator functions

import datetime
from utils import add, subtract

print("Name: Nayeem Islam")
print("Today's Date:", datetime.date.today())
print("5 + 3 =", add(5, 3))
print("10 - 4 =", subtract(10, 4))
try:
    print("10 / 0 =", divide(10, 0))
except ValueError as e:
    print("Error:", e)