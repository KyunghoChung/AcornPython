from classAudio import Audio
from classTV import TV


obj01 = Audio(True, 15)
obj02 = TV(False, 12, 40)

obj01.set_volume(10)
obj01.tune()

obj02.switch(True)  # TV를 켰다
obj02.watch()
print(obj02.size)

