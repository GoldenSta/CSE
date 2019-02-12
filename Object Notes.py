class Laptop(object):
    def __init__(self, screen_resolution, extra_space, color):
        # Things that a Laptop has
        # Everything in this list would be
        self.processor = "Intel i5"
        self.screen_resolution = screen_resolution
        self.battery_left = 100
        self.space_left = extra_space
        self.color = color
        self.os = "Linux"

    def charge(self, time):
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
            print("The computer is on  ")
