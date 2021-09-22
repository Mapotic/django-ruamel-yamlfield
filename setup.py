#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from distutils.core import Command


class TestCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        from django.conf import settings
        settings.configure(
            DATABASES={
                'default': {
                    'NAME': ':memory:',
                    'ENGINE': 'django.db.backends.sqlite3'
                }
            },
            MIDDLEWARE_CLASSES=(),
            INSTALLED_APPS=('yamlfield',)
        )
        from django.core.management import call_command
        import django
        django.setup()
        call_command('test', 'yamlfield')


setup(
    name='django-ruamel-yamlfield',
    version='0.1',
    description='A Django database field for storing YAML data with Ruamel yaml implementation',
    author='Martin Kubát',
    author_email='martin.kubat@mapotic.com',
    url="https://github.com/Mapotic/django-ruamel-yamlfield",
    packages=find_packages(),
    include_package_data=True,
    license="MIT",
    install_requires=(
        'ruamel.yaml>=0.17'
    ),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.1',
        'License :: OSI Approved :: MIT License',
    ],
    cmdclass={'test': TestCommand,}
)