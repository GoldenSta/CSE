class Camera(object):
    def __init__(self, screen_resolution, space_left=100, color="Rose Gold"):
        self.screen_resolution = screen_resolution
        self.color = color
        self.battery_left = 100
        self.pictures_left = space_left
        self.flashes = 10
        self.brightness = 100
        self.functioning = True

    def pictures(self, time):
        if self.functioning:
            if self.pictures_left <= 100:
                print("There is space left.")
                self.pictures_left -= time
