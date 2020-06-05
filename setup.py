from setuptools import setup

setup(
    name='ipcalc',
    version='1.0.0',
    description='a tool for helping people with ip calculation',
    url='https://github.com/KalleDK/py-ipcalc',
    author='Kalle M. Aagaard',
    author_email='pip@k-moeller.dk',
    license='MIT',
    packages=[
        'ipcalc',
    ],
    python_requires='>=3.6.0',
    entry_points={'console_scripts': [
        'ipcalc = ipcalc.__main__:main',
    ]}
)
