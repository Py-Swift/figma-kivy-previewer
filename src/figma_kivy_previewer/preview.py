from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle, SmoothRoundedRectangle, SmoothEllipse, SmoothTriangle, InstructionGroup


class Circles(InstructionGroup):
    def __init__(self):
        super().__init__()
        self.color_0 = Color(rgba=(0.0, 1.0, 0.18333333730697632, 1.0))
        self.add(self.color_0)
        self.ellipse_1 = SmoothEllipse(pos=(95, 87), size=(141, 96))
        self.add(self.ellipse_1)
        self.ellipse_2 = SmoothEllipse(pos=(332, 85), size=(170, 102))
        self.add(self.ellipse_2)
        self.ellipse_3 = SmoothEllipse(pos=(562, 50), size=(141, 169))
        self.add(self.ellipse_3)


class FreeRects(InstructionGroup):
    def __init__(self):
        super().__init__()
        self.color_0 = Color(rgba=(0.0, 0.3166666626930237, 1.0, 1.0))
        self.add(self.color_0)
        self.rect_1 = SmoothRoundedRectangle(pos=(0, 398), size=(296, 42), radius=[8.0])
        self.add(self.rect_1)
        self.rect_2 = Rectangle(pos=(25, 353), size=(285, 31))
        self.add(self.rect_2)
        self.rect_3 = Rectangle(pos=(25, 297), size=(322, 29))
        self.add(self.rect_3)


class BoxedRects(InstructionGroup):
    def __init__(self):
        super().__init__()
        self.color_0 = Color(rgba=(1.0, 0.2836538553237915, 0.2836538553237915, 1.0))
        self.add(self.color_0)
        self.rect_1 = Rectangle(pos=(0, 565), size=(129, 56))
        self.add(self.rect_1)
        self.color_2 = Color(rgba=(1.0, 0.3461538553237915, 0.3461538553237915, 1.0))
        self.add(self.color_2)
        self.rect_3 = Rectangle(pos=(0, 508), size=(240, 56))
        self.add(self.rect_3)
        self.color_4 = Color(rgba=(1.0, 0.0, 0.0, 1.0))
        self.add(self.color_4)
        self.rect_5 = Rectangle(pos=(0, 440), size=(357, 68))
        self.add(self.rect_5)
        self.freeRects_6 = FreeRects()
        self.add(self.freeRects_6)


class Rects(InstructionGroup):
    def __init__(self):
        super().__init__()
        self.boxedRects_0 = BoxedRects()
        self.add(self.boxedRects_0)


class CanvasTest(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        cb = self.canvas.before
        self.color_0 = Color(rgba=(0.0, 1.0, 0.18333333730697632, 1.0))
        cb.add(self.color_0)
        self.ellipse_1 = SmoothEllipse(pos=(361, 237), size=(141, 126))
        cb.add(self.ellipse_1)
        self.circles_2 = Circles()
        cb.add(self.circles_2)
        self.rects_3 = Rects()
        cb.add(self.rects_3)
        self.color_4 = Color(rgba=(0.0, 1.0, 0.6499999761581421, 0.0))
        cb.add(self.color_4)
        self.rect_5 = Rectangle(pos=(0, 43), size=(784, 578))
        cb.add(self.rect_5)
        self.color_6 = Color(rgba=(0.3812499940395355, 0.3125, 1.0, 1.0))
        cb.add(self.color_6)
        self.tri_7 = SmoothTriangle(points=[459, 368, 703, 368, 581, 525])
        cb.add(self.tri_7)

preview = CanvasTest()