import re


class ImageData:

    @staticmethod
    def html_to_RGB(num):
        return tuple([int(num[i:i + 2], 16) for i in range(1, len(num), 2)])

    @staticmethod
    def validate_color(color, pallet):
        if color in pallet.keys():
            color = pallet[color]
        if color[0] == '#':
            color = ImageData.html_to_RGB(color)
        if type(color) == str:
            color = tuple([int(string) for string in re.findall(r'\d{1,3}', color)])
        return color

    def validate_figure_color(self, figure, pallet):
        if 'color' not in figure:
            figure['color'] = self.fg_color
        else:
            figure['color'] = self.validate_color(figure['color'], pallet)

    def __init__(self, pars_data):
        self.bg_color = self.validate_color(pars_data.bg_color, pars_data.pallet)
        self.fg_color = self.validate_color(pars_data.fg_color, pars_data.pallet)
        self.width = pars_data.width
        self.height = pars_data.height
        for figure in pars_data.figures:
            self.validate_figure_color(figure, pars_data.pallet)
        self.figures = pars_data.figures
