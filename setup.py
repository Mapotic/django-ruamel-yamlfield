import setuptools

setuptools.setup(
    name="django-yamlfield",
    version="0.1.0",
    description='A Django database field for storing YAML data with Ruamel yaml implementation',
    author='Martin Kubát',
    author_email='martin.kubat@mapotic.com',
    url="https://github.com/Mapotic/django-ruamel-yamlfield",
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
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=(
        'ruamel.yaml>=0.17'
    ),
)

