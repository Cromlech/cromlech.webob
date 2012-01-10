from setuptools import setup, find_packages
import os

version = '0.3a1'

install_requires = [
    'WebOb > 1.1.1',
    'cromlech.browser >= 0.3a2',
    'cromlech.io >= 0.2a1',
    'grokcore.component',
    'setuptools',
    'zope.cachedescriptors',
    'zope.i18n',
    'zope.interface',
    ]

tests_require = [
    'pytest',
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
