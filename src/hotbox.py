import pygame


class Hotbox:
    def __init__(self, x, y, width, height, label):
        self.rect = pygame.Rect(x, y, width, height)
        self.label = label
        self.is_hovered = False

    def update(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def was_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

    def draw(self, surface, font):
        if not self.is_hovered:
            return

        overlay = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        overlay.fill((210, 210, 210, 80))
        surface.blit(overlay, self.rect.topleft)

        pygame.draw.rect(surface, (130, 115, 95), self.rect, 2)

        text_surface = font.render(self.label, True, (255, 255, 255))

        text_bg = pygame.Surface(
            (text_surface.get_width() + 12, text_surface.get_height() + 8),
            pygame.SRCALPHA
        )
        text_bg.fill((0, 0, 0, 180))

        label_x = self.rect.x
        label_y = self.rect.y - text_bg.get_height() - 6

        if label_y < 0:
            label_y = self.rect.y + self.rect.height + 6

        surface.blit(text_bg, (label_x, label_y))
        surface.blit(text_surface, (label_x + 6, label_y + 4))