from kivy.app import App
from kivy.lang import Builder

class SquaringApp(App):
    def build(self):
        self.title = "Square Number 2"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self, number_text):
        try:
            number = float(number_text)
            result = number ** 2
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = "0.0"

if __name__ == '__main__':
    SquaringApp().run()