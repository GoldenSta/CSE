class Dog(object):
    def __init__(self, breed="pug", dob=2/4/5, color="Pale Gray", energy=100, gender="girl"):
        self.breed = breed
        self.color = color
        self.energy = energy
        self.dob = dob
        self.gender = gender
        self.functioning = True

    def energy(self, time):
        if self.functioning:
            if self.energy >= 100:
                print("Your dog is full of energy.")
                return
            self.energy += 100

            if self.energy > 100:
                print("Your dog has some energy left.")
                self.energy = 100

            else:
                print("")