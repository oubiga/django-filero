from setuptools import setup, find_packages
import os

try:
    from setuptest import test
except ImportError:
    from setuptools.command.test import test

version = __import__('filer').__version__

def read(fname):
    # read the contents of a text file
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "django-filero",
    version = version,
    url = 'https://github.com/oubiga/django-filero',
    license = 'BSD',
    platforms=['OS Independent'],
    description = "A file management application for django that makes handling of files and images a breeze.",
    long_description = read('README.rst'),
    author = 'Stefan Foulis',
    author_email = 'stefan@foulis.ch',
    packages=find_packages(),
    install_requires = (
        'Django==2.2',
        'easy-thumbnails==2.2',
        'django-mptt==0.7.4',
        'django_polymorphic==0.7.1',
        'Unidecode>=0.04.17',
    ),
    include_package_data=True,
    zip_safe=False,
    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='cms_helper.run',
    tests_require=(
        'argparse',  # needed on python 2.6
        'south',
    ),
)
