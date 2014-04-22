#!/usr/bin/env python
from distutils.core import setup
from os import path

setup(
	name = 'bambu-analytics',
	version = '0.3',
	description = 'Provides a simple, pluggable system for analytics in Django',
	author = 'Steadman',
	author_email = 'mark@steadman.io',
	url = 'https://github.com/iamsteadman/bambu-analytics',
	long_description = open(path.join(path.dirname(__file__), 'README')).read(),
	install_requires = ['Django>=1.4'],
	namespace_packages = ['bambu'],
	packages = [
		'bambu.analytics',
		'bambu.analytics.providers',
		'bambu.analytics.templatetags'
	],
	package_data = {
		'bambu.analytics': [
			'templates/analytics/*.html',
			'templates/analytics/*.js'
		]
	},
	classifiers = [
		'Development Status :: 4 - Beta',
		'Environment :: Web Environment',
		'Framework :: Django'
	]
)
