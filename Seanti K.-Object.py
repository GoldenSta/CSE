class Camera(object):
    def __init__(self, screen_resolution, pictures_left=100, color="Rose Gold"):
        self.screen_resolution = screen_resolution
        self.color = color
        self.battery_left = 100
        self.space_left = pictures_left
        self.os = "Samung"
        self.functioning = True

    def brightness(self, charge):
        if self.functioning:
                