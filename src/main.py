import pygame
import sys

from scene import Scene
from scene_event import SceneEvent
from hotbox import Hotbox
from textbox import TextBox


WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
FPS = 60

BACKGROUND_PATH = "assets/scenes/warehouse.png"


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("AI Capone POC")

        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("arial", 22)

        self.scene = self._create_start_scene()

        self.running = True

    def _create_start_scene(self):
        scene = Scene(
            background_path=BACKGROUND_PATH,
            window_width=WINDOW_WIDTH,
            window_height=WINDOW_HEIGHT
        )

        terminal_event = SceneEvent(
            hotbox=Hotbox(
                x=170,
                y=380,
                width=950,
                height=280,
                label="conference table"
            )
        )

        terminal_event.add_textbox(
            TextBox(
                x=40,
                y=540,
                width=1200,
                height=140,
                text=(
                    "a old heavy wooden conference table stands in the middle of the room. Some bottles of booze are still on the table, but they are all empty. Together with some glasses and cigarettes, they are covered in a thick layer of dust."
                )
            )
        )

        terminal_event.add_textbox(
            TextBox(
                x=40,
                y=540,
                width=1200,
                height=140,
                text=(
                    "A man approaches you."
                )
            )
        )

        scene.add_scene_event(terminal_event)

        return scene

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

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.scene.handle_left_click(event.pos)

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        self.scene.update(mouse_pos)

    def draw(self):
        self.scene.draw(self.screen, self.font)


if __name__ == "__main__":
    game = Game()
    game.run()