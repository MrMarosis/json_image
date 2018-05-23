from json_parser import JsonParser
from visual_models import ImageData
from shapes import FigureFactory
from window import *
import sys


def main():

    if len(sys.argv)<2:
        raise Exception("Not enough arguments")

    json_parser = JsonParser()
    parsed_data = json_parser.parse_json(sys.argv[1])

    models = ImageData(parsed_data)
    shapes = [FigureFactory.factory(figure) for figure in models.figures]
    window = Window(models.width,models.height,models.bg_color,shapes)
    window.draw()

    if len(sys.argv) > 3:
        if sys.argv[2] in ['-o','--output']:
            window.ss_window(sys.argv[3])

    window.show_image()


if __name__ == '__main__':
    main()