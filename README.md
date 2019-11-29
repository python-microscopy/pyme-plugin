# python-microscopy-plugin-template
Template for making plug-ins for the Python-Microscopy Environment (PYME)

## Instructions
1. Clone the repository, add your recipe module files, dsviewer module files, and visgui module files to the respective
folders in `pyme-plugin/package_name`. 
2. Change the name of the ```pyme-plugin/package_name``` directory.
3. In the `_etc/PYME/plugins/` folder, go into the `dsviewer`, `recipes`, and `visgui` folders and edit
`package_name.txt` to include your actual package name, and to point to each of your module files with a new line, e.g. 
two dsviewer module files could have a `package_name.txt` file like this:
```
#mynewpackage.python_microscopy.dsviewer_modules.first_module_file_without_the_file_extension
#mynewpackage.python_microscopy.dsviewer_modules.second_module_file_without_the_file_extension
```
4. Change the filenames of the `package_name.txt` files to match your package.
5. Run `python install_plugin.py` to make PYME aware of the
6. Install your package however you need to install it e.g. distutils, etc.
 
