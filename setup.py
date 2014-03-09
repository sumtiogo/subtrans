from setuptools import setup, find_packages

setup(
    name='subtrans',
    scripts=['subtrans'],
    package=find_packages(),
    install_requires=[
        'cchardet',
        'jianfan==0.0.2'
    ],
)
