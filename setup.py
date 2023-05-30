from setuptools import setup, find_packages

with open("README.md", "r") as readme:
     long_description = readme.read()



setup(
    name='openpanthera',
    version='0.0.11',
    description='simple db importer',
    py_modules=['openpanthera'],
    package_dir={'openpanthera':'src'},
    packages=['openpanthera'],
    install_requires=[
        "hny-config>=0.0.1",
        "mariadb",
    ],
    extras_require={
        "dev":[
            "pytest>=6.2"
        ]
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Topic :: Utilities'
    ],
    url='https://github.com/Soldy/openPanthera',
    author='Soldy',
    long_description=long_description,
    long_description_content_type="text/markdown"
)
