from setuptools import setup

dependencies = [
    'seaborn',
    'statsmodels',
    'scipy',
    'patsy',
    'matplotlib',
    'pandas',
    'numpy'
  ]

VERSION = "0.3.4.3"

setup(
    name='pymatch_fake',
    packages=['pymatch'],
    version=VERSION,
    description='Matching techniques for Observational Studies',
    author='Ben Miroglio',
    url='https://github.com/Luzhehan/111',
    download_url='https://github.com/Luzhehan/111/archive/{}.tar.gz'.format(VERSION),
    keywords=['logistic', 'regression', 'matching', 'observational', 'study', 'causal', 'inference'],
    include_package_data=True,
    install_requires=dependencies
)
