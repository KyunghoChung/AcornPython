from AudioTVParent import AudioTVParent

# 상속 표형: class 자식클래스(부모클래스)
class Audio(AudioTVParent):
    def __init__(self, power, volume):
        # super() : 생성자
        super().__init__(power, volume)

    def tune(self):
        str01 = "ha ha ha..." if self.power else "turn it on"
        # 아래는 삼중 연산자의 if문 형태
        # if self.power:
        #     str01 = "ha ha ha..."    
        # else:
        #     str01 = "turn it on"
        print(str01)