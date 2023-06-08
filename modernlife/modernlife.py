# modernlife.py
#
# Conway's Game of Life implemented in OpenGL with the moderngl and
# moderngl_window python modules

from pathlib import Path
import moderngl as mgl
import moderngl_window as mglw
from modglapp.baseapp import BaseApp


class ModernLife(BaseApp):
    gl_version = (4, 3)
    window_size = (512, 512)
    title = "(floatwong)"
    resizable = False
    resource_dir = (Path(__file__) / '../resources').resolve()
    samples = 8

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.front_buffer = self.ctx.texture(ModernLife.window_size, 4, None)
        self.back_buffer = self.ctx.texture(ModernLife.window_size, 4, None)

    def swap_buffers(self):
        temp = self.front_buffer
        self.front_buffer = self.back_buffer
        self.back_buffer = temp

    def render(self, time: float, frametime: float):
        # rendering happens here, of all places
        self.ctx.clear()

    def resize(self, width: int, height: int):
        print("Window was resized, buffer size is {}x{}".format(width, height))

    def mouse_position_event(self, x, y, dx, dy):
        print("Mouse position: ({}, {})".format(x, y))

    def mouse_press_event(self, x, y, button):
        print("Mouse button {} pressed at ({}, {})".format(button, x, y))


if __name__ == '__main__':
    ModernLife.run()
    print(str(ModernLife.resource_dir))
