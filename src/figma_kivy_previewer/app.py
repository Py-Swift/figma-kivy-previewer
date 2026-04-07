
from thorvg_cython.thorvg import Engine

_tvg_engine = Engine()
_tvg_engine.init()

from kivy.app import App
from kivy.lang import Builder
from os import environ
from .previewer import Previewer

from .generated import preview

class MainApp(App):

    def __init__(self, ip: str, port: int, **kwargs):
        super().__init__(**kwargs)
        self.ip = ip
        self.port = port
        self.previewer = Previewer(ip, port)
        self.previewer.listener.start()

    def build(self):
        return preview


def main():



    
    ip = environ.get('PREVIEWER_IP', 'localhost')
    port = int(environ.get('PREVIEWER_PORT', 7654))
    app = MainApp(ip, port)
    app.run()