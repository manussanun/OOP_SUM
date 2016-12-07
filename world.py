import arcade.key

class World:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.state = 'start'
        self.ans = ''

    def on_key_press(self, key, key_modifiers):
        if self.state == 'game':
            if key == 48:
                self.ans += '0'
            elif key == 49:
                self.ans += '1'
            elif key == 50:
                self.ans += '2'
            elif key == 51:
                self.ans += '3'
            elif key == 52:
                self.ans += '4'
            elif key == 53:
                self.ans += '5'
            elif key == 54:
                self.ans += '6'
            elif key == 55:
                self.ans += '7'
            elif key == 56:
                self.ans += '8'
            elif key == 57:
                self.ans += '9'

    def on_key_release(self, key, key_modifiers):
        if key == arcade.key.SPACE and self.state == 'start':
            self.state = 'game'


    # def animate(self, delta):
