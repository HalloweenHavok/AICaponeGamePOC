import pygame

from scene_event import SceneEvent
from hotbox import Hotbox
from textbox import TextBox


class Scene:
    def __init__(self, background_path, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height

        self.background = self._load_background(background_path)

        self.scene_events = []
        self.active_event = None

    def _load_background(self, path):
        try:
            image = pygame.image.load(path).convert()
            image = pygame.transform.scale(image, (self.window_width, self.window_height))
            return image
        except pygame.error as e:
            print(f"Could not load background image: {path}")
            print(e)
            return None

    def add_scene_event(self, scene_event):
        self.scene_events.append(scene_event)

    def update(self, mouse_pos):
        for scene_event in self.scene_events:
            scene_event.update(mouse_pos)

    def handle_left_click(self, mouse_pos):
        # Wenn gerade ein Event aktiv ist:
        # Jeder Klick schaltet zur nächsten Textbox weiter.
        if self.active_event is not None:
            self.active_event.next_textbox()

            if not self.active_event.is_active:
                self.active_event = None

            return

        # Wenn kein Event aktiv ist:
        # Prüfe, ob eine Hotbox angeklickt wurde.
        for scene_event in self.scene_events:
            if scene_event.was_clicked(mouse_pos):
                self._set_active_event(scene_event)
                return

        self._clear_active_event()

    def _set_active_event(self, scene_event):
        if self.active_event is not None:
            self.active_event.deactivate()

        self.active_event = scene_event
        self.active_event.activate()

    def _clear_active_event(self):
        if self.active_event is not None:
            self.active_event.deactivate()

        self.active_event = None

    def draw(self, surface, font):
        if self.background:
            surface.blit(self.background, (0, 0))
        else:
            surface.fill((30, 30, 30))

        for scene_event in self.scene_events:
            scene_event.draw(surface, font)