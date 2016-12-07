import arcade.key

class World:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.state = 'start'
        self.nums = []

    def on_key_release(self, key, key_modifiers):
        if key == arcade.key.SPACE and self.state == 'start':
            self.state = 'game'
