#!/usr/bin/env python

from __future__ import with_statement

import sys
from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

long_description = """
To find out what's new in this version of Fabric, please see `the changelog
<http://fabfile.org/changelog.html>`_.

You can also install the `in-development version
<https://github.com/fabric/fabric/tarball/master#egg=fabric-dev>`_ using
pip, with `pip install fabric==dev`.

----

%s

----

For more information, please see the Fabric website or execute ``fab --help``.
""" % (readme)



setup(
    name='Gael Deploy',
    version=get_version('short'),
    description='Gael Deploy is a simple & fast tool for deployment.',
    long_description=long_description,
    author='Daniel Soria',
    author_email='danielsoriacoronel@gmail.com',
    url='http://www.azhtom.com',
    packages=find_packages(),
    install_requires=install_requires,
    # entry_points={
    #     'console_scripts': [
    #         'fab = fabric.main:main',
    #     ]
    # },
    # classifiers=[
    #       'Development Status :: 5 - Production/Stable',
    #       'Environment :: Console',
    #       'Intended Audience :: Developers',
    #       'Intended Audience :: System Administrators',
    #       'License :: OSI Approved :: BSD License',
    #       'Operating System :: MacOS :: MacOS X',
    #       'Operating System :: Unix',
    #       'Operating System :: POSIX',
    #       'Programming Language :: Python',
    #       'Programming Language :: Python :: 2.5',
    #       'Programming Language :: Python :: 2.6',
    #       'Programming Language :: Python :: 2.7',
    #       'Topic :: Software Development',
    #       'Topic :: Software Development :: Build Tools',
    #       'Topic :: Software Development :: Libraries',
    #       'Topic :: Software Development :: Libraries :: Python Modules',
    #       'Topic :: System :: Clustering',
    #       'Topic :: System :: Software Distribution',
    #       'Topic :: System :: Systems Administration',
    # ],
)
