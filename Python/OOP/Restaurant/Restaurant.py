class Restaurant():

    """
    A simple attempt to model a restaurant. 
    """
    def __init__(self, restaurant_name, cuisine_name):
        """
        Initialize restaurant_name and cuisine_name attributes. 
        """
        self.restaurant_name = restaurant_name
        self.cuisine_name = cuisine_name
        self.number_served = 0

    def toString(self):
        """
        Returns a human-readable string containing the restaurant attributes. 
        """
        prompt = "Restaurant Name: " + str(self.restaurant_name) + "\n"
        prompt += "Restaurant Cuisine Name: " + str(self.cuisine_name) + "\n" 
        return prompt
    
    def open_restaurant(self):
        """
        Opens the restaurant. 
        """
        return "The restaurant is open"
    
    def set_number_served(self, number_served):
        """
        Set the customers number served to the new given value.
        """
        if(number_served < 0):
            print("The value of customers served can't be negative")
        else:
            self.number_served = number_served
    def increment_number_served(self, number_served_addition):
        """Add the given amount to the customer number served"""
        if(number_served_addition < 0):
            print("The value of customers served can't be negative")
        else: 
            self.number_served += number_served_addition


        