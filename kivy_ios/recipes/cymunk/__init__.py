"""
Author: Lawrence Du, Lukasz Mach
E-mail: larrydu88@gmail.com, maho@pagema.net
"""

<<<<<<< HEAD:kivy_ios/recipes/cymunk/__init__.py
<<<<<<< HEAD:kivy_ios/recipes/cymunk/__init__.py
from kivy_ios.toolchain import CythonRecipe
=======
=======
>>>>>>> parent of 64bd692... Flake8 CI fixes (#451):recipes/cymunk/__init__.py
from toolchain import CythonRecipe,shprint
import os
from os.path import join
import sh
<<<<<<< HEAD:kivy_ios/recipes/cymunk/__init__.py
>>>>>>> parent of 64bd692... Flake8 CI fixes (#451):recipes/cymunk/__init__.py
=======
>>>>>>> parent of 64bd692... Flake8 CI fixes (#451):recipes/cymunk/__init__.py


class CymunkRecipe(CythonRecipe):
    version = 'master'
    url = 'https://github.com/kivy/cymunk/archive/{version}.zip'
    name = 'cymunk'
    pre_build_ext = True
    library = 'libcymunk.a'

    depends = ['python']

    def get_recipe_env(self, arch):
        ret = super(CymunkRecipe, self).get_recipe_env(arch)
        ret['CFLAGS'] += ' -Wno-implicit-function-declaration'
        return ret


recipe = CymunkRecipe()
