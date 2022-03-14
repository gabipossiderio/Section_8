

def time(hours, minutes, seconds):
    hours = hours * 3600
    minutes = minutes * 60
    return hours + minutes + seconds


print(time(10, 20, 55))
