from PYME import config
import os
import sys
from distutils.dir_util import copy_tree

def main():
    this_dir = os.path.dirname(__file__)

    try:
        if sys.argv[1] == 'dist':
            copy_tree(os.path.join(this_dir, 'plugins'), 
                      os.path.join(config.dist_config_directory, 'plugins'))
    except IndexError:  # no argument provided, default to user config directory
        copy_tree(os.path.join(this_dir, 'plugins'), 
                  os.path.join(config.user_config_dir, 'plugins'))

if __name__ == '__main__':
    main()