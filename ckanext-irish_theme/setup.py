from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='ckanext-irish_theme',
    version=version,
    description="Irish Data Gov Theme",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Maulik Kamdar',
    author_email='maulik.kamdar@deri.org',
    url='www.maulik-kamdar.com',
    license='LGPL',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.irish_theme'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        # Add plugins here, e.g.
        irish_theme=ckanext.irish_theme.plugin:IrishThemePlugin
    ''',
)
