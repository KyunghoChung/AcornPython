from AudioTVParent import AudioTVParent

class TV(AudioTVParent):
    def __init__(self, power, volume, size):
        super().__init__(power, volume)
        self.size = size

    def watch(self):
        str02 = "Have fun" if self.power else "Switch it on"
        print(str02)

    