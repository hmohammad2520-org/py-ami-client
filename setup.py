from setuptools import find_packages, setup

setup(
    name='py-ami-client',
    version='0.1.2',
    license="MIT",
    description='Python Asterisk Management Interface Client',
    author='Radin-System',
    author_email='technical@rsto.ir',
    url='https://github.com/Radin-System/py-ami-client',
    install_requires=[
        "classmods==1.0.0",
    ],
    packages=find_packages(exclude=['test', 'test.*']),
    include_package_data=True,
    zip_safe=False,
)