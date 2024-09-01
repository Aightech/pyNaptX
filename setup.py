from setuptools import find_packages, setup
setup(
    packages=find_packages(include=['naptX']),
    version='1.1.1',
    name='naptX',
    url="https://github.com/Aightech/pyNaptX",
    description='Python library to communicate with the NaptX device',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Alexis Devillard',
    license='MIT',
    install_requires=['pyserial'],
    setup_requires=['pytest-runner', 'pyserial'],
    tests_require=['pytest==4.4.1', 'pyserial'],
    test_suite='tests',
)