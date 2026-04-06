from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        for name in self.names:
            label = Label(text=name, font_size=24, color=(1, 1, 1, 1))
            self.root.ids.main.add_widget(label)
        return self.root

if __name__ == '__main__':
    DynamicLabelsApp().run()