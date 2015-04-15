''' s0lst1c3 - TitleBar '''

from setuptools import setup


def read(*paths):
    ''' build a file path from *paths* and return the contents.'''
    with open(os.path.join(*paths), 'r') as input_handle:
        return input_handle.read()

setup(
    name='titlebar',
    version='0.1.0',
    description='Easy to use dynamic titlebar module for command line utils.',
    long_description=('\n\n'.join([
                    read('README.rst'),
                    read('HISTORY.rst'),
                    read('AUTHORS.rst')])),
    url='https://github.com/s0lst1c3/titlebar',
    license='MIT',
    author='John Gabriel Ryan',
    author_email='contact@solstice.me',
    py_modules=['titlebar'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
