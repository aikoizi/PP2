class Points():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print('coordinates of the point ' + 'x = ' + str(self.x) + ' and '+ ' y = ' + str(self.y))
    def move(self):
        self.t = self.y
        self.y = self.x
        self.x = self.t
    def dist(self):
        print(abs(self.y - self.x))
mako = Points(4, 7)
mako.show()
mako.dist()
mako.move()
mako.show()
mako.dist()