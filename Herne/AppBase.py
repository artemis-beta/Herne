#============================================================================#
#                                Herne App                                   #
#                                                                            #
# Base class for creating new Herne Apps with the configurable properties    #
#                                                                            #
#============================================================================#

import logging
logging.basicConfig()

from Herne.Core import app_run, singleton

import socket
_host = socket.gethostname()

import os
import copy

_width = os.get_terminal_size().columns

class HerneApp(object, metaclass=singleton):
    __version__ = None
    _herne_logger = logging.getLogger('Herne Runner\t')
    _herne_logger.setLevel('INFO')
    _members = ['OutputLevel']
    def __call__(self):
        _opt_str=' {o} : {v}'
        print('-'*_width)
        for member in self._members:
            self._herne_logger.info(_opt_str.format(o=member, v=getattr(self, member)))
        print('-'*_width)
        self._herne_logger.info(' Application Setup Successful.')

    def __enter__(self):
        self._logger.setLevel(self.OutputLevel)
        print(self._out_str)
        return self

    def __exit__(self, type, value, traceback):
        if type:
            self._herne_logger.error("Application Failed to Complete.")
            raise value
        self._herne_logger.info(' Application Completed Successfully.')

    def __init__(self, app_name=None):
        _app_info = self.__class__.__name__ + ' ' + self.__version__
        _spacing = int(0.5*(_width-len(_app_info)))
        _nameofhost = 'Running on '+_host
        _spc2 = int(0.5*(_width-len(_nameofhost)))
        self._out_str='''
{b}
{n}
{s}
{b}
        '''.format(n=_spacing*' '+_app_info+_spacing*' ',
                   v=self.__version__, 
                   s=_spc2*' '+_nameofhost+_spc2*' ', b=_width*'=')
        if app_name:
    	     self._logger = logging.getLogger(app_name+'\t')
        for member in self._members:
            setattr(self, member, None)
        self.OutputLevel = 'INFO'
        app_run() + self
