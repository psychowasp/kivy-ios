<<<<<<< HEAD:kivy_ios/recipes/plyer/__init__.py
from kivy_ios.toolchain import PythonRecipe
=======
from toolchain import PythonRecipe
>>>>>>> parent of 64bd692... Flake8 CI fixes (#451):recipes/plyer/__init__.py

class PlyerRecipe(PythonRecipe):
    version = "master"
    url = "https://github.com/kivy/plyer/archive/{version}.zip"
    depends = ["python", "pyobjus"]
    archs = ["x86_64"]


recipe = PlyerRecipe()
