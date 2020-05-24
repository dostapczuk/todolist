import os
from setuptools import setup

def read(fname):
    try:
        with open(os.path.join(os.path.dirname(__file__), fname)) as fh:
            return fh.read()
    except IOError:
        return ''

requirements = read('requirements.txt').splitlines()

setup(name='todolist',
      version='0.1.0',
      description='Todo List',
      url='https://github.com/dostapczuk/todolist',
      author='Daria Ostapczuk',
      author_email='daria.ostapczuk@gmail.com',
      zip_safe=False,
      install_requires=requirements,
      )
