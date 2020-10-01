class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """
        Initialize name and age attributes.
        """
        self.name = name 
        self.age = age

    def sit(self):
        """
        Simulate a dog sitting in response to a command.
        """
        print(f"{self.name.title()} is now sitting.")

    def roll_over(self):
        """
        Simulate rolling over in response to a command. 
        """
        print(f"{self.name.title()} rolled over!")


my_dog = Dog("Tommy", 12)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.");
