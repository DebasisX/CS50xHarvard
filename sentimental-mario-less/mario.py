# TODO
from cs50 import get_int
var = True
while var:
    height = get_int("Enter HEIGHT: ")
    if (0 < height < 9):
        var = False
for i in range(height):
    for j in range(height - (i + 1), 0, -1):
        print(" ", end="")
    for k in range(i + 1):
        print("#", end="")
    print("")