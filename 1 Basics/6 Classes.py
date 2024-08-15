#  we will be learnign classes in Python


# class Vehicle():
#     # init initials the data
#   def __init__(self , bodystyle):
#     self.bodystyle = bodystyle


# class Car(Vehicle):
#   def __init__(self, enginetype):
#     # we use the super function to initialize the super class
#     super().__init__("Car")
#     self.wheels =4
#     self.doors =4
#     self.enginetype = enginetype

# class Motorcycle(Vehicle):
#   def __init__(self, enginetype,hassidecar):
#     super().__init__("Motorcycle")
#     if (hassidecar):
#       self.wheels = 3
#     else: 
#       self.wheels = 2
#       self.doors = 0
#       self.enginetype = enginetype

# car1 = Car("gas")
# car2 = Car("electric")
# mc1 = Motorcycle("gas",True)

# print(mc1.wheels)
# print(car1.enginetype)
# print(car2.doors)




# lets get these vehicles to drive

class Vehicle:
    # __init__ initializes the data
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle


    def drive(self, speed):
        self.mode = "driving"
        self.speed = speed

class Car(Vehicle):
    def __init__(self, enginetype):
        # Use the super function to initialize the superclass
        super().__init__("Car")
        self.wheels = 4
        self.doors = 4
        self.enginetype = enginetype

    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.enginetype, "car at", self.speed)

class Motorcycle(Vehicle):
    def __init__(self, enginetype, hassidecar):
        super().__init__("Motorcycle")
        if hassidecar:
            self.wheels = 3
        else:
            self.wheels = 2
        self.doors = 0
        self.enginetype = enginetype

    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.enginetype, "motorcycle at", self.speed)

# Create instances
car1 = Car("gas")
car2 = Car("electric")
mc1 = Motorcycle("gas", True)

# Print attributes
print(mc1.wheels)       # Output: 3
print(car1.enginetype)  # Output: gas
print(car2.doors)       # Output: 4

# Call drive method on objects
car1.drive(30)
car2.drive(40)
mc1.drive(50)