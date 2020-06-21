import unittest
from hypothesis import given, strategies, settings, example, assume
from Herne.AppBase import HerneApp
from Herne.AppBuilder import AppBuilder

import os
import string
import subprocess
import shutil

class TestHerne(unittest.TestCase):
    @given( app_name = strategies.text(
                alphabet = string.ascii_lowercase,
                min_size = 5,
                max_size = 10 ),
            configurable_parameters = strategies.lists(
                strategies.text(
                    alphabet = string.ascii_lowercase,
                    min_size = 5,
                    max_size = 10 ),
                min_size = 6,
                max_size = 6 ),
            values = strategies.lists( 
                strategies.text(
                    alphabet = string.ascii_lowercase,
                    min_size = 4,
                    max_size = 10 ),
                min_size = 6,
                max_size = 6 )
            )
    @settings( deadline=None )
    @example( app_name='HerneTest', configurable_parameters=['Var1', 'Var2'], values=['Val1', 'Val2'] )
    def testAppBuilder( self, app_name, configurable_parameters, values ):
        _folder_name = app_name.replace(" ", "_")
        _interface = os.path.join(_folder_name, 'Configurables.py')
        _opts_file = _folder_name+'.py'

        os.mkdir(_folder_name) # Create Dummy Python Module

        # Create 'Configurables.py' (Herne Interface definition) script
        _builder = AppBuilder( app_name, configurable_parameters,
                out_file = _interface )

        # Create Options script
        with open(_opts_file, 'w') as f:
            _str = '\n'.join([f'{_folder_name}().{i} = "{j}"' for i, j in zip(configurable_parameters, values)])
            f.write(_str)

        # Run Herne and Check Exit 0
        self.assertFalse(subprocess.check_call(f'./run {_interface} {_opts_file}', shell=True, stdout=subprocess.DEVNULL ))

        # Clean Up
        assert(not subprocess.check_call( f'rm {_opts_file}', shell=True ))
        assert(not subprocess.check_call( f'rm -rf {_folder_name}', shell=True ))


if __name__ in "__main__":
    unittest.main()
