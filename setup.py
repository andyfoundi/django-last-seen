#!/usr/bin/env python
from __future__ import unicode_literals
from distutils.core import setup
import os

__author__ = 'Ferran Pegueroles'
__copyright__ = 'Copyright 2013, Ferran Pegueroles'
__credits__ = ['Ferran Pegueroles']


__license__ = 'GPL'
__version__ = '0.4'
__email__ = 'ferran@pegueroles.com'


long_description = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()


setup(
    name='django-last-seen',
    version=__version__,
    url='http://bitbucket.org/ferranp/django-last-seen',
    author=__author__,
    author_email=__email__,
    license='GPL',
    packages=['last_seen', 'last_seen.migrations'],
    description='Keep track of when a user has been last seen',
    long_description=long_description,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ]
)
