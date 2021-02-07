class Rectangle:
    def __init__(self,x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_config_rectangle(self):
        return str(f'Rectangle ({self.x} , {self.y}, {self.width}, {self.height})')

    def get_rectangle_area(self):
        return self.width * self.height