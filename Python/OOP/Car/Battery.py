class Battery():
    def __init__(self, battery_size = 70):
        self.battery_size = battery_size

    def get_battery_size(self):
        """
        Return the battery size of the object. 
        """
        return self.battery_size
    
    def set_battery_size(self, newBatterySize):
        """
        Sets the battery size of the object. 
        """
        if(newBatterySize < 0):
            print("You can't set a negative size to the car battery");
        else: 
            if(newBatterySize != 85 or newBatterySize != 70):
                print("Invalid battery size")
            else:
                self.battery_size = newBatterySize; 
    def describe_battery(self):
        """
        Print a statement describing the battery size. 
        """
        print("This is a " + str(self.get_battery_size()) + "-KWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if(self.battery_size == 70)
            range = 240
        elif(self.battery_size == 85)
            range = 270 
        message = "This car can go approximately " + range + " miles on a full charge."
        print(message);