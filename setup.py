#!/usr/bin/env python

# Fill out this template to enable setuptools installation of your plugin as a
# Python package, i.e. `python setup.py develop` or `python setup.py install`.
# This script it set up to additionally register the plugin with PYME in a post-
# install command by running the included `install_plugin.py` script. You can
# get arbitrarily fancy there if you like in terms of configuring your plugin.

# Replace 'package_name' with the name of your plugin. This must be importable,
# and will point towards the directory by the same name in your repository. For
# example you might call your repository directory 'pyme-plugin' but the
# directory inside of it which stores all of your installable python code should
# be called 'pyme_plugin'.
PACKAGE_NAME = 'package_name'
# Set your version, as a string. Something like YY.MM.DD works well here
PACKAGE_VERSION = '00.00.00'
# Include a short description of your package. This might eventually get
# displayed in e.g. Anaconda cloud if you build/upload packages, etc.
PACKAGE_DESCRIPTION = 'What your plugin does'

# -------- If you filled in everything up to here you should be set ------------

from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install

def install_pyme_plugin():
    import sys
    import subprocess
    import os
    plugin_install_path = os.path.join(os.path.dirname(__file__), PACKAGE_NAME,
                                       'install_plugin.py')
    subprocess.Popen('%s %s' % (sys.executable, plugin_install_path), 
                        shell=True)


class DevelopModuleAndInstallPlugin(develop):
    """Post-installation for development mode."""
    def run(self):
        develop.run(self)
        install_pyme_plugin()
        

class InstallModuleAndInstallPlugin(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        install_pyme_plugin()


setup(
    name=PACKAGE_NAME,
    version=PACKAGE_VERSION,
    description=PACKAGE_DESCRIPTION,
    packages=find_packages(),
    cmdclass={
        'develop': DevelopModuleAndInstallPlugin,
        'install': InstallModuleAndInstallPlugin,
    },
)
