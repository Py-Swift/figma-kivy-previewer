from kivy.graphics import Rectangle, Color, InstructionGroup
from kivy.core.text import Label as CoreLabel
from kivy.graphics.texture import Texture
from thorvg_cython.sw_canvas import SwCanvas
from thorvg_cython.thorvg import Engine, Shape, Picture


class Svg(Rectangle):

    swc: SwCanvas

    def __init__(self,x, y, width: int, height: int, path: str):
        size = (width, height)
        
        tex = Texture.create(size=(width, height), colorfmt='rgba')
        tex.flip_vertical()

        swc = SwCanvas(width, height)

        pic = Picture()
        pic.load(path)
        pic.set_size(width, height)
        swc.add(pic)

        swc.draw()
        swc.sync()
        tex.blit_buffer(swc, colorfmt='rgba', bufferfmt='ubyte')
        super().__init__(texture=tex, size=size, pos=(x, y))

        self.swc = swc
        self.pic = pic



    def resize(self, width: int, height: int):
        print(f"Resizing Svg to: {width}x{height}")
        swc = self.swc
        pic = self.pic
        pic.set_size(width, height)
        tex = Texture.create(size=(width, height), colorfmt='rgba')
        tex.flip_vertical()
        swc.resize(width, height)
        swc.update()
        swc.draw()
        swc.sync()
        tex.blit_buffer(swc, colorfmt='rgba', bufferfmt='ubyte')
        self.texture = tex
        self.size = (width, height)
