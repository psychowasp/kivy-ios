<<<<<<< HEAD:kivy_ios/recipes/curly/__init__.py
from kivy_ios.toolchain import CythonRecipe
=======
from toolchain import CythonRecipe
<<<<<<< HEAD:kivy_ios/recipes/curly/__init__.py
>>>>>>> parent of 64bd692... Flake8 CI fixes (#451):recipes/curly/__init__.py
=======
>>>>>>> parent of 64bd692... Flake8 CI fixes (#451):recipes/curly/__init__.py

class CurlyRecipe(CythonRecipe):
    version = "master"
    url = "https://github.com/tito/curly/archive/{version}.zip"
    library = "libcurly.a"
    depends = ["python", "libcurl", "sdl2", "sdl2_image"]
    pre_build_ext = True


recipe = CurlyRecipe()
