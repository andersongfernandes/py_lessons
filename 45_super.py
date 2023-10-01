# timecode 4:08:30
# super function

class Rectangle:
    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width

class Square(Rectangle):
    def __init__(self, length, width) -> None:
        super().__init__(length, width)

    def area(self):
        return self.length * self.width

class Cube(Rectangle):
    def __init__(self, length, width, height) -> None:
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length * self.width * self.height

square = Square(3,3)
print(square.area())

cube = Cube(2,3,4)
print(cube.volume())