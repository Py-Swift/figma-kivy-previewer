
from kivy.uix.widget import Widget
from kivy.properties import ListProperty, ObjectProperty
from .network_listener import NetworkListener





class Previewer(Widget):


    preview_widget = ObjectProperty(None)

    listener: NetworkListener

    def __init__(self, ip: str, port: int, **kwargs):
        super().__init__(**kwargs)
        self.listener = NetworkListener(ip, port)
        self.listener.bind(on_new_widget=self.update_widget)
        self.bind(pos=self.on_pos, size=self.on_size)


    def on_pos(self, _, new_pos):
        print(f"Position changed: {new_pos}")
        self.update_widget_properties(pos=new_pos)

    def on_size(self, _, new_size):
        print(f"Size changed: {new_size}")
        self.update_widget_properties(size=new_size)

    def update_widget(self,_, new_widget):
        if self.preview_widget:
            self.remove_widget(self.preview_widget)
        self.update_widget_properties(pos=self.pos, size=self.size)
        self.preview_widget = new_widget
        self.add_widget(self.preview_widget)

    def update_widget_properties(self, **properties):
        if self.preview_widget:
            for prop, value in properties.items():
                setattr(self.preview_widget, prop, value)