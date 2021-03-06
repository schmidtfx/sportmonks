
import sys
import os.path
from setuptools import find_packages, setup, Command
from sportmonks import __version__
from shutil import rmtree


class UploadCommand(Command):
    """ Shamelessly copied from Kenneth Reitz. """

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPi via Twine…')
        os.system('twine upload dist/*')

        sys.exit()


setup(
    name='sportmonks',
    version=__version__,
    description='Pythonic wrapper around SportMonks API.',
    long_description='Pythonic wrapper around SportMonks API.',
    author='Dmitrii Izgurskii',
    author_email='izgurskii@gmail.com',
    url='https://github.com/Dmitrii-I/sportmonks',
    license='MIT',
    packages=find_packages(exclude=['contrib', 'docs', '*test*']),
    install_requires=['requests'],
    python_requires='>=3.5.2',
    cmdclass={'upload': UploadCommand}
)
