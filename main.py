from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        self.label = Label(text='Hello, World!')
        layout.add_widget(self.label)

        btn = Button(text='Click Me!')
        btn.bind(on_press=self.change_text)
        layout.add_widget(btn)

        return layout

    def change_text(self, instance):
        self.label.text = 'Button Clicked!'

if __name__ == '__main__':
    MyApp().run()
