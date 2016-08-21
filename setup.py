from setuptools import setup

setup(
    name='pybble',
    version='0.1',
    py_modules=['pybble'],
    install_requires=[
        'transcrypt',
        'envoy',
        'click',
        'pyperclip'
    ],
    entry_points='''
        [console_scripts]
        pybble=cli:cli
    ''',
)
