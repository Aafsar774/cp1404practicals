from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

class ConvertMilesKilometre(App):
    output = StringProperty()
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root
    def handle_update(self):
        """Handle changes to the text input by updating the model from the view."""
        self.output = self.root.ids.input_miles.text
ConvertMilesKilometre().run()
