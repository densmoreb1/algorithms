# https://www.hackerrank.com/challenges/time-conversion/problem
# convert AM PM time to military time

def timeConversion(s):
    AM_PM = s[-2:]
    s = s[:8]
    hh, mm, ss = [int(x) for x in s.split(":")]

    if AM_PM == 'PM' and hh != 12:
        return ('{:02}:{:02}:{:02}'.format(hh + 12, mm, ss))
    elif AM_PM == 'AM' and hh == 12:
        return ('{:02}:{:02}:{:02}'.format(0, mm, ss))
    else:
        return ('{:02}:{:02}:{:02}'.format(hh, mm, ss))


def time2(s):
    ap = s[-2:]
    h, m, s = [int(x) for x in s[:8].split(':')]

    if ap == "PM":
        return f"{h % 12 + 12:02}:{m:02}:{s:02}"
    else:
        return f"{h % 12:02}:{m:02}:{s:02}"


print(time2('07:05:45PM'))
