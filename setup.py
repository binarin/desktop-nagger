from setuptools import setup

setup(name='desktop_nagger',
      version='0.1',
      description='Displays desktop notifications in an annoying fashion.',
      url='http://github.com/binarin/desktop-nagger',
      author='Alexey Lebedeff',
      author_email='binarin@gmail.com',
      license='MIT',
      packages=['desktop_nagger'],
      install_requires=[
          "pygtk"
      ],
      zip_safe=False)
