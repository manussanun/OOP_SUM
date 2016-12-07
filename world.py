import arcade.key

class World:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.state = 'start'
        self.ans = ''
        self.sum_ans = 0
        self.ans_pos_x = self.width/2

    def on_key_press(self, key, key_modifiers):
        if self.state == 'game':
            if 48 <= key <= 57:
                self.ans_pos_x -= 11
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

            if key == arcade.key.SPACE:
                self.sum_ans = int(self.ans)
                self.ans = ''
                self.ans_pos_x = self.width/2

    def on_key_release(self, key, key_modifiers):
        if key == arcade.key.SPACE and self.state == 'start':
            self.state = 'game'


    # def animate(self, delta):
