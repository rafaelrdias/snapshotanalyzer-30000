from setuptools import setup

setup(
    name='snapshotanalyser-30000',
    version='0.01',
    author='Rafael Dias',
    author_email='rafaelroberto.dias@gmail.com',
    description='SnapshotAlyzer 30000 is a tool to manage AWS EC2 snapshots',
    license='GPLv3',
    packages=['shotty'],
    url='https://github.com/rafaelrdias/snapshotanalyzer-30000',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
            [console_scripts]
            shotty=shotty.shotty:cli
    ''',
    )
