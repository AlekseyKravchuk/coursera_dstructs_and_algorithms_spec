import zoneinfo
from datetime import datetime
from dateutil import tz

if __name__ == '__main__':
    # Eastern time
    et = tz.gettz('America/New_York')

    last = datetime(2022, 2, 10, 21, 16, 55, tzinfo=et)
    last2 = datetime(2022, 2, 10, 21, 16, 55, tzinfo=zoneinfo.ZoneInfo('America/Vancouver'))
    last3 = datetime(2022, 2, 10, 21, 16, 55, tzinfo=zoneinfo.ZoneInfo('Europe/Moscow'))
    print(last)
    print(last2)
    print(last3)

