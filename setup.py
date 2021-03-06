import sys
from setuptools import setup

if sys.version_info >= (3,0):
    description = open('README.md', encoding='utf-8').read()
else:
    description = open('README.md').read()

setup(
    name='unicode-slugify',
    version='0.1.4',
    description='A slug generator that turns strings into unicode slugs.',
    long_description=description,
    author='Jeff Balogh, Dave Dash',
    author_email='jbalogh@mozilla.com, dd@mozilla.com',
    url='http://github.com/mozilla/unicode-slugify',
    license='BSD',
    packages=['slugify'],
    include_package_data=True,
    package_data={'': ['README.md']},
    zip_safe=False,
    install_requires=['six', 'unidecode'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Environment :: Web Environment :: Mozilla',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)


