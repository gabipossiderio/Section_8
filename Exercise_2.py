def date(day=4, month=4, year=1995):
    months_full = {
        '1': 'january',
        '2': 'february',
        '3': 'march',
        '4': 'april',
        '5': 'may',
        '6': 'june',
        '7': 'july',
        '8': 'august',
        '9': 'september',
        '10': 'october',
        '11': 'november',
        '12': 'december'
    }
    if str(month) in months_full.keys():
        print(f'The date inputted was {months_full[str(month)]} {day}, {year}.')


date(day=5, month=5, year=1996)
