# Define the Person class
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    # Method to introduce the person
    def introduce(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old, and I am {self.gender}.")

# Create an instance of the Person class
person1 = Person("Alex", 26, "Male")

# Call the introduce method to display the person's information
person1.introduce()
