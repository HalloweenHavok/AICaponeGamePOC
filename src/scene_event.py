class SceneEvent:
    def __init__(self, hotbox):
        self.hotbox = hotbox
        self.textboxes = []

        self.is_active = False
        self.current_textbox_index = 0

    def add_textbox(self, textbox):
        self.textboxes.append(textbox)

    def update(self, mouse_pos):
        self.hotbox.update(mouse_pos)

    def was_clicked(self, mouse_pos):
        return self.hotbox.was_clicked(mouse_pos)

    def activate(self):
        self.is_active = True
        self.current_textbox_index = 0
        self._show_current_textbox()

    def next_textbox(self):
        if not self.is_active:
            return

        self._hide_all_textboxes()

        self.current_textbox_index += 1

        if self.current_textbox_index >= len(self.textboxes):
            self.deactivate()
            return

        self._show_current_textbox()

    def deactivate(self):
        self.is_active = False
        self.current_textbox_index = 0
        self._hide_all_textboxes()

    def _show_current_textbox(self):
        self._hide_all_textboxes()

        if not self.textboxes:
            return

        self.textboxes[self.current_textbox_index].show()

    def _hide_all_textboxes(self):
        for textbox in self.textboxes:
            textbox.hide()

    def draw(self, surface, font):
        self.hotbox.draw(surface, font)

        for textbox in self.textboxes:
            textbox.draw(surface, font)