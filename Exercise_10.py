

def greater_number(num1, num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    return 'You entered two identical numbers.'


print(greater_number(5, 5))
