#!/usr/bin/env python
from setuptools import setup
from os import path

setup(
	name = 'bambu-analytics',
	version = '2.0',
	description = 'Provides a simple, pluggable system for analytics in Django',
	author = 'Steadman',
	author_email = 'mark@steadman.io',
	url = 'https://github.com/iamsteadman/bambu-analytics',
	long_description = open(path.join(path.dirname(__file__), 'README')).read(),
	install_requires = ['Django>=1.4'],
	packages = [
		'bambu_analytics',
		'bambu_analytics.providers',
		'bambu_analytics.templatetags'
	],
	package_data = {
		'bambu_analytics': [
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
