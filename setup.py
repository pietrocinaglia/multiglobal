from setuptools import setup

setup(
    version='1.1',
    description='Multilayer Global-Aligner (MultiGlobAl) allows performing the pairwise global alignment of multilayer networks.',
    author='Pietro Cinaglia',
    author_email='cinaglia@unciz.it',
    url='https://github.com/pietrocinaglia/multiglobal',
    install_requires=[
        'gensim==4.3.1',
        'joblib==1.2.0',
        'networkx==2.8.6',
        'numpy==1.23.2',
        'pandas==2.0.3',
        'PySimpleGUI==4.60.5',
        'setuptools==65.5.0',
        'tqdm==4.64.0',
        'Unipath==1.1',
    ],
)

import platform
if platform.system() == 'Linux':
    from subprocess import STDOUT, check_call
    import os
    check_call(['apt-get', 'install', '-y', 'python3-tk'],
        stdout=open(os.devnull,'wb'), stderr=STDOUT) 


