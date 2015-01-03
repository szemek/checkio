from math import fabs

def clock_angle(time):
    hours, minutes = map(lambda x:int(x), time.split(':'))
    hours %= 12

    hour_hand_angle = hours * 30.0 + minutes / 2.0
    minute_hand_angle = minutes * 6.0

    result = fabs(hour_hand_angle - minute_hand_angle)

    if result > 180.0:
        result = 360.0 - result

    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert clock_angle("02:30") == 105, "02:30"
    assert clock_angle("13:42") == 159, "13:42"
    assert clock_angle("01:42") == 159, "01:42"
    assert clock_angle("01:43") == 153.5, "01:43"
    assert clock_angle("00:00") == 0, "Zero"
    assert clock_angle("12:01") == 5.5, "Little later"
    assert clock_angle("18:00") == 180, "Opposite"
