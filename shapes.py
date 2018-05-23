class Circle:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color


class Square:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color


class Polygon:
    def __init__(self, points, color):
        self.points = points
        self.color = color


class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color


class Rectangle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color


class FigureFactory:

    def factory(s_data):
        type = s_data['type']

        if type == "circle":
            return Circle(s_data['x'], s_data['y'],
                           s_data['radius'], s_data['color'])
        elif type == "square":
            return Square(s_data['x'], s_data['y'],
                           s_data['size'], s_data['color'])
        elif type == "polygon":
            return Polygon(s_data['points'], s_data['color'])

        elif type == "point":
            return Point(s_data['x'], s_data['y'], s_data['color'])

        elif type == "rectangle":
            return Rectangle(s_data['x'], s_data['y'], s_data['width'],
                             s_data['height'], s_data['color'])
