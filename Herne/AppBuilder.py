############################################################
#
#                  Herne App Builder
#
# Provides a more convenient way of creating Herne Apps
# ready for methods to then be implemented.
#
# @author   K. Zarebski
# @date     last modified   2019-09-21
#
############################################################

import datetime
import logging

logging.basicConfig()

now = datetime.datetime.now()
now = now.strftime('%Y-%m-%d %H:%M')

class AppBuilder(object):
    def __init__(self, app_name, config_params, out_file=None, 
                 author=None, description=None):
        '''
        Construct a new Herne App as a python script

        Arguments
        ---------

        app_name           Name of the application
 
        config_params      List of configurable parameters 
                           which can be redefined in an 
                           options file

        
        Optional Arguments
        ------------------

        out_file           Change the output file name and
                           location

        author             Include an author name in the script
 
        description        Add an app description

        '''
        self._logger = logging.getLogger('AppBuilder')
        self._logger.setLevel('INFO')
        self._name = app_name
        self._author = author
        self._desc = description
        self._outfile = out_file if out_file else f'{self._name.lower()}.py'
        self._params = config_params
        self._par_str = '\n#        '.join([self._name+'().'+str(i)+' = value' for i in self._params])
        self._logger.info(f'Creating new app {self._name} in {self._outfile}')
        self._template = f'''
############################################################
#
#                      {self._name}
#
# {'{} '.format(self._desc) if self._desc else ''}
# This application was generated using the Herne AppBuilder
#
# @date  {now}
# {'@author {}'.format(self._author) if self._author else ''}
#
# Usage:
#
#    Import this app into an options script, the parameters:
#    {self._params.__str__()} are then set:
#        
#        {self._par_str}
#
############################################################ 

from Herne.AppBase import HerneApp
import copy

class {self._name}(HerneApp):
    __version__ = 'v0.1.0'
    def __init__(self):
        HerneApp.__init__(self, '{self._name}')
        self._members = copy.deepcopy(HerneApp._members)
        self._members += {self._params.__str__()}
   
    def __call__(self):
        HerneApp.__call__(self)
        
        # Write function methods here using the parameters that you have
        # assigned to your application in the form 'self.Param'
        # e.g. 'print(self.Param_1)'
'''
        self._write_to_file()

    def _write_to_file(self):
        with open(self._outfile, 'w') as f:
            f.write(self._template)
