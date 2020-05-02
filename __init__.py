# make treacl a module



# __version__ = "19.3.0"
# __version_info__ = VersionInfo._from_version_string(__version__)

# __title__ = "attrs"
# __description__ = "Classes Without Boilerplate"
# __url__ = "https://www.attrs.org/"
# __uri__ = __url__
# __doc__ = __description__ + " <" + __uri__ + ">"

# __author__ = "Hynek Schlawack"
# __email__ = "hs@ox.cx"

# __license__ = "MIT"
# __copyright__ = "Copyright (c) 2015 Hynek Schlawack"



# from see

"""
see: dir for humans.

Documentation is available at https://ljcooke.github.io/see/

"""
from .inspector import see
from .output import SeeResult


__all__ = ['see', 'SeeResult']

__author__ = 'Liam Cooke'
__contributors__ = 'See AUTHORS.rst'
__version__ = '1.4.1'
__copyright__ = 'Copyright (c) 2009-2017 Liam Cooke'
__license__ = 'BSD License'
