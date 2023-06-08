import moderngl as mgl
import moderngl_window as mglw
from pathlib import Path


class ComputeRenderTexture(mglw.WindowConfig):
    title = "floatme"
    resource_dir = (Path(__file__) / '../resources').resolve()
    gl_version = 4, 3
    window_size = 256, 256
    aspect_ratio = 1.0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.compute_shader = self.load_compute_shader('compute_texture.glsl')
        self.compute_shader['destTex'] = 0
        self.texture_program = self.load_program('texture.glsl')
        self.quad_fs = mglw.geometry.quad_fs()
        self.texture = self.ctx.texture((256, 256), 4)
        self.texture.filter = mgl.NEAREST, mgl.NEAREST

    def render(self, time, frame_time):
        self.ctx.clear(0.3, 0.3, 0.3)

        w, h = self.texture.size
        gw, gh = 16, 16
        nx, ny, nz = int(w / gw), int(h / gh), 1

        try:
            self.compute_shader['time'] = time
        except Exception:
            pass
        # by default the texture bidns as a GL_R32F / r32f (read from the
        # texture)
        self.texture.bind_to_image(0, read=False, write=True)
        self.compute_shader.run(nx, ny, nz)

        # render texture
        self.texture.use(location=0)
        self.quad_fs.render(self.texture_program)


if __name__ == '__main__':
    mglw.run_window_config(ComputeRenderTexture)
