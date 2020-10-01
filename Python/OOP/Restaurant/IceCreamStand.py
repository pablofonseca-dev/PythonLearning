from Restaurant import Restaurant
class IceCreamStand(Restaurant):

    """
    A simple attempt to model an ice cream stand.
    """
    def __init__(self, restaurant_name, cuisine):
        super().__init__(restaurant_name, cuisine)
        self.flavors = []

    def add_flavor(self, flavor_name):
        """
        Add an icecream flavor to the list of flavors. 
        """
        self.flavors.append(flavor_name)
    def reset_flavors(self):
        """
        Deletes all the icecream flavors that were added. 
        """
        self.flavors = []
    def describe_flavors(self):
        """
        Return a string with all the flavors added to the Ice Cream Stand.
        """
        list_of_flavors = ""
        counter = 0
        for i in self.flavors:
            list_of_flavors += str(counter + 1) + "- " + str(i) + "\n"
            counter += 1
        return list_of_flavors


myIceCreamStand = IceCreamStand("Heladeria Otaku", "Otakers Cuisine") 

myIceCreamStand.add_flavor("Chocolate")
myIceCreamStand.add_flavor("Vanilla")
myIceCreamStand.add_flavor("Cheesecake")

flavors = myIceCreamStand.describe_flavors()

print(flavors)