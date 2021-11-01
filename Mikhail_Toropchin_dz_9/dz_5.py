class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("Рисуем ручкой")


class Pencil(Stationery):
    def draw(self):
        print("Рисуем карандашом")


class Handle(Stationery):
    def draw(self):
        print("Рисуем маркером")


m = Handle("маркер")
m.draw()

pen = Pen("ручка")
pen.draw()

pencil = Pencil("карандаш")
pencil.draw()

thing = Stationery("линейка")
thing.draw()
