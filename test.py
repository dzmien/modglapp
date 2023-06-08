#!/home/damian/.virtualenvs/modglapp/bin/python

import moderngl
import numpy as np
from PIL import Image


class Shaders:
    def __init__(self, vertfile=None, fragfile=None):
        with open(vertfile, 'r') as vs:
            self.vertex = ''.join(vs.readlines())
        with open(fragfile, 'r') as fs:
            self.fragment = ''.join(fs.readlines())


shaders = Shaders("vert.glsl", "frag.glsl")
ctx = moderngl.create_standalone_context()


prog = ctx.program(
    vertex_shader=shaders.vertex,
    fragment_shader=shaders.fragment,
)


x = np.linspace(-1.0, 1.0, 50)
y = np.random.rand(50) - 0.5
r = np.ones(50)
g = np.zeros(50)
b = np.zeros(50)


vertices = np.dstack([x, y, r, g, b])


vbo = ctx.buffer(vertices.astype('f4').tobytes())
vao = ctx.simple_vertex_array(prog, vbo, 'in_vert', 'in_color')


fbo = ctx.simple_framebuffer((512, 512))
fbo.use()
fbo.clear(0.0, 0.0, 0.0, 1.0)
vao.render(moderngl.LINE_STRIP)


Image.frombytes('RGB', fbo.size, fbo.read(), 'raw', 'RGB', 0, -1).show()
