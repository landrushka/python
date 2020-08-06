class Stationery(object):
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    def draw(self):
        print("Запуск отрисовки. {}".format(self.title))


class Pencil(Stationery):
    def draw(self):
        print("Запуск отрисовки. {}".format(self.title))


class Handle(Stationery):
    def draw(self):
        print("Запуск отрисовки. {}".format(self.title))


pen = Pen(title="Pen")
pen.draw()
pencil = Pencil(title="Pencil")
pencil.draw()
handle = Handle(title="Handle")
handle.draw()
