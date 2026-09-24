# Complete the if and elif statements!
def grade_converter(grade: int) -> str:
    if grate >= 90:
        return "A"
    elif grate >= 80:
        return "B"
    elif grate >= 70:
        return "C"
    elif grate >= 65:
        return "D"
    else:
        return "F"


# This should print an "A"
print(grade_converter(92))

# This should print a "C"
print(grade_converter(70))

# This should print an "F"
print(grade_converter(61))
