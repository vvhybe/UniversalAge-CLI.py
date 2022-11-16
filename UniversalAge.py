from datetime import date as DATE, MAXYEAR, MINYEAR

class UniversalAge:
    __planets_rev = {"mercury": 87.97, "venus": 244.7, "earth": 365.25625, "mars": 686.68175, "jupiter": 4331.939125, "saturn": 10760.449125000001, "neptune": 60190.577437500004, "pluto": 90799.05118750001}

    def __init__(self, birthdate:str, planet="earth"):
        assert planet.lower() in UniversalAge.__planets_rev.keys()
        self.planet = planet.lower()
        self.birthdate = birthdate

    def age(self):
        bdate = UniversalAge.spread_date(self.birthdate)
        y, m, d = bdate["y"], bdate["m"], bdate["d"]
        daysdif = (DATE.today() - DATE(y,m,d)).days
        age = daysdif / UniversalAge.__planets_rev["earth"]
        return self.planet != "earth" and age / (UniversalAge.__planets_rev[self.planet] / UniversalAge.__planets_rev["earth"]) or age

    def tell_my_age(self):
        return f"Your age in planet of {self.planet} is {self.age():.2f} years old."

    @staticmethod
    def spread_date(date:str):
        #@ possible date combinatios: exclude "MM/DD/YYYY" but icludes "YYYY" as "01/01/YYYY"
        # 1999/12/7 or 7/12/1999
        # 7\12\1999 or 1999\12\7
        # 7-12-1999 or 1999-12-7
        # 7_12_1999 or 1999_12_7
        # 7.12.1999 or 1999.12.7
        date = len(date) == 4 and f"01/01/{date}" or date
        sep = [d for d in date if d in ["/", "\\", "-", "_", "."]]
        if not sep[0] == sep[1]: return (f"separator must be identical: sep1='{sep[0]}', sep2='{sep[1]}'")
        date = date.split(sep[0],3)
        y = int(date[0]) > 31 and date[0] or date[-1]
        m = date[1]
        d = y == date[0] and date[-1] or date[0]
        if int(date[1]) > 12 : return (f"date must be formated like: 'YYYY{sep[0]}MM{sep[0]}DD' or 'DD{sep[0]}MM{sep[0]}YYYY'")
        if int(y) > MAXYEAR or int(y) < MINYEAR : return (f"the year:'{y}' must be in range of '{MAXYEAR}' >= {y} >= '000{MINYEAR}'")
        return {"y":int(y), "m":int(m), "d":int(d)}
    
# birthdate = "07-12-1999"
birthdate = input("Enter your birthdate: ")
uage = UniversalAge(birthdate, "mercury")
print(uage.tell_my_age())
