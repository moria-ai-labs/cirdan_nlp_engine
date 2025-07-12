from setuptools import setup, find_packages

setup(
    name="spell_checker",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'editdistance'
    ],
    entry_points={
        'console_scripts': [],
    },
)
