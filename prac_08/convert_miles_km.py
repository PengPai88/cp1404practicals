from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934

class ConvertMilesKmApp(App):
    km_output = StringProperty("0.0")

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self, miles_text):
        try:
            miles = float(miles_text)
            self.km_output = f"{miles * MILES_TO_KM:.6f}"
        except ValueError:
            self.km_output = "0.0"

    def handle_increment(self, miles_text, delta):
        try:
            miles = float(miles_text)
        except ValueError:
            miles = 0.0
        new_miles = miles + delta
        self.root.ids.input_miles.text = str(new_miles)
        self.handle_convert(str(new_miles))

if __name__ == '__main__':
    ConvertMilesKmApp().run()