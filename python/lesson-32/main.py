# Parent class
class Laptop:
    def parts(self):
        print("Keyboard, Display, Motherboard")

# Adding an additional method to the Desktop class
class Desktop(Laptop):
    def weight(self):
        print("Desktops are heavyweight")

# Create objects and call methods
my_laptop = Laptop()
my_laptop.parts()  # Output: Keyboard, Display, Motherboard

my_desktop = Desktop()
my_desktop.parts()  # Output: Keyboard, Display, Motherboard



# Create object and call the new method
my_desktop = Desktop()
my_desktop.parts()  # Output: Keyboard, Display, Motherboard
my_desktop.weight()  # Output: Desktops are heavyweight