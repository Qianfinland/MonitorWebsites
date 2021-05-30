"""
Script to run tests
Usage: run.py <tags>
"""
import os
import sys
import shutil
from robot import run, pythonpathsetter


class EnvironmentSettings(object):
    target_environment = None

    def set_target(self, target_environment):
        if target_environment not in ('prod', 'preprod', 'test'):
            raise ValueError('Invalid target environment: {}'.format(target_environment))
        self.target_environment = target_environment

class RunHelper(object):

    @staticmethod
    def _validate_context(context):
        if not (context.target_environment):
            msg = 'Please define a target environment, any of: prod, preprod, test'
            raise ValueError(msg)
    
    @staticmethod
    def get_variable_file(context):
        RunHelper._validate_context(context)
        return 'libraries/src/variablefile.py:{}'.format(context.target_environment)

    @staticmethod
    def cleanup_output_directory(output_directory):
        try:
            shutil.rmtree(output_directory, ignore_errors=True)
            if not os.path.exists(output_directory):
                os.mkdir(output_directory)
        except:
            pass

    @staticmethod
    def setup_python_path():
        # Extend python libraries with the following paths
        current_dir = os.getcwd()
        paths = []
        paths.append(os.path.join(current_dir, 'libraries', 'src'))
        for path in paths:
            print('Adding to python search path: {}'.format(path))
            pythonpathsetter.add_path(path, end=True)

# Main routine
context = EnvironmentSettings()
target = os.environ['TARGET_ENVIRONMENT'] if os.environ.get('TARGET_ENVIRONMENT') else 'prod'
context.set_target(target)

out_dir = 'output'

RunHelper.cleanup_output_directory(out_dir)

RunHelper.setup_python_path()
sources_location = 'tests'
rc = run(sources_location,
         outputdir=out_dir,
         loglevel='TRACE',
         variablefile=RunHelper.get_variable_file(context)
         )
sys.exit(rc)
