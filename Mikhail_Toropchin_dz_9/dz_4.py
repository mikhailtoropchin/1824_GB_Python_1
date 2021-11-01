class Car:

    def __init__(self, name, color, speed, is_police):
        # аттрибуты
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        self.speed += 10
        print("машина поехала")

    def stop(self):
        self.speed = 0
        print("машина остановилась")


    def turn(self, direction):
        print(f"машина поеврнула {direction}")

    def show_speed(self):
        print(self.speed)

    def info(self):
        if self.is_police:
            print("Это полицейская машина")
        print(f"{self.name}, {self.color}, скорость движения {self.speed}")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Превышение скорости!")
        else:
            print(self.speed)

    def show_info(self):
        super().info()
        print("Это городская машина")


class WorkCar(Car):
    def show_speed(self):
        if Car.speed > 40:
            print("Превышение скорости!")
        else:
            print(self.speed)

    def show_info(self):
        super().info()
        print("Это рабочая машина")

class SportCar(Car):
    def show_info(self):
        super().info()
        print("Это спортивная машина")

class PoliceCar(Car):
    def show_info(self):
        super().info()
        print("Это полицейская машина")
    pass


car = Car("kia rio", "black", 80, False)
car.info()

t_car = TownCar("toyota camry", "white", 65, False)
t_car.show_info()
t_car.show_speed()

s_car = SportCar("чепырка", "желтая", 150, False)
s_car.show_info()

p_car = PoliceCar("octavia", "white", 90, True)
p_car.show_info()
p_car.go()
p_car.stop()
print(p_car.speed)
p_car.go()
print(p_car.speed)
