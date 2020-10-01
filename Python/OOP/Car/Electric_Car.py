from Car import Car
from Battery import Battery
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery();
        

    #Override
    def fill_gas_tank(self):
        """
        Electric cars don't have gas tanks
        """
        print("This car doesn't have a gas tank, is electric!");
        

my_tesla = ElectricCar('tesla', 'Model S', '2016')

print(my_tesla.get_descriptive_name())

print(my_tesla.battery.describe_battery(), end="\n");