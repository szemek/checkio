def total_cost(calls):
    data = map(extract, calls)

    durations = {}

    for (date, duration) in data:
        duration = minutes(duration)
        durations[date] = durations.get(date, 0) + duration

    cost = 0

    for (date, duration) in durations.iteritems():
        if duration <= 100:
            cost += duration
        else:
            duration -= 100
            cost += 100 + 2 * duration

    return cost

def extract(log):
    date, _, duration = log.split(' ')
    return [date, int(duration)]

def minutes(duration):
    minutes, seconds = divmod(duration, 60)

    if seconds > 0:
        minutes += 1

    return minutes

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert total_cost((u"2014-01-01 01:12:13 181",
                       u"2014-01-02 20:11:10 600",
                       u"2014-01-03 01:12:13 6009",
                       u"2014-01-03 12:13:55 200")) == 124, "Base example"
    assert total_cost((u"2014-02-05 01:00:00 1",
                       u"2014-02-05 02:00:00 1",
                       u"2014-02-05 03:00:00 1",
                       u"2014-02-05 04:00:00 1")) == 4, "Short calls but money..."
    assert total_cost((u"2014-02-05 01:00:00 60",
                       u"2014-02-05 02:00:00 60",
                       u"2014-02-05 03:00:00 60",
                       u"2014-02-05 04:00:00 6000")) == 106, "Precise calls"
