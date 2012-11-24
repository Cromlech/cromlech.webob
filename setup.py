# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

version = '1.0-dev'

install_requires = [
    'WebOb > 1.1.1',
    'cromlech.browser >= 0.5',
    'setuptools',
    'zope.cachedescriptors',
    'zope.interface',
    ]

tests_require = [
    ]

setup(name='cromlech.webob',
      version=version,
      description="Cromlech Web Framework io implementation using WebOb",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join('src', 'cromlech', 'webob',
                                         'test_api.txt')).read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='',
      license='ZPL',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      namespace_packages=['cromlech', ],
      include_package_data=True,
      zip_safe=False,
      tests_require=tests_require,
      install_requires=install_requires,
      extras_require={'test': tests_require},
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
