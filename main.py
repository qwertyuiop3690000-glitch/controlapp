from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import requests


class ControlApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        self.label = Label(text='مرحبا بكم')
        layout.add_widget(self.label)

        self.button = Button(text='زر التحكم')
        self.button.bind(on_press=self.enable_control)
        layout.add_widget(self.button)

        return layout

    def enable_control(self, instance):
        self.label.text = 'تم تفعيل التحكم'
        requests.get('http://your-bot-url/enable_control')


if __name__ == '__main__':
    ControlApp().run()
