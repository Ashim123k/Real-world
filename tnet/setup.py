from setuptools import setup, find_packages

setup(
    name='ants',
    version='0.2',
    py_modules=['ants'],
    install_requires=[
        'click'
    ],
    entry_points='''
        [console_scripts]
        tnet=ant:ant
    ''',
)