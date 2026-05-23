import pygame


class TextBox:
    def __init__(self, x, y, width, height, text=""):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.visible = False

    def show(self):
        self.visible = True

    def hide(self):
        self.visible = False

    def set_text(self, text):
        self.text = text

    def draw(self, surface, font):
        if not self.visible or not self.text:
            return

        box = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        box.fill((0, 0, 0, 190))
        surface.blit(box, self.rect.topleft)

        pygame.draw.rect(surface, (180, 180, 180), self.rect, 2)

        self._draw_wrapped_text(
            surface=surface,
            font=font,
            text=self.text,
            x=self.rect.x + 20,
            y=self.rect.y + 18,
            max_width=self.rect.width - 40
        )

    def _draw_wrapped_text(self, surface, font, text, x, y, max_width):
        words = text.split(" ")
        line = ""

        for word in words:
            test_line = line + word + " "
            test_surface = font.render(test_line, True, (255, 255, 255))

            if test_surface.get_width() <= max_width:
                line = test_line
            else:
                surface.blit(font.render(line, True, (255, 255, 255)), (x, y))
                y += font.get_height() + 4
                line = word + " "

        if line:
            surface.blit(font.render(line, True, (255, 255, 255)), (x, y))