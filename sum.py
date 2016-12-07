import arcade
from world import World

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900

class SumMeGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        self.startScreen = arcade.Sprite('images/startScreen.png')
        self.startScreen.set_position(600,450)

        self.world = World(width, height)

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.PINK)
        if self.world.state == 'start' :
            self.startScreen.draw()
        if self.world.state == 'game' :
            arcade.draw_text(self.world.ans, self.world.ans_pos_x, self.height/2,
                            arcade.color.BLACK, 30)
    # def animate(self, delta):
    #     self.world.animate(delta)

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

    def on_key_release(self, key, key_modifiers):
        self.world.on_key_release(key, key_modifiers)

if __name__ == '__main__':
    window = SumMeGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
