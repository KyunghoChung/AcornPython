class AudioTVParent:
    def __init__(self, power, volume):
        self.power = power
        self.volume = volume

    def switch(self, onOff):
        self.power = onOff

    def set_volume(self, vol):
        self.volume = vol