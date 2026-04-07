from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle

import urllib.request as _urllib_request
import os as _os
import tempfile as _tempfile

_os.makedirs(_os.path.join(_tempfile.gettempdir(), "svgs"), exist_ok=True)

SVG_232_206 = _os.path.join(_tempfile.gettempdir(), "svgs", "svg_232_206.svg")
if not _os.path.exists(SVG_232_206):
    _urllib_request.urlretrieve(("http://localhost:8765/svg/232%3A206"), SVG_232_206)

from kivy.graphics.texture import Texture as _Texture
from thorvg_cython.sw_canvas import SwCanvas as _SwCanvas
from thorvg_cython.thorvg import Picture as _Picture

from .svg_instructions import Svg


class Canva(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        cb = self.canvas
        self.color_0 = Color(rgba=(1.0, 1.0, 1.0, 1.0))
        cb.add(self.color_0)
        self.svg_1 = Svg(0, 0, 393, 868, SVG_232_206)
        cb.add(self.svg_1)

preview = Canva()