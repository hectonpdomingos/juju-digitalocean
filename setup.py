from setuptools import setup, find_packages

setup(name='juju-docean',
      version="0.6.0",
      classifiers=[
          'Intended Audience :: Developers',
          'Programming Language :: Python :: 2 :: Only',
          'Operating System :: OS Independent'],
      author='Kapil Thangavelu',
      author_email='kapil.foss@gmail.com',
      description="Digital Ocean integration with juju",
      long_description=open("README.rst").read(),
      url='https://github.com/kapilt/juju-digitalocean',
      license='BSD',
      packages=find_packages(),
      install_requires=["PyYAML", "requests", "jujuclient"],
      tests_require=["nose", "mock"],
      entry_points={
          "console_scripts": [
              'juju-docean = juju_docean.cli:main']},
      )
