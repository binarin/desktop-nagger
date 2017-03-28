from setuptools import setup, find_packages

setup(name='desktop_nagger',
      version='0.1',
      description='Displays desktop notifications in an annoying fashion.',
      url='http://github.com/binarin/desktop-nagger',
      author='Alexey Lebedeff',
      author_email='binarin@gmail.com',
      license='MIT',
      packages=find_packages(),
      # install_requires=[
      #     "pygtk >= 2.24.0"
      # ],
      entry_points="""
      [console_scripts]
      desktop-nagger = desktop_nagger:main
      """,
      include_package_data=True)
