class Dog(object):
    def __init__(self, breed="pug", dob=2/4/5, color="Pale Gray", energy=100, gender="girl"):
        self.breed = breed
        self.color = color
        self.energy_left = energy
        self.dob = dob
        self.gender = gender
        self.functioning = True

    def energy(self, time):
        if self.functioning:
            if self.energy_left >= 100:
                print("Your dog is full of energy.")
                return
            self.energy_left += time

            if self.energy_left > 100:
                print("Your dog has some energy left.")
                self.energy_left = 100

            else:
                print("She needs a nap. She has %d left" % self.energy_left)
        else:
            print("She is trying not to hear your voice so you wouldn't take her out.")

    def tried(self):
        self.functioning = False
        print("Leave the dog alone please.")

    def play_time(self, time):
        self.energy_left -= time
        print("She played with you for about %s minutes" % time)
