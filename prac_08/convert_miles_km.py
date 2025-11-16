from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

class ConvertMilesKilometre(App):
    output = StringProperty("0.0")
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_update(self):
        self.output = self.root.ids.input_miles.text

    def handle_convert(self):
        miles = self.get_miles()
        kilometres = miles * 1.60934
        self.output = str(kilometres)

    def get_miles(self):
        try:
            return float(self.root.ids.input_miles.text)
        except ValueError:
            return 0.0

ConvertMilesKilometre().run()
