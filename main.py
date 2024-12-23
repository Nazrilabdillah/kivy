from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.properties import NumericProperty


class MyGame(Widget):
    # Properti untuk posisi bola
    ball_x = NumericProperty(100)
    ball_y = NumericProperty(100)
    ball_speed_x = NumericProperty(5)
    ball_speed_y = NumericProperty(5)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball = Image(source='assets/bird.gif', size=(50, 50))
        self.ball.size_hint = (None, None)
        self.add_widget(self.ball)

        # Tambahkan tombol untuk keluar
        self.exit_button = Button(
            text="Exit",
            size_hint=(None, None),
            size=(100, 50),
            pos=(10, 10)
        )
        self.exit_button.bind(on_press=self.exit_game)
        self.add_widget(self.exit_button)

        # Jadwalkan update game
        Clock.schedule_interval(self.update, 1 / 60)

    def update(self, dt):
        # Gerakkan bola
        self.ball_x += self.ball_speed_x
        self.ball_y += self.ball_speed_y

        # Pantulkan bola saat menyentuh batas layar
        if self.ball_x <= 0 or self.ball_x + 50 >= self.width:
            self.ball_speed_x *= -1
        if self.ball_y <= 0 or self.ball_y + 50 >= self.height:
            self.ball_speed_y *= -1

        # Perbarui posisi bola
        self.ball.pos = (self.ball_x, self.ball_y)

    def exit_game(self, instance):
        App.get_running_app().stop()


class MyGameApp(App):
    def build(self):
        return MyGame()


if __name__ == '__main__':
    MyGameApp().run()
