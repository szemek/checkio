from datetime import date, timedelta

def checkio(from_date, to_date):
    delta = to_date - from_date
    days = delta.days + 1

    total = 0

    weeks, remainder = divmod(days, 7)
    total += 2 * weeks
    from_date = from_date + timedelta(days=weeks * 7)

    diff = to_date - from_date
    days = diff.days + 1

    weekdays = [(from_date + timedelta(offset)).weekday() for offset in range(days)]

    total += weekdays.count(5)
    total += weekdays.count(6)

    return total

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2, "1st example"
    assert checkio(date(2013, 1, 1), date(2013, 2, 1)) == 8, "2nd example"
    assert checkio(date(2013, 2, 2), date(2013, 2, 3)) == 2, "3rd example"

