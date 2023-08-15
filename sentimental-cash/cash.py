# TODO
from cs50 import get_float
import math
var = True
while var:
    amt = get_float("Enter Amount: ")
    if amt < 0:
        continue
    else:
        var = False
c = 0
amt = round(amt * 100)  # rounding and multiplying with zero so that
# I don't have to care about precision.

while (amt >= 0):  # = 0 because it should run the final print command
    if amt >= 25:
        amt = amt - 25
        c += 1
    elif amt >= 10:
        amt = amt - 10
        c += 1
    elif amt >= 5:
        amt = amt - 5
        c += 1
    elif amt >= 1:
        amt = amt - 1
        c += 1
    else:
        print(c)
        break
