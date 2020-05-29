from setuptools import find_packages, setup

setup(
    name='sumopy',
    version=0.2,
    packages=find_packages(exclude=['*.tests', '*.tests.*', 'tests.*', 'tests']),
    url='https://github.com/xavivars/sumopy',
    author='Xavi Ivars',
    author_email='xavi.ivars@gmail.com',
    description='HTTP Logging handler for SumoLogic',
    install_requires=[
        'requests'
    ]
)
