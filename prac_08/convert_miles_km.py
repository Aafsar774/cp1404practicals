from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
MILES_IN_KM = 1.60934
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
        kilometres = miles * MILES_IN_KM
        self.output = str(kilometres)

    def handle_positive_increment(self):
        miles = self.get_miles()
        miles += 1
        self.root.ids.input_miles.text = str(miles)
        self.handle_convert()

    def handle_negative_increment(self):
        miles = self.get_miles()
        miles -= 1
        self.root.ids.input_miles.text = str(miles)
        self.handle_convert()

    def get_miles(self):
        try:
            return float(self.root.ids.input_miles.text)
        except ValueError:
            return 0

ConvertMilesKilometre().run()
