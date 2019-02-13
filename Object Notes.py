import Special_Random


class Laptop(object):
    def __init__(self, screen_resolution, extra_space=1000, color="Blue"):
        # Things that a Laptop has.
        # Everything in this list would be relevant to the program.
        self.processor = "Intel i5"
        self.screen_resolution = screen_resolution
        self.battery_left = 100
        self.space_left = extra_space
        self.color = color
        self.os = "Linux"
        self.functioning = True

    def charge(self, time):
        if self.functioning:
            # Computer is already charged.
            if self.battery_left >= 100:
                print("The computer is already charged.")
                return

            self.battery_left += time
            # Computer is mostly charged.
            if self.battery_left > 100:
                print("The computer quickly charges.")
                self.battery_left = 100

            # Computer is not charged at all.
            else:
                print("The computer is on at %d%% " % self.battery_left)
        else:
            print("It's broken. Good job.")

    def smash(self):
        self.functioning = False
        print("I took the laptop...")
        print()
        print("...wait for it...")
        print()
        print("...AND I THREW IT ON THE GROUND!!!!!")

    def use(self, time):
        self.battery_left -= time
        print("You use the laptop for %s minutes" % time)


my_computer = Laptop("1920x1080", 10000, "Black")
your_computer = Laptop("10x10", 0, "Orange")
wiebe_computer = Laptop("900000000000x900000000", 9999999999999999, "Awesome")
default_computer = Laptop("1920x1080")

my_computer.use(60)
my_computer.charge(1000)
my_computer.smash()
my_computer.charge(20)

your_computer.charge(20)

print(Special_Random.RandomWiebe.special_random())
