class Rectangle:
    def __init__(self, c, l, w):
        self.color = c
        self.length = l
        self.width = w

    def area(self):
        self.area = self.length*self.width
        return self.area

    def per(self):
        self.perimeter = 2*self.length*+2*self.width
        return self.perimeter

    def diagonal(self):
        self.diag = (self.width**2+self.length**2)**(1/2)
        return self.diag

    def volume(self, h):
        self.height = h
        self.vol = self.height*self.width*self.length
        return self.vol

    def testing(self):
        return self.diag


myRect1 = Rectangle('red', 2, 1)
myRect2 = Rectangle('blue', 4, 2)
print(myRect1.color)
print('myRect1 length=', myRect1.length)
print('myRect1 area=', myRect1.area())
print('myRect1 perimeter=', myRect1.per())
print('myRect1 diagonal=', myRect1.diagonal())
print('myRect1 transformed to volume is:', myRect1.volume(5))

print(myRect2.color)
print('myRect2 length=', myRect2.length)
print('myRect2 area=', myRect2.area())
print('myRect2 perimeter=', myRect2.per())
print('myRect2 diagonal=', myRect2.diagonal())
print('myRect2 transformed to volume is:', myRect2.volume(5))

print('myRect2 diagonal=', myRect2.testing())
