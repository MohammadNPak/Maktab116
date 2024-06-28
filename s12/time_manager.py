

class DateTime:
    origin = {"year": 1970, "month": 1, "day": 1,
              "hour": 0, "minute": 0, "second": 0}

    def __init__(self, year, month, day, hour, minute, second) -> None:
        self._seconds = DateTime.datetime2second(
            year, month, day, hour, minute, second)

    @property # getter method
    def year(self):
        return self.origin["year"]+self._seconds//(365*24*60*60)

    @year.setter
    def year(self,value):
        if value<0:
            raise ValueError("year must be grater than zero")
        self._seconds -= self.year*12*30*24*60*60
        self._seconds += value*12*30*24*60*60



    @classmethod
    def second2datetime(cls, second):
        year, r = divmod(second, 365*24*60*60)
        month, r = divmod(r, 30*24*60*60)
        day, r = divmod(r, 24*60*60)
        hour, r = divmod(r, 60*60)
        minute, second = divmod(r, 60)
        return (cls.origin["year"]+year,
                cls.origin["month"]+month,
                cls.origin["day"]+day,
                cls.origin["hour"]+hour,
                cls.origin["minute"]+minute,
                cls.origin["second"]+second)

    @classmethod
    def datetime2second(cls, year, month, day, hour, minute, second):
        seconds_from_origin = ((year-cls.origin["year"])*365 +
                               (month-cls.origin["month"])*30 +
                               (day-cls.origin["day"]))*24*60*60 + (
            (hour-cls.origin["hour"])*3600 +
            (minute-cls.origin["minute"])*60 +
            (second-cls.origin["second"]))
        return seconds_from_origin

    def __str__(self) -> str:
        date_time = DateTime.second2datetime(self._seconds)
        return f"DateTime(year:{date_time[0]},month:{date_time[1]},day:{date_time[2]},hour:{date_time[3]},minute:{date_time[4]},second:{date_time[5]})"


    def __gt__(self,other):
        if self._seconds > other._seconds:
            return True
        return False
    


d1 = DateTime(1991, 3, 23, 12, 0, 0)
d2 = DateTime(1991, 3, 24, 21, 10, 25)
print(d1>d2)
# print(d1.year())
print(d1.year)
d1.year = 1995
print(d1)

