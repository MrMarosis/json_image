import pygame
from shapes import Point, Circle, Polygon, Square, Rectangle


class Window:

    def __init__(self, width, height, bg_color, models):
        self.width = width
        self.height = height
        self.bg_color = bg_color
        self.models = models
        pygame.display.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("JSON SHAPES")
        self.screen.fill(self.bg_color)

    def _draw_point(self, point):
        pygame.draw.circle(self.screen, point.color,
                           (point.x, point.y), 1)

    def _draw_circle(self, circle):
        pygame.draw.circle(self.screen, circle.color,
                           (circle.x, circle.y), circle.radius)

    def _draw_polygon(self, polygon):
        pygame.draw.polygon(self.screen, polygon.color, polygon.points)

    def _draw_square(self, square):
        pygame.draw.rect(self.screen, square.color,
                         (square.x, square.y, square.size, square.size))

    def _draw_rectangle(self, rectangle):
        pygame.draw.rect(self.screen, rectangle.color,
                         (rectangle.x, rectangle.y, rectangle.width, rectangle.height))

    def _draw_shape(self, figure):
        if isinstance(figure, Point):
            self._draw_point(figure)
        elif isinstance(figure, Circle):
            self._draw_circle(figure)
        elif isinstance(figure, Polygon):
            self._draw_polygon(figure)
        elif isinstance(figure, Square):
            self._draw_square(figure)
        elif isinstance(figure, Rectangle):
            self._draw_rectangle(figure)

    def draw(self):
        for model in self.models:
            self._draw_shape(model)

    def ss_window(self,image_save_path):
        pygame.image.save(self.screen, image_save_path)

    def show_image(self):
        pygame.display.flip()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    pygame.quit()
            try:
                key = pygame.key.get_pressed()
                if key[pygame.K_s]:
                    self.ss_window("screenshot.jpeg")
                if key[pygame.K_q]:
                    pygame.quit()
                    done = True
            except pygame.error:
                pass
                '''Video system is not initialised'''

            pygame.time.wait(50)


