

def number_sum(number):
    if number > 0:
        return sum(int(i) for i in str(number))
    return 'Invalid number.'


print(number_sum(15))
print(number_sum(0))
