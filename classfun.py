class Car:
    make = None
    model = None
    __theYear = None
    count = 0

    @property
    def description(self):
        Car.count += 1
        if self.__theYear and self.make and self.model:
            return str(self.__theYear) + ' ' + self.make + ' ' + self.model
        else:
            return 'Unknown'

    def get_year(self):
        return self.__theYear

    def set_year(self, year):
        self.__theYear = year

    year = property(get_year, set_year)

    @classmethod
    def fleet_size(cls):
        return cls.count

    @staticmethod
    def define():
        print("A car carries one or more people and has 4 wheels.")


class Jeep(Car):
    def __init__(self):
        super().__init__()
        self.make = 'Jeep'
        self.trailRated = True

# playground
# ride = Car()
# print("Description:", ride.description)

funRide = Jeep()
funRide.model = 'Wrangler'
funRide.year = 2015
print("Description:", funRide.description)

plainRide = Car()
plainRide.make = 'Ford'
plainRide.model = 'Tempo'
plainRide.set_year(1989)
print("Description:", plainRide.description)

otherRide = Car()
otherRide.make = 'Ford'
otherRide.model = 'LTD'
otherRide.set_year(1977)
print("Description:", otherRide.description)

print("There are", Car.fleet_size(), 'cars.')
Jeep.define()
