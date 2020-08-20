<<<<<<< HEAD:kivy_ios/recipes/pyobjus/__init__.py
from kivy_ios.toolchain import CythonRecipe
=======
from toolchain import CythonRecipe
<<<<<<< HEAD:kivy_ios/recipes/pyobjus/__init__.py
>>>>>>> parent of 64bd692... Flake8 CI fixes (#451):recipes/pyobjus/__init__.py
=======
>>>>>>> parent of 64bd692... Flake8 CI fixes (#451):recipes/pyobjus/__init__.py

class PyobjusRecipe(CythonRecipe):
    version = "master"
    url = "https://github.com/kivy/pyobjus/archive/{version}.zip"
    library = "libpyobjus.a"
    depends = ["python"]
    pre_build_ext = True


recipe = PyobjusRecipe()
