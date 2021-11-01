import time


class TrafficLight:
    __color = "красный" # можно пустую

    def swicth_lights(self, light: str, s: int):
        """меняет аттрибут __color на параметр light, задерживает скрипт на s секунд"""
        TrafficLight.__color = light # меняем аттрибут
        print(TrafficLight.__color)
        time.sleep(s) # задержка на n секунд

    def running(self):
        """переключает светофор в последовательности красный-желлтый-зеленый"""
        self.swicth_lights("красный", 7)
        self.swicth_lights("желтый", 2)
        self.swicth_lights("зеленый", 3)


a = TrafficLight()
a.running() # можно зациклить и на дорогу.
