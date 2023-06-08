from pathlib import Path

import moderngl as mgl
import moderngl_window as mglw


class BaseApp(mglw.WindowConfig):
    gl_version = (4, 3)
    window_size = (512, 512)
    title = "(floatwong)"
    resizable = False
    resource_dir = (Path(__file__) / '../resources').resolve()
    samples = 8

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @classmethod
    def run(cls):
        mglw.run_window_config(cls)
