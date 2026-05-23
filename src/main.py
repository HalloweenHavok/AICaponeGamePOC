import pygame
import sys


# ------------------------------------------------------------
# Settings
# ------------------------------------------------------------

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
FPS = 60

BACKGROUND_PATH = "assets/scenes/warehouse.png"

class Hotspot:
    def __init__(self, x, y, width, height, label):
        self.rect = pygame.Rect(x, y, width, height)
        self.label = label
        self.is_hovered = False

    def update(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def draw(self, surface, font):
        if self.is_hovered:
            # halbtransparente Fläche
            overlay = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
            overlay.fill((255, 255, 0, 80))
            surface.blit(overlay, self.rect.topleft)

            # Rahmen
            pygame.draw.rect(surface, (255, 220, 0), self.rect, 2)

            # Label
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


# ------------------------------------------------------------
# Game
# ------------------------------------------------------------

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("AICapone POC")

        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("arial", 22)

        self.background = self.load_background(BACKGROUND_PATH)

        self.hotspots = [
            Hotspot(
                x=500,
                y=280,
                width=220,
                height=140,
                label="Alter Terminal"
            )
        ]

        self.running = True

    def load_background(self, path):
        try:
            image = pygame.image.load(path).convert()
            image = pygame.transform.scale(image, (WINDOW_WIDTH, WINDOW_HEIGHT))
            return image
        except pygame.error as e:
            print(f"Could not load background image: {path}")
            print(e)
            return None

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()

            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def update(self):
        mouse_pos = pygame.mouse.get_pos()

        for hotspot in self.hotspots:
            hotspot.update(mouse_pos)

    def draw(self):
        if self.background:
            self.screen.blit(self.background, (0, 0))
        else:
            self.screen.fill((30, 30, 30))

        for hotspot in self.hotspots:
            hotspot.draw(self.screen, self.font)

if __name__ == "__main__":
    game = Game()
    game.run()