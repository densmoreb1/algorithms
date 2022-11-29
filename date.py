def date_convert(date_convert: str):
    if not date_convert.replace(' ', ''):
        return 'E8430'

    try:
        m, d, y = date_convert.split('/')
    except:
        return 'E9021'
    
    if not 0 < int(m) < 13:
        return 'E1756'
    if not 0 < int(d) < 31:
        return 'E1756'
    
    return str((dt.datetime.strptime(date_convert, '%m/%d/%Y').date() - dt.datetime.today().date()).days)

import datetime as dt

print(date_convert('07/10/2023'))