import arcade

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900

class SumMeGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        self.startScreen = arcade.Sprite('images/startScreen.png')
        self.startScreen.set_position(600,450)

    def on_draw(self):
        arcade.start_render()

        self.startScreen.draw()

if __name__ == '__main__':
    window = SumMeGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
